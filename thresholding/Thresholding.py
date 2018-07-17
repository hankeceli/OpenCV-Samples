import cv2
import numpy as np

img = cv2.imread('book-page.jpg')

retval, threshold = cv2.threshold(img, 8, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2nd, threshold2nd = cv2.threshold(grayscaled, 8, 255, cv2.THRESH_BINARY)
gaussian = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)
retval2, otsu = cv2.threshold(grayscaled, 85,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2nd',threshold2nd)
cv2.imshow('gaussian',gaussian)
cv2.imshow('otsu',otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
