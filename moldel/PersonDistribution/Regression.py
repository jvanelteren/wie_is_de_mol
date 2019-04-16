import math
import numpy as np

class Regression:
    def __init__(self, input, output):
        con_output = [self.inv_sigmoid(x) for x in output]
        self.coef = np.linalg.lstsq(input, output, rcond = -1)[0]

    def compute(self, new_input):
        res = np.dot(new_input, self.coef)
        return self.sigmoid(res)

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

    def inv_sigmoid(self, x):
        return -1 * math.log((1 / x) - 1)