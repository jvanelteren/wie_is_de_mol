import string
from WikiWordDistribution.DataParsers.Linker import linker

class DataParser:
    """ The Data Parser will read the Wiki Files and Linker for each candidate. And will parse
    the word occurences (occ), season number (season) and whether that person is the Mol or not (mol). """
    WIKI_FILES_FOLDER = "WikiWordDistribution/WikiFiles/"

    @staticmethod
    def parse():
        """ Will parse all data for all candidates """
        parsed_data = dict()
        for row in linker:
            parsed_data[row[0]] = {"occ": DataParser.wiki_file_parse(row[2]), "season": row[1], "mol": row[3]}
        return parsed_data

    @staticmethod
    def get_all_words(parsed_data):
        """ Extract all words from the parsed data """
        all_words = set()
        for candidate in parsed_data:
            candidate_words = parsed_data[candidate]["occ"].keys()
            all_words.update(candidate_words)
        return all_words

    @staticmethod
    def wiki_file_parse(file_name):
        """ Will parse the word occurrences of a single wiki file """
        file = open(DataParser.WIKI_FILES_FOLDER + file_name, "r", encoding="utf8")
        lines = file.readlines()
        word_occurrence = dict()
        for line in lines:
            filtered = DataParser.line_filter(line)
            split = filtered.split(" ")
            for word in split:
                pure_word = DataParser.word_filter(word)
                word_occurrence[pure_word] = word_occurrence.get(pure_word, 0) + 1
        return word_occurrence

    @staticmethod
    def line_filter(line):
        result = line.lower()
        for char in string.punctuation: # Remove symbols from text
            result = result.replace(char, ' ')
        result = result.strip("\n")
        result = result.strip("\t")
        return result

    @staticmethod
    def word_filter(word):
        result = word.strip("\n")
        result = result.strip("\t")
        return result
