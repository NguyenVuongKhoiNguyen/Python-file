import cv2 as cv

def rescaleFrame(frame, scale = 0.7): #take in frame
    width = int(frame.shape[1] * scale)  #scale that frame into new size
    height = int(frame.shape[0] * scale) #scale that frame into new size

    dimensions = (width, height) #tuple means storing multiple items in one variable

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA) #adding up frame and dimensions

capture = cv.VideoCapture('Videos/osmosis.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('Resized video', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release 
cv.destroyAllWindows 