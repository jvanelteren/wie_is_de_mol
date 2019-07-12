from WikiWordDistribution.DataFilters.DataFilter import DataFilter

class CandidateName_Filter(DataFilter):
    """ The Candidate Name Filter removes words that contain any candidate name """

    def filter(self, all_words, parsed_data, season):
        names = set() # All candidate names
        for candidate in parsed_data:
            names.add(candidate.value.lower())

        important_words = set()
        for w in all_words:
            if not any(n in w for n in names):
                important_words.add(w)
        return important_words