from DistributionTransformers.NormalizeTransformer import NormalizeTransformer
from PersonDistribution.Data import *
from PersonDistribution.Distances import Distances
from ProbabilityDistribution import ProbabilityDistribution

class PersonDistribution(ProbabilityDistribution):
    def __init__(self, strict):
        """ Create an person distribution class.
        Arguments:
            strict (bool): False means that all data except data from that season may be used, True means that only
            data from earlier seasons might be used """
        self.strict = strict

    def compute_distribution(self, season, episode):
        input_data = self.input_data(season, person_data)
        filtered_data = self.filter_data(season, person_data)
        weights = {"season": 0.001, "age": 0.01, "popularity": 0.01, "gender": 0.00, "actor-school": 0.01, "jobs": 0.01}
        distances = Distances(filtered_data, weights, 0.5)
        distribution = dict()
        for r in input_data:
            candidate = data_from_row(r, "candidate")
            print("Testing: " + candidate.value)
            distribution[candidate] = 0.0
            total_distance = 0.0
            for r2 in filtered_data:
                total_distance += distances.rev_distance(r, r2)
            for r2 in filtered_data:
                is_mol = data_from_row(r2, "mol")
                if is_mol:
                    distance = distances.rev_distance(r, r2) / total_distance
                    distribution[candidate] += distance
                    print(data_from_row(r2, "candidate").value + ": " + str(distance))
        normalizer = NormalizeTransformer()
        return normalizer.transform_distribution(distribution)

    def input_data(self, season, data):
        input_data = []
        for row in data:
            row_season = data_from_row(row, "season")
            if row_season == season:
                input_data.append(row)
        return input_data

    def filter_data(self, season, data):
        filtered_data = []
        for row in data:
            row_season = data_from_row(row, "season")
            if self.strict and row_season < season:
                filtered_data.append(row)
            elif not self.strict and row_season != season:
                filtered_data.append(row)
        return filtered_data

