import math

class WordOccurenceTransformation:
    @staticmethod
    def combined_keys(occurrences):
        keys = set()
        for occ in occurrences:
            keys.update(occ.keys())
        return keys

    @staticmethod
    def add(occurrences):
        new_occurrence = dict()
        keys = WordOccurenceTransformation.combined_keys(occurrences)
        for k in keys:
            sum = 0
            for occ in occurrences:
                sum += occ.get(k, 0)
            new_occurrence[k] = sum
        return new_occurrence

    @staticmethod
    def min(occurrences):
        new_occurrence = dict()
        keys = WordOccurenceTransformation.combined_keys(occurrences)
        for k in keys:
            min_res = math.inf
            for occ in occurrences:
                min_res = min(occ.get(k, 0), min_res)
            new_occurrence[k] = min_res
        return new_occurrence

    @staticmethod
    def filter(occurrence, threshold):
        new_occurence = dict()
        for k in occurrence:
            if occurrence[k] >= threshold:
                new_occurence[k] = occurrence[k]
        return new_occurence
