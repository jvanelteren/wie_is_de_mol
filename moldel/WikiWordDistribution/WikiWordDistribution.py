from DistributionTransformers.NormalizeTransformer import NormalizeTransformer
from DistributionTransformers.ReverseTransformer import ReverseTransformer
from ProbabilityDistribution import ProbabilityDistribution
from WikiWordDistribution.DataExtractors.Output_Extractor import Output_Extractor
from WikiWordDistribution.DataParsers.DataParser import DataParser
from WikiWordDistribution.DataSelectors.Normal_Train_Selector import Normal_Train_Selector
from WikiWordDistribution.DataSelectors.Predict_Selector import Predict_Selector
from WikiWordDistribution.DataSelectors.Strict_Train_Selector import Strict_Train_Selector

class WikiWordDistribution(ProbabilityDistribution):
    def __init__(self, input_extractor, filter, predicter, strict):
        self.input_extractor = input_extractor
        self.filter = filter
        self.predicter = predicter
        if strict:
            self.train_selector = Strict_Train_Selector()
        else:
            self.train_selector = Normal_Train_Selector()

    def compute_distribution(self, season, episode):
        parsed_data = DataParser.parse()
        all_words = DataParser.get_all_words(parsed_data)
        important_words = list(self.filter.filter(all_words, parsed_data))
        important_words.sort()
        numberic_input = self.input_extractor.extract(important_words, parsed_data)
        numberic_output = Output_Extractor().extract(important_words, parsed_data)
        train_input = self.train_selector.select(numberic_input, parsed_data, season)
        train_output = self.train_selector.select(numberic_output, parsed_data, season)
        self.predicter.train(train_input, train_output)
        predict_input = Predict_Selector().select(numberic_input, parsed_data, season)
        predict_output = self.predicter.predict(predict_input)
        normalizer = NormalizeTransformer()
        reverser = ReverseTransformer()
        return reverser.transform_distribution(normalizer.transform_distribution(predict_output))