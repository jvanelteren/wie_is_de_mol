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

# All frequently changed constants. The episode value is inclusive, meaning that also the result of the test of that
# episode is also included as data. If you set episode to 0 as value then no episodes are used as data at all. If you
# set episode to None then all known information about that season is used.
EXAM_ACTIVATED = True
WIKIWORD_ACTIVATED = True
SEASON = 16
EPISODE = None

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