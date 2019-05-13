from WikiWordDistribution.DataPredictors.DataPredictor import DataPredictor

class NearestNeighbour(DataPredictor):
    def train(self, train_input, train_output):
        self.train_input = train_input
        self.train_output = train_output

    def predict(self, predict_input):
        weights = []
        

    def distance(self, ):