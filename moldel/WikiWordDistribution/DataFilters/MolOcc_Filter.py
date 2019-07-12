from WikiWordDistribution.DataFilters.DataFilter import DataFilter

class MolOcc_Filter(DataFilter):
    def __init__(self, minimum_occ):
        self.minimum_occ = minimum_occ

    def filter(self, all_words, parsed_data, season):
        all_mols = [c for c in parsed_data if parsed_data[c]["season"] != season and parsed_data[c]["mol"]]
        important_words = set()
        for w in all_words:
            count = 0
            for c in all_mols:
                if w in parsed_data[c]["occ"]:
                    count += 1
            if count >= self.minimum_occ:
                important_words.add(w)
        return important_words