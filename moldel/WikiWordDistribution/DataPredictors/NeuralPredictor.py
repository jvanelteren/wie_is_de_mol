from WikiWordDistribution.DataPredictors.DataPredictor import DataPredictor
import numpy as np

from keras.models import Sequential
from keras.layers import Dense

class NeuralPredictor(DataPredictor):
    def __init__(self, epochs):
        self.epochs = epochs

    def array_convert(self, dictionary, candidates):
        return np.array([np.array(dictionary[c]) for c in candidates])

    def train(self, train_input, train_output):
        candidates = [c for c in train_input]
        ac = list(train_input.keys())[0]  # An arbitrary candidate
        input_size = len(train_input[ac])
        arr_train_input = self.array_convert(train_input, candidates)
        arr_train_output = self.array_convert(train_output, candidates)
        self.model = Sequential()
        self.model.add(Dense(1, input_shape=(input_size,), activation="relu"))
        self.model.add(Dense(1, activation="sigmoid"))
        self.model.compile(optimizer='sgd', loss='mse')
        self.model.fit(arr_train_input, arr_train_output, epochs=self.epochs, batch_size=16, verbose=0)

    def predict(self, predict_input):
        candidates = [c for c in predict_input]
        acc_predict_input = self.array_convert(predict_input, candidates)
        acc_predict_output = self.model.predict(acc_predict_input)
        predict_output = [out[0] for out in acc_predict_output]
        return dict(zip(candidates, predict_output))
