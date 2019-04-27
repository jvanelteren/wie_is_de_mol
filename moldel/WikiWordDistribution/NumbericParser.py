class NumbericParser:
    @staticmethod
    def parse(linker, occurrences, season_occurrences, important_words):
        numberic_data = dict()
        for c in occurrences:
            numberic_data[c] = NumbericParser.candidate_parse(c, linker, occurrences, season_occurrences,
                                                              important_words)
        return numberic_data

    @staticmethod
    def candidate_parse(candidate, linker, occurrences, season_occurrences, important_words):
        ind_numberic_data = []
        season = NumbericParser.get_season_candidate(candidate, linker)
        occur = occurrences[candidate]
        for words in important_words:
            part = occur.get(words, 0) / season_occurrences[season][words]
            ind_numberic_data.append(part)
        return ind_numberic_data

    @staticmethod
    def get_season_candidate(candidate, linker):
        for row in linker:
            if row[0] == candidate:
                return row[1]