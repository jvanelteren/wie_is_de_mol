from WikiWordDistribution.DataFilters.DataFilter import DataFilter

class DWF_Filter(DataFilter):
    """ The Dutch Word Frequency Filter will remove the most frequent dutch words out of the list of words """
    FREQUENCY_FILE = "WikiWordDistribution/WikiFiles/dutch_word_frequency.txt"

    def __init__(self, best_of):
        file = open(self.FREQUENCY_FILE, "r", encoding="utf8")
        self.frequent_words = set()
        for i in range(best_of):
            line = file.readline()
            word = line.split(" ")[0]
            self.frequent_words.add(word)

    def filter(self, all_words, parsed_data, season):
        return all_words.difference(self.frequent_words)
