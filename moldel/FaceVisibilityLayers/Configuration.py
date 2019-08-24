# This is the configuration file for the FaceTracker class. When you want to run the FaceTracker for a certain episode
# then you need to change these values appropriately. Do not commit the changes to this file!
from Candidates import *

# The identifier name is printed at the beginning and the end of the script. The identifier is not necessary to run the
# FaceTracker, but is useful if you run multiple instances of the FaceTracker. With the identifier name you can match
# the results with the right episode and season.
IDENTIFIER_NAME = "Season 17 - Episode 4"

# The location to the video file of the episode on which you want to run the FaceTracker. Only mp4 and mkv files have
# been tested with the FaceTracker, other video formats might not work. Make sure that only the episode is included in
# video. MolTalk and commercial breaks should not be contained in the video.
EPISODE_VIDEO_LOCATION = "/home/multifacio/WIDM/Seizoen 17/Videos/Episode 4.mp4"

FACE_IMAGE_FOLDER = "/home/multifacio/WIDM/Seizoen 17/Candidates/"

# The locations of the pictures for each candidate. Make sure that the quality of this pictures is good enough. This
# means that for each candidate the chin, eyes, mouth and nose are clearly visible. Also the edges of the face should
# be clear in the picture (if there is too much shadow over the face in the picture then it might have problems
# detecting the candidates). The candidate should look right into the camera (not to the left or the right). Moreover
# make sure that the picture only contains the head of the candidate (including the body of the candidate is unnecessary
# and having multiple faces in 1 picture might confuse the algorithm). Recommended is to pick a close-up of the
# candidate during the first episode or a moment when the candidate has a solo talk moment with a black background
# where he gives his opinion about something that happened. Never use a picture from the intro (because these are often
# low quality and candidates might look different during the intro then during the episode). If you cannot find a good
# quality picture then you can search for one on Google or check the second episode. When getting the results make sure
# that every candidate, except the candidates that dropped off, have been detected at least 75 times during every
# episode or has been detected at least 100 times during episode 2, 3 or 4. If this is not the case then you should
# pick a higher quality picture of the candidate. If this new picture still does not give higher detection values then
# you should pick the best picture and stick to the low detection values of the candidate.
FACE_IMAGE_NAMES = {Candidates.DIEDERIK_17: ["Diederik.jpeg", "Diederik2.jpeg"],
                    Candidates.IMANUELLE_17: ["Imanuelle.jpeg", "Imanuelle2.jpeg"],
                    Candidates.JEROEN_17: ["Jeroen.jpeg", "Jeroen2.jpeg"],
                    Candidates.JOCHEM_17: ["Jochem.jpeg", "Jochem2.jpeg"],
                    Candidates.ROOS_17: ["Roos.jpeg", "Roos2.jpeg"],
                    Candidates.SANNE_17: ["Sanne.jpeg", "Sanne2.jpeg"],
                    Candidates.SIGRID_17: ["Sigrid.jpeg", "Sigrid2.jpeg"],
                    Candidates.THOMAS_17: ["Thomas.jpeg", "Thomas2.jpeg"],
                    Candidates.VINCENT_17: ["Vincent.jpeg", "Vincent2.jpeg"],
                    Candidates.YVONNE_17: ["Yvonne.jpeg", "Yvonne2.jpeg"]}

# How many frames get skipped before analysing a frame (setting this value higher will make the script run faster,
# but makes the results less accurate). The general rule is to use 1 frame every 0.5 seconds. Therefore for video files
# with 25 frames per second it is recommended to use a FRAME_SKIP of 10 (which means a frame get analysed every 0.4
# second). For video files with 30 frames per second it is recommeded to use a FRAME_SKIP of 15.
FRAME_SKIP = 15