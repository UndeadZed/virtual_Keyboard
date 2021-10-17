import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key,Controller
from time import sleep


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)


detector = HandDetector(detectionCon=0.8)
keys = [["Q","W","E","R","T","Y","U","I","O","P","<"],
        ["A","S","D","F","G","H","J","K","L","_"]
        ,["Z","X","C","V","B","N","M",",","."]]

keyboard = Controller()

def drawALL(img,buttonList):
    for button in buttonList:
        x,y = button.pos
        w,h = button.size
        cv2.rectangle(img,button.pos,(x+w,y+h), (150,200,0), cv2.FILLED)
        cv2.putText(img,button.text,(x+20, y+65), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),4)
    return img



class Button():

    def __init__(self, pos, text, size = [75,75]):
        self.pos = pos
        self.size = size
        self.text = text


buttonList = []
for i in range(len(keys)):
    for j,key in enumerate(keys[i]):
        buttonList.append(Button([100*j+50,100*i+50],key))


while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    img = detector.findHands(img)
    lmlist, bboxinfo = detector.findPosition(img)
    img = drawALL(img,buttonList)

    if lmlist:
        for button in buttonList:
            x,y = button.pos
            w,h = button.size

            if x< lmlist[8][0]<x+w and y<lmlist[8][1] <y+h:
                cv2.rectangle(img,button.pos,(x+w,y+h), (50,100,0), cv2.FILLED)
                cv2.putText(img,button.text,(x+20, y+65), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),4)
                

                l,_,_ = detector.findDistance(8,4,img,draw=False)
                print(l)


                if l<30 and l>15:
                    if button.text == "_":
                        keyboard.press(" ")
                    elif button.text == "<-":
                        keyboard.press(Key.backspace)
                    else:
                        keyboard.press(button.text)
                    cv2.rectangle(img,button.pos,(x+w,y+h), (0,255,0), cv2.FILLED)
                    cv2.putText(img,button.text,(x+20, y+65), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),4)
                    sleep(0.15)

    

    cv2.imshow("frame",img)
    key = cv2.waitKey(27)
    if(key == 27):
        break
cv2.destroyAllWindows()

