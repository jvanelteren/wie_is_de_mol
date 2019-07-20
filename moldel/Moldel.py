from itertools import compress

from DistributionTransformers.CompositeTransformer import CompositeTransformer
from DistributionTransformers.RoundTransformer import RoundTransformer
from ExamDistribution.ExamDistribution import ExamDistribution
from Printers.PiechartPrinter import PiechartPrinter
from WikiWordDistribution.DataExtractors.Job_Extractor import Job_Extractor
from WikiWordDistribution.DataPredictors.Cossim_Predictor import Cossim_Predictor
from WikiWordDistribution.WikiWordDistribution import WikiWordDistribution

LAYERS = [ExamDistribution(10000),
          WikiWordDistribution(Job_Extractor(), Cossim_Predictor(10, 2, 0.02), False)]
PRINTER = PiechartPrinter()

# All frequently changed constants
EXAM_ACTIVATED = True
WIKIWORD_ACTIVATED = True
SEASON = 19
EPISODE = 8 # If episode is set to None then all known information is used

# Start of the code
include = [EXAM_ACTIVATED, WIKIWORD_ACTIVATED]
included_layers = list(compress(LAYERS, include))
results = []
for l in included_layers:
    results.append(l.compute_distribution(SEASON, EPISODE))
composite = CompositeTransformer()
results = composite.transform_distribution(results)
rounder = RoundTransformer()
results = rounder.transform_distribution(results, precision = 3)
PRINTER.do_print(results)