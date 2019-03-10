class DataError(Exception):
    pass

# Interface used to compute probabilities that someone is the 'Mol'
class ProbabilityDistribution:
    def compute_distribution(self, season, episode):
        """ Compute the probability distribution of each candidate that it is the 'Mol'
            Args:
                season (int): The season number for which a probability distribution is computed (19 november 1999 is
                considered as season 1)
                episode (int): Until which episode the data is used, including this entire episode. None means that all
                episodes known so far are used. 0 means that none data of the episodes is used at all.

            Returns:
                dict: A dictionary that contains the probabilities for each candidate that it is the 'Mol'

            Raises:
                DataError: When the model does not have sufficient enough data to compute a distribution
        """
        pass