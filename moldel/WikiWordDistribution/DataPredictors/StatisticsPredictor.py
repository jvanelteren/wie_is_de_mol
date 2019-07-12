from WikiWordDistribution.DataPredictors.DataPredictor import DataPredictor

class StatisticsPredictor(DataPredictor):
    def train(self, train_input, train_output):
        ac = list(train_input.keys())[0] # An arbitrary candidate
        input_size = len(train_input[ac])
        self.non_contains_prob = []
        self.contains_prob = []

        for i in range(input_size):
            cand_0 = [c for c in train_input if train_input[c][i] == 0.0 and train_output[c] == 0]
            mol_0 = [c for c in train_input if train_input[c][i] == 0.0 and train_output[c] == 1]
            cand_1 = [c for c in train_input if train_input[c][i] == 1.0 and train_output[c] == 0]
            mol_1 = [c for c in train_input if train_input[c][i] == 1.0 and train_output[c] == 1]
            self.non_contains_prob.append(len(mol_0) / (len(cand_0) + len(mol_0)))
            self.contains_prob.append(len(mol_1) / (len(cand_1) + len(mol_1)))

    def predict(self, predict_input):
        input_size = len(self.contains_prob)
        predict_output = dict()

        for c in predict_input:
            prob = 1.0
            for i in range(input_size):
                if predict_input[c][i] == 1.0:
                    prob *= self.contains_prob[i]
                else:
                    prob *= self.non_contains_prob[i]
            predict_output[c] = prob

        return predict_output