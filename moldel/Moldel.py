from DistributionTransformers.RoundTransformer import RoundTransformer
from Printers.PiechartPrinter import PiechartPrinter
from WikiWordDistribution.DataExtractors.Binary_Extractor import Binary_Extractor
from WikiWordDistribution.DataFilters.MainFilter import MainFilter
from WikiWordDistribution.DataPredictors.SpecialLinearRegression import SpecialLinearRegression
from WikiWordDistribution.WikiWordDistribution import WikiWordDistribution

dis = WikiWordDistribution(Binary_Extractor(True), MainFilter(), SpecialLinearRegression(10.0, 0.05, True, 7, 100.0),
                           False)
res = dis.compute_distribution(19, None)
rounder = RoundTransformer()
res = rounder.transform_distribution(res, precision = 3)
printer = PiechartPrinter()
printer.do_print(res)