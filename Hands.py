import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
import time
font = cv2.FONT_HERSHEY_COMPLEX


def fing_Counter(image):
    with mp_hands.Hands(
       static_image_mode=True,
       max_num_hands=2,
       min_detection_confidence=0.5) as hands:

       # Read an image, flip it around y-axis for correct handedness output (see
       # above).
       
       # Convert the BGR image to RGB before processing.
       results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
       if not results.multi_hand_landmarks:
           print("Continue")

       # Print handedness and draw hand landmarks on the image.
       print('Handedness:', results.multi_handedness)
       image_height, image_width, _ = image.shape
       annotated_image = image.copy()
       count = 0
       lm_info = []
       fingers = []
       for hand_landmarks in results.multi_hand_landmarks:
         for hand_lms in results.multi_hand_landmarks:
             for id , lm in enumerate(hand_lms.landmark):
                 h , w , c = annotated_image.shape
                 cx , cy = int(lm.x*w) , int(lm.y*h)
                 #converting decimal value of landmark into pixels
                 print(id,cx,cy)
                 a=[]
                 a.append(id)
                 a.append(cx)
                 a.append(cy)
                 lm_info.append(a)
         for i in range(8,21,4):
             if(lm_info[i][2] <  lm_info[i-2][2]):
                 fingers.append(1)
             else:
                 fingers.append(0)
         # For right hand image just turn '<' into '>'
         if((lm_info[4][1]>=lm_info[5][1] and lm_info[3][1]<=lm_info[17][1]) or (lm_info[4][1]<=lm_info[5][1] and lm_info[3][1]>=lm_info[17][1])):
             fingers.append(0)
         else:
             fingers.append(1)
##         
##         if(lm_info[4][1] <  lm_info[3][1]):
##             fingers.append(1)
##         else:
##             fingers.append(0)
         #print('hand_landmarks:', hand_landmarks)
         print(lm_info)
         print(fingers)
         count = count + 1

       annotated_image=image
       
       # Resizing image
       annotated_image= cv2.resize(annotated_image,(800,600))
       
       counter = 0
       for i in fingers:
           if(i==1):
               counter = counter + 1
               
       cv2.putText(annotated_image,f'Fingers : {counter}',(230,550), font, 2,(0,0,255),3) 

       cv2.imwrite(r'hands.png', annotated_image)
       cv2.imshow('hands.png', annotated_image)
       
       print("Image shape : ",annotated_image.shape)
       if(counter == 1):
           light = cv2.imread('light.jpg')
           light = cv2.resize(light,(800,600))
           blended = cv2.addWeighted(annotated_image, 0.6, light, 0.4, 0)
           cv2.imwrite(r's_filter.png', annotated_image)
           cv2.imshow('s_filter.png',blended)

       if(counter == 2):
           sun = cv2.imread('sun.jpg')
           sun = cv2.resize(sun,(800,600))
           blended = cv2.addWeighted(annotated_image, 0.6, sun, 0.4, 0)
           cv2.imwrite(r's_filter.png', annotated_image)
           cv2.imshow('s_filter.png',blended)

           
       if(counter == 3):
           rain = cv2.imread('rain.png')
           rain = cv2.resize(rain,(800,600))
           blended = cv2.addWeighted(annotated_image, 0.7, rain, 0.3, 0)
           cv2.imwrite(r's_filter.png', annotated_image)
           cv2.imshow('s_filter.png',blended)

       if(counter == 4):
           snow_flake = cv2.imread('snow_bg.jpg')
           snow_flake = cv2.resize(snow_flake,(800,600))
           blended = cv2.addWeighted(annotated_image, 0.7, snow_flake, 0.3, 0)
           cv2.imwrite(r's_filter.png', annotated_image)
           cv2.imshow('s_filter.png',blended)

       if(counter == 5):
           moon = cv2.imread('moon.png')
           moon = cv2.resize(moon,(800,600))
           blended = cv2.addWeighted(annotated_image, 0.7, moon, 0.3, 0)
           cv2.imwrite(r's_filter.png', annotated_image)
           cv2.imshow('s_filter.png',blended)

#  Function calling

# Uncomment last two line to check manually

image = cv2.imread('c_palm.jpeg')  #Insert your Image Here
fing_Counter(image)


