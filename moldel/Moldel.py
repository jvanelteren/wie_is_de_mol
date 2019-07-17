from DistributionTransformers.CompositeTransformer import CompositeTransformer
from DistributionTransformers.RoundTransformer import RoundTransformer
from ExamDistribution.Data.Data import exam_data
from ExamDistribution.ExamDistribution import ExamDistribution
from Printers.PiechartPrinter import PiechartPrinter

from WikiWordDistribution.DataExtractors.Job_Extractor import Job_Extractor
from WikiWordDistribution.DataPredictors.Cossim_Predictor import Cossim_Predictor
from WikiWordDistribution.WikiWordDistribution import WikiWordDistribution

dis = WikiWordDistribution(Job_Extractor(), Cossim_Predictor(10, 2, 0.02), False)
res = dis.compute_distribution(10, 2)
# dis2 = ExamDistribution(exam_data, 10000)
# res2 = dis2.compute_distribution(19, 2)
# composite = CompositeTransformer()
# res = composite.transform_distribution([res, res2])
rounder = RoundTransformer()
res = rounder.transform_distribution(res, precision = 3)
printer = PiechartPrinter()
printer.do_print(res)