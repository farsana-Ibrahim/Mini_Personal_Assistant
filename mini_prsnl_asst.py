import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from keras.models import load_model
import pyautogui
import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model('D:\programs\AI\project\mini_prsnl_asstnt\mp_hand_gesture')

# Load class names
f = open('D:\programs\AI\project\mini_prsnl_asstnt\gesture.names', 'r')
classNames = f.read().split('\n')
f.close()
print(classNames)

# Initialize the webcam
cap = cv2.VideoCapture(0)
commands = []
gesture_mode = False  # Flag to control mode

while True:
    # Read each frame from the webcam
    _, frame = cap.read()

    x, y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if gesture_mode:
        # Get hand landmark prediction
        result = hands.process(framergb)

        className = ''

        # post-process the result
        if result.multi_hand_landmarks:
            landmarks = []
            for handslms in result.multi_hand_landmarks:
                for lm in handslms.landmark:
                    lmx = int(lm.x * x)
                    lmy = int(lm.y * y)
                    landmarks.append([lmx, lmy])

                # Drawing landmarks on frames
                mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

                # Predict gesture
                prediction = model.predict([landmarks])
                classID = np.argmax(prediction)
                className = classNames[classID]

                if len(commands) < 2:
                    if className not in commands:
                        commands.append(className)
                else:
                    print(commands)
                    first = commands[0]
                    second = commands[1]

                    if first == "close":
                        pyautogui.hotkey('win', 'down')
                        pyautogui.hotkey('win', 'down')

                    elif first == "hold":
                        pyautogui.hotkey('alt', 'tab')
                        pyautogui.hotkey('win', 'up')

                    elif first == "six":
                        pyautogui.hotkey('win', '6')

                    elif first == "two":
                        pyautogui.hotkey('win', '2')

                    elif first == "three":
                        pyautogui.hotkey('win', '3')

                    elif first == "select all" and second == "close":
                        pyautogui.hotkey('ctrl', 'a')
                        pyautogui.hotkey('ctrl', 'c')

                    elif first == "close" and second == "select all":
                        pyautogui.hotkey('ctrl', 'v')

                    elif first == "pause":
                        pyautogui.hotkey('space')

                    commands.clear()

    else:
        # Use the default microphone as the audio source
        with sr.Microphone() as source:
            print("Speak something...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise

            try:
                audio_data = recognizer.listen(source)  # Listen to the microphone input

                # Recognize speech using Google Web Speech API
                recognized_text = recognizer.recognize_google(audio_data)
                print("Recognized text: " + recognized_text)
                recognized_text = recognized_text.lower()

                if recognized_text == "activate hand gesture":
                    gesture_mode = True
                    print("Hand gesture mode activated")

                elif recognized_text == "deactivate hand gesture":
                    gesture_mode = False
                    print("Hand gesture mode deactivated")

                elif recognized_text == "open chrome" or recognized_text == "open browser":
                    pyautogui.hotkey('win','1')
                elif recognized_text == "open file explorer":
                    pyautogui.hotkey('win','2')
                elif recognized_text == "open microsoft edge":
                    pyautogui.hotkey('win','3')
                elif recognized_text == "open microsoft store":
                    pyautogui.hotkey('win','4')
                elif recognized_text == "open visual studio code":
                    pyautogui.hotkey('win','5')
                elif recognized_text == "open spotify":
                    pyautogui.hotkey('win','6')
                elif recognized_text == "minimise the window":
                    pyautogui.hotkey('win','down')
                    pyautogui.hotkey('win','down')
                elif recognized_text == "open the last window":
                    pyautogui.hotkey('alt','tab')
                    pyautogui.hotkey('win','up')
                elif recognized_text == "select all and copy": 
                    pyautogui.hotkey('ctrl','a')
                    pyautogui.hotkey('ctrl', 'c')
                elif recognized_text == "paste it":
                    pyautogui.hotkey('ctrl','v')
                elif recognized_text == "stop it":
                    pyautogui.hotkey('space')
                elif recognized_text == "play":
                    pyautogui.hotkey('space')
                elif recognized_text == "volume up" or recognized_text == "increase volume":
                    pyautogui.hotkey('volumeup')
                elif recognized_text == "volume down" or recognized_text == "decrease volume":
                    pyautogui.hotkey('volumedown')

                else:
                    print("Cannot understand the language")

            except sr.UnknownValueError:
                print("Speech recognition could not understand the audio")

            except sr.RequestError as e:
                print("Error occurred;{0}".format(e))

    # Show the final output
    cv2.imshow("Output", frame)
    print("Detection started")

    if cv2.waitKey(1) == ord('q'):
        break

# Release the webcam and destroy all active windows
cap.release()
cv2.destroyAllWindows()
