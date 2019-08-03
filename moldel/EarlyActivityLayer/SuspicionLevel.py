from aenum import Enum, NoAlias

class SuspicionLevel(Enum):
    _settings_ = NoAlias

    NOT_UNLIKELY = 1.0
    SLIGHTLY_UNLIKELY = 0.7
    UNLIKELY = 0.3
    VERY_UNLIKELY = 0.1