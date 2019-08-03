from Candidates import *
from EarlyActivityLayer.SuspicionLevel import *

# Suspicion Levels must be determined manually by looking for early activity. "Wie is de Mol" is often recorded during
# the month May and June, so during these months you have to check for activity. The recording of "Wie is de Mol" take
# 18 days in total.

# You can use the social media analysis of Jaap van Zessen to fill in these values. For example for season 19 this can
# be found at the following url: https://www.ad.nl/show/de-social-media-analyse-van-wie-is-de-mol-2019~ac68622f/
# If this is not possible for certain seasons then you should analyse Facebook, Twitter, Youtube, Instagram, etc
# with a tool and determine if that candidate was active.

# Suspicion Levels are quite subjective, but these are the guidelines for the Suspicion Levels:
# -NOT_UNLIKELY: Only if you cannot find any form of activity during the recording period.
# -SLIGHTLY_UNLIKELY: If the candidate has posted more tweets or facebook posts than before. Or had a phone call during
# night time (of the recorded country). Etcetera...
# -UNLIKELY: If the candidate has posted many tweets or facebook post. Has uploaded some instagram pictures. If the
# candidate has posted some tweets or facebook posts with pictures. If the candidate was present during a dutch radio
# recording or had multiple phone call during night time (of the recorded country) or a combination of these things.
# Or if the candidate has uploaded a some short video. Etcetera...
# -VERY_UNLIKELY: If the candidate has uploaded a long video. Or if the candidate has some picture with a dutch
# background. If the candidate participated in another dutch television show/serie. Or if there is any clear evidence
# that the candidate was present in the Netherland during the recording. Or if the candidate carries out his/her
# current job. Or if the candidate was present during multiple dutch radio recording. Extremely many tweets or facebook
# posts or a combination is not enough the be classified in this category.

# Closer to the end date of the recording will be considered closer to NOT_UNLIKELY. Declaration of witnesses will not
# be used to determine suspicion levels and also rumours of suspicions of any kind will also not be used to determine
# suspicion levels. If there is no other form of activity then the candidate has to be classified as NOT_UNLIKELY.

# Only based on https://www.ad.nl/show/de-social-media-analyse-van-wie-is-de-mol-2019~ac68622f/
SEASON19 = {Candidates.ROBERT_19: SuspicionLevel.UNLIKELY, Candidates.SINAN_19: SuspicionLevel.UNLIKELY,
            Candidates.EVI_19: SuspicionLevel.VERY_UNLIKELY, Candidates.NIKKIE_19: SuspicionLevel.UNLIKELY,
            Candidates.EVELIEN_19: SuspicionLevel.NOT_UNLIKELY, Candidates.JAMIE_19: SuspicionLevel.NOT_UNLIKELY,
            Candidates.MEREL_19: SuspicionLevel.NOT_UNLIKELY, Candidates.NIELS_19: SuspicionLevel.NOT_UNLIKELY,
            Candidates.RICK_PAUL_19: SuspicionLevel.NOT_UNLIKELY, Candidates.SARAH_19: SuspicionLevel.NOT_UNLIKELY}

# Only based on https://www.ad.nl/show/social-media-analyse-wie-is-de-mol-2018~ac1d7cf8/
SEASON18 = {Candidates.BELLA_18: SuspicionLevel.NOT_UNLIKELY, Candidates.EMILIO_18: SuspicionLevel.NOT_UNLIKELY,
            Candidates.JAN_18: SuspicionLevel.NOT_UNLIKELY, Candidates.JEAN_MARC_18: SuspicionLevel.NOT_UNLIKELY,
            Candidates.LOES_18: SuspicionLevel.NOT_UNLIKELY, Candidates.OLCAY_18: SuspicionLevel.NOT_UNLIKELY,
            Candidates.RON_18: SuspicionLevel.NOT_UNLIKELY, Candidates.RUBEN_18: SuspicionLevel.NOT_UNLIKELY,
            Candidates.SIMONE_18: SuspicionLevel.NOT_UNLIKELY, Candidates.STINE_18: SuspicionLevel.NOT_UNLIKELY}

# Only based on https://www.ad.nl/tv-en-radio/dit-zijn-de-afvallers-van-wie-is-de-mol-2017~a995a64a/
SEASON17 = {Candidates.ROOS_17: SuspicionLevel.UNLIKELY, Candidates.SIGRID_17: SuspicionLevel.UNLIKELY,
            Candidates.VINCENT_17: SuspicionLevel.SLIGHTLY_UNLIKELY, Candidates.DIEDERIK_17: SuspicionLevel.NOT_UNLIKELY,
            Candidates.IMANUELLE_17: SuspicionLevel.NOT_UNLIKELY, Candidates.JEROEN_17: SuspicionLevel.NOT_UNLIKELY,
            Candidates.JOCHEM_17: SuspicionLevel.NOT_UNLIKELY, Candidates.SANNE_17: SuspicionLevel.NOT_UNLIKELY,
            Candidates.THOMAS_17: SuspicionLevel.NOT_UNLIKELY, Candidates.YVONNE_17: SuspicionLevel.NOT_UNLIKELY}

# Only based on http://www.jaapvanzessen.nl/social-media-analist-blogs/nieuwe-wie-is-de-mol-social-media-analyse-live/
SEASON16 = {Candidates.AIREN_16: SuspicionLevel.UNLIKELY, Candidates.TAEKE_16: SuspicionLevel.UNLIKELY,
            Candidates.ELLIE_16: SuspicionLevel.SLIGHTLY_UNLIKELY, Candidates.MARJOLEIN_16: SuspicionLevel.SLIGHTLY_UNLIKELY,
            Candidates.CECILE_16: SuspicionLevel.SLIGHTLY_UNLIKELY, Candidates.ANNEMIEKE_16: SuspicionLevel.NOT_UNLIKELY,
            Candidates.ROP_16: SuspicionLevel.NOT_UNLIKELY, Candidates.KLAAS_16: SuspicionLevel.NOT_UNLIKELY,
            Candidates.TIM_16: SuspicionLevel.NOT_UNLIKELY, Candidates.REMY_16: SuspicionLevel.NOT_UNLIKELY}

# Only based on https://www.marketingfacts.nl/berichten/social-media-voorspelt-ook-afvaller-wie-is-de-mol-door-monitoring
SEASON15 = {Candidates.CAROLINA_15: SuspicionLevel.SLIGHTLY_UNLIKELY, Candidates.EVELIEN_15: SuspicionLevel.SLIGHTLY_UNLIKELY,
            Candidates.AJOUAD_15: SuspicionLevel.NOT_UNLIKELY, Candidates.CHRIS_15: SuspicionLevel.NOT_UNLIKELY,
            Candidates.MARGRIET_15: SuspicionLevel.NOT_UNLIKELY, Candidates.MARLIJN_15: SuspicionLevel.NOT_UNLIKELY,
            Candidates.MARTINE_15: SuspicionLevel.NOT_UNLIKELY, Candidates.PIETER_15: SuspicionLevel.NOT_UNLIKELY,
            Candidates.RIK_15: SuspicionLevel.NOT_UNLIKELY, Candidates.VIKTOR_15: SuspicionLevel.NOT_UNLIKELY}

# Only based on http://www.jaapvanzessen.nl/social-media-analist-blogs/wie-de-mol-deelnemer-laten-sporen-achter-op-social-media/
SEASON14 = {Candidates.MAURICE_14: SuspicionLevel.UNLIKELY, Candidates.FREEK_14: SuspicionLevel.SLIGHTLY_UNLIKELY,
            Candidates.TYGO_14: SuspicionLevel.UNLIKELY, Candidates.AAF_14: SuspicionLevel.NOT_UNLIKELY,
            Candidates.DAPHNE_14: SuspicionLevel.NOT_UNLIKELY, Candidates.JAN_WILLEM_14: SuspicionLevel.NOT_UNLIKELY,
            Candidates.JENNIFER_14: SuspicionLevel.NOT_UNLIKELY, Candidates.OWEN_14: SuspicionLevel.NOT_UNLIKELY,
            Candidates.SOFIE_14: SuspicionLevel.NOT_UNLIKELY, Candidates.SUSAN_14: SuspicionLevel.NOT_UNLIKELY}

SUSPICION_DATA = {19: SEASON19, 18: SEASON18, 17: SEASON17, 16: SEASON16, 15: SEASON15, 14: SEASON14}