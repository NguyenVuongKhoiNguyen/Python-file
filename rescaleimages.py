import cv2 as cv

img = cv.imread('Photos/friends.jpg')

def rescaleFrame(frame, scale = 0.7): #take in file
    width = int(frame.shape[1] * scale)  #extract size and scale that that size
    height = int(frame.shape[0] * scale)

    dimensions = (width, height) #tuple means storing multiple items in one variable

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA) #adding up frame and dimensions

resized_image = rescaleFrame(img)

cv.imshow('Friend', img)
cv.imshow('Friend Resized', resized_image)
cv.waitKey(0)

