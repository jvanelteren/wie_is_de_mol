class DataExtractor:
    """ The Data Extractor interface """

    def extract(self, important_words, parsed_data):
        """ Extract numberic vectors out of the candidate data.
        Arguments:
            important_words (list): A sorted list of the most important words
            parsed_data (dict): A dictionary that contains the data for each candidate

        Returns: A dictionary with the numberic vectors for each candidate """
        pass
