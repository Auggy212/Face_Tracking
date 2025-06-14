import cv2
import mediapipe as mp
import numpy as np

mp_face = mp.solutions.face_detection

def analyze_frame(image):
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    h, w, _ = img.shape

    with mp_face.FaceDetection(model_selection=0, min_detection_confidence=0.5) as detector:
        results = detector.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        if not results.detections:
            return "❌ No face detected", "❌ Not centered", "❓ Gaze unknown", img

        det = results.detections[0]
        bboxC = det.location_data.relative_bounding_box
        x = int(bboxC.xmin * w)
        y = int(bboxC.ymin * h)
        width = int(bboxC.width * w)
        height = int(bboxC.height * h)
        center_x = x + width // 2

        # Draw bbox
        cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)

        face_status = "✅ Face visible"
        centered_status = "✅ Centered" if 0.3 * w < center_x < 0.7 * w else "⚠️ Not centered"
        gaze_status = "👀 Likely looking at camera" if 0.4 * w < center_x < 0.6 * w else "🙈 Likely distracted"

        return face_status, centered_status, gaze_status, img
