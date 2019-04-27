import operator

from WikiWordDistribution.WordOccurenceTransformation import WordOccurenceTransformation

class ImportanceFilter:
    def __init__(self):
        self.important_words = set()
        self.season_occurrences = dict()

    def compute(self, linker, occurrences, threshold):
        seasons = self.get_seasons(linker)
        candidates_per_season = self.get_candidates_per_season(seasons, linker)
        self.important_words = self.get_important_words(seasons, candidates_per_season, occurrences, threshold)

    def get_seasons(self, linker):
        seasons = set()
        for row in linker:
            seasons.add(row[1])
        return seasons

    def get_candidates_per_season(self, seasons, linker):
        candidates_per_season = dict()
        for s in seasons:
            candidates = [row[0] for row in linker if row[1] == s]
            candidates_per_season[s] = candidates
        return candidates_per_season

    def get_important_words(self, seasons, candidates_per_season, occurrences, threshold):
        listed_occurrences = []
        for s in seasons:
            self.season_occurrences[s] = self.get_season_occurrence(candidates_per_season[s], occurrences)
            listed_occurrences.append(self.season_occurrences[s])
        total_occurrence = WordOccurenceTransformation.min(listed_occurrences)
        return WordOccurenceTransformation.filter(total_occurrence, threshold).keys()

    def get_season_occurrence(self, candidates, occurrences):
        candidate_occurences = []
        for c in candidates:
            candidate_occurences.append(occurrences[c])
        return WordOccurenceTransformation.add(candidate_occurences)