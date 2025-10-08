import cv2 as cv

capture = cv.VideoCapture('Videos/osmosis.mp4') #create a capture device

while True:
    isTrue, frame = capture.read() #read frame by frame
    cv.imshow('Video', frame) #show frame by frame

    if cv.waitKey(20) & 0xFF == ord('d'): #if p is press then break out of loop
        break

capture.release #release the capture device
cv.destroyAllWindows #close the window

