import math
import numpy as np

class Regression:
    def __init__(self, data_linker, numberic_data, includes, error_margin):
        input = self.selected_input(data_linker, numberic_data, includes)
        output = self.selected_output(data_linker, error_margin)
        self.includes = includes
        result = np.linalg.lstsq(input, output, rcond = -1)
        self.reg = result[0]
        if len(result[1]) == 0:
            self.sqrt_error = math.inf
        else:
            self.sqrt_error = result[1][0]

    def compute(self, candidate, numberic_data):
        new_input = self.selected_candidate_input(candidate, numberic_data, self.includes)
        res = np.dot(new_input, self.reg)
        return self.sigmoid(res)

    def get_regression_error(self):
        return self.sqrt_error

    def selected_input(self, data_linker, numberic_data, includes):
        selected = []
        for row in data_linker:
            selected.append(self.selected_candidate_input(row[0], numberic_data, includes))
        return selected

    def selected_candidate_input(self, candidate, numberic_data, includes):
        candidate_selected = []
        for incl in includes:
            candidate_selected.append(numberic_data[candidate][incl])
        candidate_selected.append(1)
        return candidate_selected

    def selected_output(self, data_linker, error_margin):
        selected = []
        for row in data_linker:
            selected.append(self.output_score(row[3], error_margin))
        return selected

    def output_score(self, is_mol, error_margin):
        if is_mol:
            return self.inv_sigmoid(1 - 9 * error_margin)
        else:
            return self.inv_sigmoid(error_margin)

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def inv_sigmoid(self, x):
        return -1 * math.log((1 / x) - 1)