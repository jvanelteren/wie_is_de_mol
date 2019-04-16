import math

import numpy as np

from DistributionTransformers.NormalizeTransformer import NormalizeTransformer
from PersonDistribution.Data import *
from PersonDistribution.Regression import Regression
from ProbabilityDistribution import ProbabilityDistribution

class PersonDistribution(ProbabilityDistribution):
    def __init__(self, strict, error_marge, job_threshold, age_split, popularity_split):
        """ Create an person distribution class.
        Arguments:
            strict (bool): False means that all data except data from that season may be used, True means that only
            data from earlier seasons might be used.
            error_marge (float): The probability that a non-Mol candidate still is the Mol. Setting this value higher
            means that the probability distribution will converge more to an uniform distribution.
            job_threshold (int): The job is only taken into account if it occurs at least this number of times in the
            list of candidates.
            age_split (int): In how much categories the age will get split up.
            popularity_split (int): In how much categories the popularity will get split up. """
        self.strict = strict
        self.error_marge = error_marge
        self.job_threshold = job_threshold
        self.age_split = age_split
        self.popularity_split = popularity_split

    def compute_distribution(self, season, episode):
        input_data = self.input_data(season, person_data)
        filtered_data = self.filter_data(season, person_data)
        sig_jobs = self.significant_jobs(filtered_data, self.job_threshold)
        age_groups = self.data_splits(filtered_data, "age", self.age_split)
        popularity_groups = self.data_splits(filtered_data, "popularity", self.popularity_split)

        filtered_data_input = []
        filtered_data_output = []
        for row in filtered_data:
            filtered_data_input.append(self.parse_input_row(row, sig_jobs, age_groups, popularity_groups))
            filtered_data_output.append(self.parse_output_row(row))
        regression = Regression(filtered_data_input, filtered_data_output)

        distribution = dict()
        for row in input_data:
            candidate = data_from_row(row, "candidate")
            distribution[candidate] = \
                regression.compute(self.parse_input_row(row, sig_jobs, age_groups, popularity_groups))
        normalizer = NormalizeTransformer()
        return normalizer.transform_distribution(distribution)

    def parse_input_row(self, row, sig_jobs, age_groups, popularity_groups):
        # Add the boolean variables to the input
        parsed_input = [self.bool_to_num(row, "gender"), self.bool_to_num(row, "actor-school")]
        jobs = data_from_row(row, "jobs") # Add the significant job values to the input
        for j in sig_jobs:
            if j in jobs:
                parsed_input.append(1)
            else:
                parsed_input.append(0)
        parsed_input.extend(self.group_input(row, "age", age_groups)) # Add the age and popularity to the input
        parsed_input.extend(self.group_input(row, "popularity", popularity_groups))
        parsed_input.append(1) # Add the bias
        return parsed_input

    def parse_output_row(self, row):
        if data_from_row(row, "mol"):
            return 1.0 - 9.0 * self.error_marge
        else:
            return self.error_marge

    def data_splits(self, data, var, split_nums):
        var_data = [data_from_row(row, var) for row in data]
        splits = []
        for i in range(1, split_nums):
            splits.append(np.percentile(var_data, 100.0 / split_nums * i))
        splits.append(math.inf)
        return splits

    def significant_jobs(self, data, threshold):
        significant_jobs = []
        jobs_occurence = dict()
        for row in data:
            jobs = data_from_row(row, "jobs")
            for j in jobs:
                jobs_occurence[j] = jobs_occurence.get(j, 0) + 1
        for j in Jobs:
            if jobs_occurence.get(j, 0) >= threshold:
                significant_jobs.append(j)
        return significant_jobs

    def group_input(self, row, var, groups):
        input = [0 for i in range(len(groups))]
        value = data_from_row(row, var)
        i = 0
        while value > groups[i]:
            i += 1
        input[i] = 1
        return input

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

    def bool_to_num(self, row, var):
        if data_from_row(row, var):
            return 1
        else:
            return 0
