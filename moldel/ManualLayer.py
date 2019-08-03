from DistributionTransformers.NormalizeTransformer import NormalizeTransformer
from Layer import Layer, DataError

class ManualLayer(Layer):
    """ The Manual Layer will set likelihoods to each candidate manually. """

    def __init__(self, likelihoods):
        """ Create a Manual Layer.
        Arguments:
            likelihoods (dict): A dictionary with as key the season (integer) and as value a dictionary with as
            key the candidate (enum) and as value the likelihood (float) """
        self.likelihoods = likelihoods

    def compute_distribution(self, season, episode):
        if season not in self.likelihoods:
            raise DataError("Manual Layer - Missing data season " + str(season))
        distribution = self.likelihoods[season]
        normalizer = NormalizeTransformer()
        return normalizer.transform_distribution(distribution)