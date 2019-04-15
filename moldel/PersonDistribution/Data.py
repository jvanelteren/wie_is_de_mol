from Candidates import *
from PersonDistribution.Structure import *

# The Personal data about every candidate that participated in 'Wie is de Mol' starting from the season with BN'ers
# (which is season 5). Every candidate is represented by a data tuple containing the following data
# 0: Name of the candidate, which is just a Candidate enum value
# 1: Season number in which the candidate participated, starting from season 5
# 2: Whether that person was the 'Mol' or not. True means he/she was the 'Mol', false means he/she was not the 'Mol'
# 3: Gender of the candidate. True means that the candidate was a Male. False means that the candidate was a Female.
# 4: Age of the candidate in years. Meaning the age at the time the first episode is broadcasted, if that episode was
# that candidates birthday then he is considered 1 year older.
# 5: List of jobs of the candidate, including previous jobs of the candidate
# 6: Whether the candidate studied at a 'Theater School' or 'Toneel School'. True means he/she did,
# false means he/she did not. (Also if the candidate did not finish his study it is still counted)
# 7: The google trends score of the candidate: https://trends.google.nl. It is the average score of that candidate
# 1 year in advance till the first episode broadcast date of Wie is de Mol. You obtain this score by comparing a
# candidate with itself.

person_data_map = {"candidate": 0, "season": 1, "mol": 2, "gender": 3, "age": 4, "jobs": 5, "actor-school": 6,
                   "popularity": 7}

person_data = [
    # Candidates of season 19
    (Candidates.EVI_19, 19, False, False, 40, {Jobs.TV_ACTEUR, Jobs.ZANGER, Jobs.MODEL, Jobs.TV_PRESENTATOR,
    Jobs.FESTIVAL_PRESENTATOR, Jobs.RADIO_PRESENTATOR, Jobs.STEM_ACTEUR}, False, 15),
    (Candidates.EVELIEN_19, 19, False, False, 44, {Jobs.TV_PRESENTATOR, Jobs.RADIO_PRODUCER, Jobs.RADIO_PRESENTATOR},
     False, 8),
    (Candidates.JAMIE_19, 19, False, True, 28, {Jobs.TV_PRESENTATOR}, False, 5),
    (Candidates.MEREL_19, 19, True, False, 39, {Jobs.TV_PRESENTATOR}, False, 11),
    (Candidates.NIELS_19, 19, False, True, 29, {Jobs.ZANGER, Jobs.SONGWRITER, Jobs.INSTRUMENTIST}, False, 7),
    (Candidates.NIKKIE_19, 19, False, False, 24, {Jobs.MODEL, Jobs.YOUTUBER}, False, 9),
    (Candidates.RICK_PAUL_19, 19, False, True, 37, {Jobs.TV_ACTEUR}, False, 5),
    (Candidates.ROBERT_19, 19, False, True, 57, {Jobs.KOK, Jobs.TV_PRESENTATOR}, False, 16),
    (Candidates.SARAH_19, 19, False, False, 32, {Jobs.TV_ACTEUR, Jobs.ZANGER}, True, 6),
    (Candidates.SINAN_19, 19, False, True, 41, {Jobs.JOURNALIST, Jobs.TV_PRODUCER}, False, 9),

    # Candidates of season 18
    (Candidates.BELLA_18, 18, False, False, 27, {Jobs.ZANGER, Jobs.DJ}, False, 5),
    (Candidates.EMILIO_18, 18, False, True, 36, {Jobs.CABARETIER, Jobs.STEM_ACTEUR, Jobs.TV_PRODUCER, Jobs.TV_ACTEUR},
     False, 5),
    (Candidates.JAN_18, 18, True, True, 32, {Jobs.TV_PRESENTATOR, Jobs.ZANGER}, True, 11),
    (Candidates.JEAN_MARC_18, 18, False, True, 50, {Jobs.ILLUSTRATOR, Jobs.TV_PRESENTATOR, Jobs.SCHRIJVER}, False, 4),
    (Candidates.LOES_18, 18, False, False, 36, {Jobs.TV_ACTEUR, Jobs.TONEEL_ACTEUR, Jobs.ZANGER}, True, 12),
    (Candidates.OLCAY_18, 18, False, False, 37, {Jobs.MODEL, Jobs.TV_PRESENTATOR}, False, 18),
    (Candidates.RON_18, 18, False, True, 54, {Jobs.TV_PRESENTATOR, Jobs.CABARETIER, Jobs.TV_ACTEUR, Jobs.STEM_ACTEUR,
    Jobs.TONEEL_PRODUCER, Jobs.TONEEL_ACTEUR, Jobs.ZANGER}, True, 9),
    (Candidates.RUBEN_18, 18, False, True, 35, {Jobs.ZANGER, Jobs.INSTRUMENTIST, Jobs.RADIO_PRESENTATOR}, False, 4),
    (Candidates.SIMONE_18, 18, False, False, 46, {Jobs.TV_PRESENTATOR, Jobs.JOURNALIST, Jobs.RADIO_PRESENTATOR,
    Jobs.STEM_ACTEUR}, False, 15),
    (Candidates.STINE_18, 18, False, False, 45, {Jobs.SCHRIJVER}, False, 9),

    # Candidates of season 17
    (Candidates.DIEDERIK_17, 17, False, True, 32, {Jobs.TV_PRESENTATOR, Jobs.TV_PRODUCER, Jobs.JOURNALIST,
    Jobs.SCHRIJVER}, False, 12),
    (Candidates.IMANUELLE_17, 17, False, False, 31, {Jobs.TONEEL_ACTEUR, Jobs.TV_ACTEUR}, False, 6),
    (Candidates.JEROEN_17, 17, False, True, 42, {Jobs.RADIO_PRESENTATOR, Jobs.STEM_ACTEUR, Jobs.DJ, Jobs.TV_PRESENTATOR,
    Jobs.TV_PRODUCER, Jobs.SCHRIJVER}, False, 7),
    (Candidates.JOCHEM_17, 17, False, True, 53, {Jobs.TV_PRESENTATOR, Jobs.ZANGER, Jobs.SCHRIJVER, Jobs.TV_ACTEUR},
     False, 21),
    (Candidates.ROOS_17, 17, False, False, 41, {Jobs.SCHRIJVER, Jobs.JOURNALIST, Jobs.TV_ACTEUR}, False, 13),
    (Candidates.SANNE_17, 17, False, False, 45, {Jobs.CABARETIER, Jobs.TV_PRESENTATOR, Jobs.TV_ACTEUR}, False, 10),
    (Candidates.SIGRID_17, 17, False, False, 23, {Jobs.TV_ACTEUR}, True, 10),
    (Candidates.THOMAS_17, 17, True, True, 32, {Jobs.TONEEL_ACTEUR, Jobs.TV_ACTEUR}, True, 4),
    (Candidates.VINCENT_17, 17, False, True, 32, {Jobs.DANSER}, False, 3),
    (Candidates.YVONNE_17, 17, False, False, 30, {Jobs.TV_ACTEUR, Jobs.ZANGER, Jobs.TONEEL_ACTEUR, Jobs.STEM_ACTEUR,
    Jobs.YOUTUBER, Jobs.MODEL}, False, 9),

    # Candidates of season 16
    (Candidates.AIREN_16, 16, False, False, 30, {Jobs.TV_PRESENTATOR}, False, 10),
    (Candidates.ANNEMIEKE_16, 16, False, False, 36, {Jobs.RADIO_PRESENTATOR, Jobs.DJ}, False, 6),
    (Candidates.CECILE_16, 16, False, False, 45, {Jobs.JOURNALIST, Jobs.SCHRIJVER}, False, 4),
    (Candidates.ELLIE_16, 16, False, False, 49, {Jobs.POLITIE}, False, 6),
    (Candidates.KLAAS_16, 16, True, True, 39, {Jobs.RADIO_PRESENTATOR, Jobs.DJ, Jobs.RADIO_PRODUCER,
    Jobs.TV_PRESENTATOR}, False, 8),
    (Candidates.MARJOLEIN_16, 16, False, False, 53, {Jobs.TV_ACTEUR, Jobs.ZANGER, Jobs.TV_PRESENTATOR,
    Jobs.RADIO_PRESENTATOR}, True, 20),
    (Candidates.REMY_16, 16, False, True, 26, {Jobs.INSTRUMENTIST}, False, 8),
    (Candidates.ROP_16, 16, False, True, 41, {Jobs.TV_ACTEUR, Jobs.TONEEL_ACTEUR, Jobs.STEM_ACTEUR, Jobs.CABARETIER},
     True, 7),
    (Candidates.TAEKE_16, 16, False, True, 35, {Jobs.TV_PRESENTATOR, Jobs.SPORTER}, False, 6),
    (Candidates.TIM_16, 16, False, True, 27, {Jobs.JOURNALIST, Jobs.TV_PRESENTATOR, Jobs.SCHRIJVER}, False, 13),

    # Candidates of season 15
    (Candidates.AJOUAD_15, 15, False, True, 27, {Jobs.RADIO_PRESENTATOR, Jobs.TV_PRESENTATOR}, False, 6),
    (Candidates.CAROLINA_15, 15, False, False, 34, {Jobs.ZANGER, Jobs.TV_PRESENTATOR, Jobs.TONEEL_ACTEUR,
    Jobs.TV_ACTEUR, Jobs.STEM_ACTEUR}, False, 14),
    (Candidates.CHRIS_15, 15, False, True, 43, {Jobs.TV_ACTEUR, Jobs.TV_PRESENTATOR, Jobs.ZANGER, Jobs.INSTRUMENTIST},
     False, 10),
    (Candidates.EVELIEN_15, 15, False, False, 33, {Jobs.RADIO_PRODUCER, Jobs.JOURNALIST, Jobs.RADIO_PRESENTATOR,
    Jobs.TV_PRODUCER, Jobs.TV_PRESENTATOR}, False, 10),
    (Candidates.MARGRIET_15, 15, True, False, 44, {Jobs.JOURNALIST, Jobs.TV_PRESENTATOR, Jobs.RADIO_PRESENTATOR,
    Jobs.SCHRIJVER}, False, 7),
    (Candidates.MARLIJN_15, 15, False, False, 31, {Jobs.TONEEL_ACTEUR, Jobs.ZANGER, Jobs.TV_ACTEUR}, True, 13),
    (Candidates.MARTINE_15, 15, False, False, 44, {Jobs.TONEEL_ACTEUR, Jobs.CABARETIER, Jobs.TV_ACTEUR,
    Jobs.TV_PRESENTATOR, Jobs.STEM_ACTEUR}, True, 10),
    (Candidates.PIETER_15, 15, False, True, 30, {Jobs.CABARETIER, Jobs.SCHRIJVER}, False, 18),
    (Candidates.RIK_15, 15, False, True, 43, {Jobs.RADIO_PRESENTATOR, Jobs.TV_PRESENTATOR, Jobs.JOURNALIST,
    Jobs.TV_ACTEUR, Jobs.STEM_ACTEUR}, False, 7),
    (Candidates.VIKTOR_15, 15, False, True, 43, {Jobs.JOURNALIST, Jobs.TV_PRESENTATOR}, False, 12),

    # Candidates of season 14
    (Candidates.AAF_14, 14, False, False, 38, {Jobs.JOURNALIST, Jobs.SCHRIJVER}, False, 8),
    (Candidates.DAPHNE_14, 14, False, False, 40, {Jobs.TV_PRESENTATOR, Jobs.TV_ACTEUR, Jobs.RADIO_PRESENTATOR}, True,
     14),
    (Candidates.FREEK_14, 14, False, True, 27, {Jobs.TONEEL_ACTEUR, Jobs.ZANGER}, False, 11),
    (Candidates.JAN_WILLEM_14, 14, False, True, 36, {Jobs.RADIO_PRESENTATOR, Jobs.STEM_ACTEUR, Jobs.JOURNALIST}, False,
     4),
    (Candidates.JENNIFER_14, 14, False, False, 33, {Jobs.TV_ACTEUR, Jobs.TV_PRESENTATOR}, False, 17),
    (Candidates.MAURICE_14, 14, False, True, 27, {Jobs.TV_PRODUCER, Jobs.TV_PRESENTATOR, Jobs.RADIO_PRESENTATOR}, False,
     5),
    (Candidates.OWEN_14, 14, False, True, 46, {Jobs.CABARETIER, Jobs.RADIO_PRODUCER, Jobs.TV_PRODUCER, Jobs.TV_ACTEUR,
    Jobs.TONEEL_ACTEUR, Jobs.TV_PRESENTATOR}, False, 5),
    (Candidates.SOFIE_14, 14, False, False, 33, {Jobs.CABARETIER, Jobs.TV_PRESENTATOR, Jobs.RADIO_PRESENTATOR,
    Jobs.TV_ACTEUR}, False, 15),
    (Candidates.SUSAN_14, 14, True, False, 48, {Jobs.TV_ACTEUR, Jobs.TONEEL_ACTEUR}, True, 12),
    (Candidates.TYGO_14, 14, False, True, 39, {Jobs.TV_ACTEUR, Jobs.STEM_ACTEUR}, False, 11),

    # Candidates of season 13
    (Candidates.CAROLIEN_13, 13, False, False, 29, {Jobs.CABARETIER, Jobs.JOURNALIST, Jobs.TONEEL_PRODUCER}, True, 7),
    (Candidates.DANIEL_13, 13, False, True, 43, {Jobs.TV_ACTEUR, Jobs.ZANGER, Jobs.TONEEL_ACTEUR}, True, 9),
    (Candidates.EWOUT_13, 13, False, True, 27, {Jobs.TV_PRODUCER, Jobs.TV_ACTEUR, Jobs.ZANGER, Jobs.TV_PRESENTATOR,
    Jobs.STEM_ACTEUR}, True, 10),
    (Candidates.JANINE_13, 13, False, False, 36, {Jobs.ZANGER, Jobs.TV_PRESENTATOR, Jobs.TV_PRODUCER,
    Jobs.RADIO_PRESENTATOR}, False, 5),
    (Candidates.JOEP_13, 13, False, True, 52, {Jobs.CABARETIER, Jobs.TV_PRODUCER, Jobs.TONEEL_ACTEUR, Jobs.TV_ACTEUR,
    Jobs.TV_PRESENTATOR, Jobs.ZANGER, Jobs.INSTRUMENTIST, Jobs.SCHRIJVER}, False, 20),
    (Candidates.KEES_13, 13, True, True, 30, {Jobs.TV_PRODUCER, Jobs.RADIO_PRESENTATOR, Jobs.TV_PRESENTATOR,
    Jobs.TV_ACTEUR}, False, 10),
    (Candidates.PAULIEN_13, 13, False, False, 36, {Jobs.CABARETIER, Jobs.JOURNALIST, Jobs.SCHRIJVER}, False, 16),
    (Candidates.TANIA_13, 13, False, False, 36, {Jobs.ZANGER}, False, 12),
    (Candidates.TIM_13, 13, False, True, 31, {Jobs.TV_ACTEUR, Jobs.TV_PRESENTATOR}, False, 9),
    (Candidates.ZARAYDA_13, 13, False, False, 30, {Jobs.TONEEL_ACTEUR, Jobs.RADIO_PRESENTATOR, Jobs.TV_PRESENTATOR,
    Jobs.SCHRIJVER}, False, 7)
]

def data_from_row(row, var):
    index = person_data_map.get(var, None)
    return row[index]