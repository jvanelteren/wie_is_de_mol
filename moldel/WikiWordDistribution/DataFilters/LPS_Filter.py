from WikiWordDistribution.DataFilters.WordManipulator import WordManipulator
from WikiWordDistribution.DataFilters.DataFilter import DataFilter

class LPS_Filter(DataFilter):
    """ The Lower Page Season Filter (LPS Filter) filters all words by taking only the words that appears at least in
    n wiki pages during every season. """

    def __init__(self, threshold):
        self.threshold = threshold

    def filter(self, all_words, parsed_data, season):
        important_words = all_words
        seasons = WordManipulator.get_seasons(parsed_data)
        for s in seasons:
            season_words = set()
            for w in important_words:
                if WordManipulator.get_season_page_occurrence_word(w, s, parsed_data) >= self.threshold:
                    season_words.add(w)
            important_words = season_words
        return important_words