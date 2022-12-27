#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp
fing = ["Thumb finger","Index finger","Middle finger","Ring finger","Pinky finger"]
Nfing = 5
cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 8:
                    id8 = int(id)
                    cy8 = cy
                if id == 7:
                    id7 = int(id)
                    cy7 = cy
                if id == 12:
                    id12 = int(id)
                    cy12 = cy
                if id == 11:
                    id11 = int(id)
                    cy11 = cy
                if id == 16:
                    id16 = int(id)
                    cy16 = cy
                if id == 15:
                    id15 = int(id)
                    cy15 = cy
                if id == 20:
                    id20 = int(id)
                    cy20 = cy
                if id == 19:
                    id19 = int(id)
                    cy19 = cy
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
            
            if ((cy12 > cy11)and(cy8 > cy7)and(cy16 > cy15)and(cy20 > cy19)and(cx4 < cx3)):
                Nfing = 0
                fing = "none"
            elif ((cy12 > cy11)and(cy8 > cy7)and(cy16 > cy15)and(cy20 > cy19)):
                Nfing = 1
                fing = "Thumb"
            elif ((cy12 > cy11)and(cx4 < cx3)and(cy16 > cy15)and(cy20 > cy19)):
                Nfing = 1
                fing = "Index"
            elif ((cx4 < cx3)and(cy8 > cy7)and(cy16 > cy15)and(cy20 > cy19)):
                Nfing = 1
                fing = "Middle"
            elif ((cy12 > cy11)and(cy8 > cy7)and(cx4 < cx3)and(cy20 > cy19)):
                Nfing = 1
                fing = "Ring"
            elif ((cy12 > cy11)and(cy8 > cy7)and(cy16 > cy15)and(cx4 < cx3)):
                Nfing = 1
                fing = "Pinky"
            elif ((cx4 < cx3)and(cy8 > cy7)and(cy12 > cy11)):
                Nfing = 2
                fing = "Ring,Pinky"
            elif ((cx4 < cx3)and(cy8 > cy7)and(cy16 > cy15)):
                Nfing = 2
                fing = "Middle,Pinky"
            elif ((cx4 < cx3)and(cy8 > cy7)and(cy20 > cy19)):
                Nfing = 2
                fing = "Middle,Ring"
            elif ((cx4 < cx3)and(cy12 > cy11)and(cy16 > cy15)):
                Nfing = 2
                fing = "Index,Pinky"
            elif ((cx4 < cx3)and(cy12 > cy11)and(cy20 > cy19)):
                Nfing = 2
                fing = "Index,Ring"
            elif ((cx4 < cx3)and(cy16 > cy15)and(cy20 > cy19)):
                Nfing = 2
                fing = "Index,Middle"
            elif ((cy12 > cy11)and(cy16 > cy15)and(cy20 > cy19)):
                Nfing = 2
                fing = "Thumb,Index"
            elif ((cy8 > cy7)and(cy16 > cy15)and(cy20 > cy19)):
                Nfing = 2
                fing = "Thumb,Middle"
            elif ((cy12 > cy11)and(cy8 > cy7)and(cy20 > cy19)):
                Nfing = 2
                fing = "Thumb,Ring"
            elif ((cy12 > cy11)and(cy8 > cy7)and(cy16 > cy15)):
                Nfing = 2
                fing = "Thumb,Pinky"
            elif ((cx4 < cx3)and(cy8 > cy7)):
                Nfing = 3
                fing = "Middle,Ring,Pinky"
            elif ((cx4 < cx3)and(cy12 > cy11)):
                Nfing = 3
                fing = "Index,Ring,Pinky"
            elif ((cx4 < cx3)and(cy16 > cy15)):
                Nfing = 3
                fing = "Index,Middle,Pinky"
            elif ((cx4 < cx3)and(cy20 > cy19)):
                Nfing = 3
                fing = "Index,Middle,Ring"
            elif ((cy8 > cy7)and(cy12 > cy11)):
                Nfing = 3
                fing = "Thumb,Ring,Pinky" 
            elif ((cy8 > cy7)and(cy16 > cy15)):
                Nfing = 3
                fing = "Thumb,Middle,Pinky"
            elif ((cy8 > cy7)and(cy20 > cy19)):
                Nfing = 3
                fing = "Thumb,Middle,Ring"
            elif ((cy12 > cy11)and(cy16 > cy15)):
                Nfing = 3
                fing = "Thumb,Index,Pinky"
            elif ((cy12 > cy11)and(cy20 > cy19)):
                Nfing = 3
                fing = "Thumb,Index,Ring"
            elif ((cy16 > cy15)and(cy20 > cy19)):
                Nfing = 3
                fing = "Thumb,Index,Middle"
            elif ((cy8 > cy7)):
                Nfing = 4
                fing = "Thumb,Middle,Ring,Pinky"
            elif ((cy12 > cy11)):
                Nfing = 4
                fing = "Thumb,Index,Ring,Pinky"
            elif ((cy16 > cy15)):
                Nfing = 4
                fing = "Thumb,Index,Middle,Pinky"
            elif ((cy20 > cy19)):
                Nfing = 4
                fing = "Thumb,Index,Middle,Ring"
            elif ((cx4 < cx3)):
                Nfing = 4
                fing = "Index,Middle,Ring,Pinky"
            else: 
                Nfing = 5
                fing = "Thumb,Index,Middle,Ring,Pinky"
                
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
        
        cv2.putText(img, str(int(Nfing)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 97, 3), 3)
        cv2.putText(img, str(fing), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2,
                    (127, 255, 0), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()