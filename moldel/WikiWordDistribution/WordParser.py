import string

class WordParser:
    WIKI_FILES_FOLDER = "WikiWordDistribution/WikiFiles/"

    @staticmethod
    def total_parse(linker):
        occurrences = dict()
        for row in linker:
            occurrences[row[0]] = WordParser.parse(row[2])
        return occurrences

    @staticmethod
    def parse(file_name):
        file = open(WordParser.WIKI_FILES_FOLDER + file_name, "r", encoding="utf8")
        lines = file.readlines()
        word_occurrence = dict()
        for line in lines:
            filtered = WordParser.line_filter(line)
            split = filtered.split(" ")
            for word in split:
                pure_word = WordParser.word_filter(word)
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
