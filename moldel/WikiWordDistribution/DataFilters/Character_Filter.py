from WikiWordDistribution.DataFilters.DataFilter import DataFilter

class Character_Filter(DataFilter):
    """ The Character Filter select only the words that consists of only letters """

    def filter(self, all_words, parsed_data):
        important_words = set()
        for w in all_words:
            if w.isalpha():
                important_words.add(w)
        return important_words