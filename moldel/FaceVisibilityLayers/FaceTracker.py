from FaceVisibilityLayers.Configuration import FACE_IMAGE_LOCATIONS, EPISODE_VIDEO_LOCATION
import face_recognition as fr
import cv2

class FaceTracker:
    """ The FaceTracker determines how often a face of a candidate is visible during an episode. This code is based
    on the project of mattijn: https://github.com/mattijn/widm """

    # How many frames get skipped before analysing a frame (setting this value higher will make the script run faster,
    # but makes the results less accurate)
    FRAME_SKIP = 15

    # Setting the tolerance higher means that faces get detected more earlier
    TOLERANCE = 0.5

    def track_faces(self):
        numbered_candidates = enumerate(list(FACE_IMAGE_LOCATIONS.keys()))
        score = dict()
        for _, candidate in numbered_candidates:
            score[candidate] = 0

        # Load the face images of all candidates
        known_faces = []
        for _, candidate in numbered_candidates:
            image = fr.load_image_file(FACE_IMAGE_LOCATIONS[candidate])
            known_faces.append(fr.face_encodings(image)[0])

        # Read the frames of the episode
        video_capture = cv2.VideoCapture(EPISODE_VIDEO_LOCATION)
        frame_count = 0
        while video_capture.isOpened():
            continues, frame = video_capture.read()
            if not continues: # If this is the last frame then stop
                video_capture.release()
                break
            frame_count += 1
            if frame_count % self.FRAME_SKIP == 0: # Only analyse every FRAME_SKIP frame
                # Find all faces in this frame
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                rgb_frame = frame[:, :, ::-1]
                face_locations = fr.face_locations(rgb_frame)
                found_faces = fr.face_encodings(rgb_frame, face_locations)
                for ff in found_faces:
                    # Check which candidate face matches with the founded face
                    match = fr.compare_faces(known_faces, ff, tolerance = self.TOLERANCE)
                    for i, candidate in numbered_candidates:
                        if match[i]:
                            score[candidate] += 1
                            break

        # Adjust and print the score
        score_sum = sum(score.values())
        for candidate, score in score.items():
            score[candidate] = score / score_sum
        print(score)

ft = FaceTracker()
ft.track_faces()
