from WikiWordDistribution.DataFilters.CandidateName_Filter import CandidateName_Filter
from WikiWordDistribution.DataFilters.Character_Filter import Character_Filter
from WikiWordDistribution.DataFilters.Composite_Filter import Composite_Filter
from WikiWordDistribution.DataFilters.DWF_Filter import DWF_Filter
from WikiWordDistribution.DataFilters.LPO_Filter import LPO_Filter
from WikiWordDistribution.DataFilters.MolOcc_Filter import MolOcc_Filter
from WikiWordDistribution.DataFilters.UPO_Filter import UPO_Filter

class MainFilter(Composite_Filter):
    def __init__(self):
        super().__init__()
        self.add(Character_Filter())
        self.add(CandidateName_Filter())
        self.add(DWF_Filter(500))
        self.add(LPO_Filter(1.5))
        self.add(UPO_Filter(7.0))
        self.add(MolOcc_Filter(3))