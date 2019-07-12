import numpy

from gurobipy import *
import math

from WikiWordDistribution.DataPredictors.DataPredictor import DataPredictor

class SpecialLinearRegression(DataPredictor):
    def __init__(self, max_run_time, error_rate, bias, max_coefs, max_diff, weights = None):
        if weights == None:
            weights = dict()
        self.max_run_time = max_run_time
        self.error_rate = error_rate
        self.bias = bias
        self.max_coefs = max_coefs
        self.max_diff = max_diff
        self.weights = weights

    def train(self, train_input, train_output):
        mol_output = self.inv_sigmoid(1.0 - 9.0 * self.error_rate)
        non_mol_output = self.inv_sigmoid(self.error_rate)
        ac = list(train_input.keys())[0] # An arbitrary candidate
        to_loop = len(train_input[ac])
        if self.bias:
            to_loop -= 1

        model = Model("Wiki Distribution")

        # The variables
        activated_vars = [] # Binary variables that indicate whether a coefficient is used or not
        coefficient_vars = [] # The variables that represent the coefficients of the linear function
        error_vars = dict() # The variables that is the difference between every real output and regression output
        for i in range(to_loop):
            activated_vars.append(model.addVar(vtype=GRB.BINARY))
        for i in range(len(train_input[ac])):
            coefficient_vars.append(model.addVar(lb=-GRB.INFINITY, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS))
        for c in train_input:
            error_vars[c] = model.addVar(lb=-GRB.INFINITY, ub=GRB.INFINITY, vtype=GRB.CONTINUOUS)

        # The objective function (which is the squares of the error values)
        obj = LinExpr()
        for c in train_input:
            obj += self.weights.get(c, 1.0) * error_vars[c] * error_vars[c]
        model.setObjective(obj, GRB.MINIMIZE)

        # Definition of error rate
        for c in train_input:
            real_output = mol_output if train_output[c] == 1 else non_mol_output
            con = LinExpr()
            for j in range(len(train_input[ac])):
                con += train_input[c][j] * coefficient_vars[j]
            con += -1.0 * error_vars[c]
            model.addConstr(lhs=con, sense=GRB.EQUAL, rhs=real_output)

        # Definition of activated variable
        for i in range(to_loop):
            model.addConstr(coefficient_vars[i] - self.max_diff * activated_vars[i] <= 0)
            model.addConstr(coefficient_vars[i] + self.max_diff * activated_vars[i] >= 0)

        # Maximum number of activated variables
        con = LinExpr()
        for i in range(to_loop):
            con += activated_vars[i]
        model.addConstr(lhs=con, sense=GRB.LESS_EQUAL, rhs=self.max_coefs)

        # Solve the model
        model.Params.OutputFlag = 0
        model.Params.timelimit = self.max_run_time
        model.optimize()

        self.coefs = []
        for i in range(len(train_input[ac])):
            self.coefs.append(coefficient_vars[i].x)

    def predict(self, predict_input):
        predict_output = dict()
        for c in predict_input:
            predict_output[c] = self.sigmoid(numpy.dot(predict_input[c], self.coefs))
        return predict_output

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def inv_sigmoid(self, x):
        return math.log(x / (1 - x))