import cv2

a = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #Assigning Haarcase File
b = cv2.VideoCapture(0)                                          #Access to the video camera

while(True):
    c_rec, d_imag = b.read()                                     #'c_rec' is for to show Rectangular box in camera, 'd_imag' is for to detect image.
    e = cv2.cvtColor(d_imag, cv2.COLOR_BGR2GRAY)                 #This line converts the captured image into Black&White(Gray)
    f = a.detectMultiScale(e, 1.3,6)
    
    for(x1, y1, w1, h1) in f:                                    #'y1' and 'h1' is for HORIZONTAL & 'x1' and 'w1' is for VERTICAL
        cv2.rectangle(d_imag, (x1, y1), (x1+w1, y1+h1), (0, 255, 0), 10)            #(0,255,0) firstValue 0 represents BLUE, secondValue 255 represents GREEN, thirdValue 0 represents RED
    
    cv2.imshow('img', d_imag)
    h = cv2.waitKey(40) & 0xff                                  #To detect the face with in 40 seconds otherwise exit the program
    if h == 40:
        break
    
    
b.release()
cv2.destroyAllWindows()
        