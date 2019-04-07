from ExamDistribution.Data.Data import exam_data
from ExamDistribution.ExamDistribution import ExamDistribution
from Printers.PiechartPrinter import PiechartPrinter

dis = ExamDistribution(exam_data, 10000, 3)
res = dis.compute_distribution(17, None)
printer = PiechartPrinter()
printer.do_print(res)