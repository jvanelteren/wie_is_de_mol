import math
import random

from WikiWordDistribution.Regression import Regression

class IterativeRegression:
    @staticmethod
    def find_best_regression(data_linker, numberic_data, total_num_words, num_selected, error_margin, start_temp,
                             dec_temp, stop_temp):
        temp = start_temp
        best_sample = random.sample(range(total_num_words), num_selected)
        best_regression = Regression(data_linker, numberic_data, best_sample, error_margin)
        best_score = best_regression.get_regression_error()
        while temp >= stop_temp:
            sample = IterativeRegression.get_neighbour(best_sample, total_num_words)
            regression = Regression(data_linker, numberic_data, sample, error_margin)
            score = regression.get_regression_error()
            if IterativeRegression.accept(best_score, score, temp):
                best_sample = sample
                best_regression = regression
                best_score = score
            temp *= dec_temp
        print(best_score)
        return best_regression

    @staticmethod
    def get_neighbour(sample, total_num_words):
        new_sample = sample.copy()
        from_set = set(range(total_num_words)).difference(set(new_sample))
        new_item = random.choice(list(from_set))
        removed_index = random.choice(range(len(sample)))
        new_sample.pop(removed_index)
        new_sample.append(new_item)
        return new_sample

    @staticmethod
    def accept(best_score, new_score, temp):
        chance = 1 / (1 + math.exp((new_score - best_score) / temp))
        return random.random() < chance
