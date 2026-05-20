import streamlit as st
from turtle import st

import cv2
import mediapipe as mp

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)

# Open webcam
streamlit-webrtc

def detect_gesture(hand_landmarks, hand_label):

    finger_status = []

    finger_tips = [4, 8, 12, 16, 20]

    # Thumb detection
    if hand_label == "Right":

        if hand_landmarks.landmark[finger_tips[0]].x < hand_landmarks.landmark[finger_tips[0] - 1].x:
            finger_status.append(1)
        else:
            finger_status.append(0)

    else:

        if hand_landmarks.landmark[finger_tips[0]].x > hand_landmarks.landmark[finger_tips[0] - 1].x:
            finger_status.append(1)
        else:
            finger_status.append(0)

    # Other fingers
    for tip in finger_tips[1:]:

        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            finger_status.append(1)
        else:
            finger_status.append(0)

    # Gesture rules
    if finger_status == [0, 0, 0, 0, 0]:
        return "FIST"

    elif finger_status == [1, 1, 1, 1, 1]:
        return "OPEN HAND"

    elif finger_status == [0, 1, 1, 0, 0]:
        return "PEACE"

    elif finger_status == [0, 1, 0, 0, 0]:
        return "FIRST"

    elif finger_status == [1, 1, 0, 0, 1]:
        return "ROCK"

    # Thumbs up
    thumb_up = (
        hand_landmarks.landmark[4].y <
        hand_landmarks.landmark[3].y <
        hand_landmarks.landmark[2].y
    )

    other_fingers_closed = (
        finger_status[1] == 0 and
        finger_status[2] == 0 and
        finger_status[3] == 0 and
        finger_status[4] == 0
    )

    if thumb_up and other_fingers_closed:
        return "YES"

    return "UNKNOWN"


while True:

    success, frame = camera.read()

    if not success:
        break

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process hand detection
    result = hands.process(rgb_frame)

    # If hand detected
    if result.multi_hand_landmarks and result.multi_handedness:

        for landmarks, hand_info in zip(
            result.multi_hand_landmarks,
            result.multi_handedness
        ):

            hand_label = hand_info.classification[0].label

            # Draw landmarks
            mp_draw.draw_landmarks(
                frame,
                landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Detect gesture
            gesture = detect_gesture(landmarks, hand_label)

            # Display gesture text
            cv2.putText(
                frame,
                f"Gesture: {gesture}",
                (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 0, 0),
                2
            )

    # Show webcam
    st.image(frame, channels="BGR")

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release webcam
camera.release()
cv2.destroyAllWindows()