from WikiWordDistribution.DataParsers.DataParser import DataParser
from WikiWordDistribution.WordFilters.Composite_Filter import Composite_Filter
from WikiWordDistribution.WordFilters.LPO_Filter import LPO_Filter
from WikiWordDistribution.WordFilters.TO_Printer import TO_Printer
from WikiWordDistribution.WordFilters.UPS_Filter import UPS_Filter

class Main:
    """ This is not dead code, but is used to manually extract words yourself for the Jobs. """
    def get_words(self, filter, printer):
        parsed_data = DataParser.parse()
        all_words = DataParser.get_all_words(parsed_data)
        important_words = list(filter.filter(all_words, parsed_data))
        printer.print(important_words, parsed_data)

filter = Composite_Filter()
filter.add(LPO_Filter(0.2))
filter.add(UPS_Filter(9))
main = Main()
main.get_words(filter, TO_Printer(True))