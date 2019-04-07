from DistributionTransformers.RoundTransformer import RoundTransformer
from ExamDistribution.Data.Data import exam_data
from ExamDistribution.ExamDistribution import ExamDistribution
from Printers.PiechartPrinter import PiechartPrinter

dis = ExamDistribution(exam_data, 10000)
res = dis.compute_distribution(17, None)
rounder = RoundTransformer()
res = rounder.transform_distribution(res, precision = 3)
printer = PiechartPrinter()
printer.do_print(res)