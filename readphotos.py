import cv2 as cv

img = cv.imread('Photos/friends.jpg') #read image file

cv.imshow('Friends', img) #display image file

cv.waitKey(0) #infinite delay