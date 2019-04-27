import operator
import random

from DistributionTransformers.NormalizeTransformer import NormalizeTransformer
from ProbabilityDistribution import ProbabilityDistribution
from WikiWordDistribution.IterativeRegression import IterativeRegression
from WikiWordDistribution.NumbericParser import NumbericParser
from WikiWordDistribution.ImportanceFilter import ImportanceFilter
from WikiWordDistribution.Linker import linker, Candidates
from WikiWordDistribution.WordParser import WordParser

class WikiWordDistribution(ProbabilityDistribution):
    def __init__(self, strict):
        self.strict = strict

    def compute_distribution(self, season, episode):
        occurrences = WordParser.total_parse(linker)
        importance_filter = ImportanceFilter()
        importance_filter.compute(linker, occurrences, 1)
        important_words = list(importance_filter.important_words)
        important_words.sort()
        print(len(important_words))
        print(important_words)
        season_occurrences = importance_filter.season_occurrences
        numberic_data = NumbericParser.parse(linker, occurrences, season_occurrences, important_words)
        data_linker = self.get_data_linker(season)
        regression = IterativeRegression.find_best_regression(data_linker, numberic_data, len(important_words), 10,
                        0.01, 1000.0, 0.999, 1)
        print(regression.compute(Candidates.JAN_18, numberic_data))
        print([important_words[i] for i in regression.includes])
        print(regression.reg)
        input_linker = self.get_input_linker(season)
        dis = dict()
        for row in input_linker:
            candidate = row[0]
            dis[candidate] = regression.compute(candidate, numberic_data)
        normalizer = NormalizeTransformer()
        return normalizer.transform_distribution(dis)

    def get_input_linker(self, season):
        input_linker = []
        for row in linker:
            if row[1] == season:
                input_linker.append(row)
        return input_linker

    def get_data_linker(self, season):
        data_linker = []
        for row in linker:
            if self.strict and row[1] < season:
                data_linker.append(row)
            elif not self.strict and row[1] != season:
                data_linker.append(row)
        return data_linker