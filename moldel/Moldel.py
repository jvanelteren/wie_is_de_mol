from DistributionTransformers.RoundTransformer import RoundTransformer
from Printers.PiechartPrinter import PiechartPrinter
from WikiWordDistribution.DataExtractors.Binary_Extractor import Binary_Extractor
from WikiWordDistribution.DataFilters.MainFilter import MainFilter
from WikiWordDistribution.DataPredictors.StatisticsPredictor import StatisticsPredictor
from WikiWordDistribution.WikiWordDistribution import WikiWordDistribution

dis = WikiWordDistribution(Binary_Extractor(False), MainFilter(), StatisticsPredictor(), False)
res = dis.compute_distribution(16, None)
rounder = RoundTransformer()
res = rounder.transform_distribution(res, precision = 3)
printer = PiechartPrinter()
printer.do_print(res)