from WikiWordDistribution.DataFilters.WordManipulator import WordManipulator

class UPO_Filter:
    """ The Upper Page Occurrence Filter (UPO Filter) only selects all words that occurs at most in n different pages
    (can be of different seasons) """

    def __init__(self, season_multiplier):
        self.season_multiplier = season_multiplier

    def filter(self, all_words, parsed_data):
        seasons = WordManipulator.get_seasons(parsed_data)
        threshold = len(seasons) * self.season_multiplier
        important_words = set()
        for word in all_words:
            count = 0
            for candidate in parsed_data:
                if word in parsed_data[candidate]["occ"].keys():
                    count += 1
            if count <= threshold:
                important_words.add(word)
        return important_words