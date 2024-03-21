import cv2
import mediapipe as mp
import math
import time
import pyfirmata2

board = pyfirmata2.Arduino('COM9')
led1 = board.get_pin("d:3:p")
led2 = board.get_pin("d:5:p")
led3 = board.get_pin("d:6:p")
led4 = board.get_pin("d:9:p")
led5 = board.get_pin("d:10:p")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
mp_hands = mp.solutions.hands
hand = mp_hands.Hands(max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

hand_detected = False
start_time = time.time()
timeout_duration = 1.0  

while True:
    success, frame = cap.read()
    if success:
        frame_flipped = cv2.flip(frame, 1)
        RGB_frame = cv2.cvtColor(frame_flipped, cv2.COLOR_BGR2RGB)
        results = hand.process(RGB_frame)

        if results.multi_hand_landmarks:
            hand_detected = True

            handlandmaks = results.multi_hand_landmarks[0]
            zeropoint = handlandmaks.landmark[0]
            indexfinger = handlandmaks.landmark[8]
            thumbinger = handlandmaks.landmark[4]
            middlefinger = handlandmaks.landmark[12]
            ringfinger = handlandmaks.landmark[16]
            pinky = handlandmaks.landmark[20]

            distanse1 = math.sqrt((thumbinger.x - zeropoint.x)**2 + (thumbinger.y - zeropoint.y)**2)
            distanse2 = math.sqrt((indexfinger.x - zeropoint.x)**2 + (indexfinger.y - zeropoint.y)**2)
            distanse3 = math.sqrt((middlefinger.x - zeropoint.x)**2 + (middlefinger.y - zeropoint.y)**2)
            distanse4 = math.sqrt((ringfinger.x - zeropoint.x)**2 + (ringfinger.y - zeropoint.y)**2)
            distanse5 = math.sqrt((pinky.x - zeropoint.x)**2 + (pinky.y - zeropoint.y)**2)
            print(distanse1,"di1")
            # print(distanse2,"di2")
            # print(distanse3,"di3")
            # print(distanse4,"di3")
            # print(distanse5,"di5")




            if distanse1 > 0.13375745176688528:
                led1.write(distanse1*2)
            else:
                led1.write(0)
            if distanse2 > 0.1292740404954853:
                led2.write(distanse2*2)
            else:
                led2.write(0)
            if distanse3 > 0.09600606591295043:
                led3.write(distanse3*2)
            else:
                led3.write(0)
            if distanse4 > 0.1488111007020982:
                led4.write(distanse5*2)
            else:
                led4.write(0)

            if distanse5 > 0.08504636112912782:
                led5.write(distanse5*2)
            else:
                led5.write(0)

            start_time = time.time()  
        else:
            if hand_detected and time.time() - start_time > timeout_duration:
                led1.write(0)
                led2.write(0)
                led3.write(0)
                led4.write(0)
                led5.write(0)
                hand_detected = False

        cv2.imshow("Captured Image", frame_flipped)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

cv2.destroyAllWindows()
cap.release()
