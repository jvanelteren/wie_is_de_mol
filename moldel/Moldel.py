from ExamDistribution.Data.Data import exam_data
from ExamDistribution.ExamDistribution import ExamDistribution

dis = ExamDistribution(exam_data, 10000, 3)
res = dis.compute_distribution(19, None)
print(res)