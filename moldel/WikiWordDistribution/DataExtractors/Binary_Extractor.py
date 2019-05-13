from WikiWordDistribution.DataExtractors.DataExtractor import DataExtractor

class Binary_Extractor(DataExtractor):
    """ The binary extractor will translate every data to a vector with 1/0. A 1 in case if that word is contained in
    the candidates wiki page and a 0 in case it it not. """

    def __init__(self, bias):
        self.bias = bias # If bias is set to true then it appends an additional 1 to every vector

    def extract(self, important_words, parsed_data):
        numberic_input = dict()
        for candidate in parsed_data:
            bin_seq = []
            word_occurs = parsed_data[candidate]["occ"]
            for word in important_words:
                if word in word_occurs:
                    bin_seq.append(1)
                else:
                    bin_seq.append(0)
            if self.bias:
                bin_seq.append(1)
            numberic_input[candidate] = bin_seq
        return numberic_input