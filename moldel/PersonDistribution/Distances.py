from PersonDistribution.Data import *

class Distances:
    """ Class used to compute distances between candidates. """

    def __init__(self, filtered_data, weights, exponent):
        self.distance_weights = {"season": 0.0, "age": 0.0, "popularity": 0.0, "gender": 0.0, "actor-school": 0.0,
                                 "jobs": 0.0}
        self.exponent = exponent
        count = 0

        for row1 in filtered_data:
            for row2 in filtered_data:
                count += 1
                for var in self.distance_weights:
                    self.distance_weights[var] += self.var_distance(row1, row2, var)

        for var in self.distance_weights:
            self.distance_weights[var] /= count
            self.distance_weights[var] *= weights[var]

    def rev_distance(self, row1, row2):
        distance = self.distance(row1, row2)
        return 1.0 / (1.0 + distance)

    def distance(self, row1, row2):
        distance = 0.0
        for var, weight in self.distance_weights.items():
            distance += weight * self.var_distance(row1, row2, var)
        return distance

    def var_distance(self, row1, row2, var):
        x = data_from_row(row1, var)
        y = data_from_row(row2, var)

        if var == "season" or var == "age" or var == "popularity":
            return self.num_distance(x, y)
        elif var == "gender" or var == "actor-school":
            return self.bool_distance(x, y)
        elif var == "jobs":
            return self.set_distance(x, y)

    def num_distance(self, x, y):
        return pow(x - y, 2)

    def bool_distance(self, x, y):
        return x != y

    def set_distance(self, x, y):
        max_size = max(len(x), len(y))
        intersect = x.intersection(y)
        distance = max_size - len(intersect)
        return distance / max_size
