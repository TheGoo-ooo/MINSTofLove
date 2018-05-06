##########################################
# https://docs.opencv.org/3.1.0/dd/d49/tutorial_py_contour_features.html
# https://www.pyimagesearch.com/2017/02/13/recognizing-digits-with-opencv-and-python/
import numpy as np
import cv2

from imutils.perspective import four_point_transform
from imutils import contours
import imutils


def resize(img, size):
    resImg = cv2.resize(img, (size, size), interpolation=cv2.INTER_AREA)
    return resImg


def show(img, title):
    print("Image :", img.shape)
    cv2.imshow(title, img)
    cv2.waitKey(0)


def save(img, path):
    cv2.imwrite(path, img)
    cv2.destroyAllWindows()
    print("Saved image")


def extract(image, type):

    show(image, "Normal")
    # Convert to grayscale and apply Gaussian filtering
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    show(gray, 'gray')

    # Threshold the image
    # for segmenting the number, OTSU for image in rgb
    ret, img_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    show(img_thresh, 'img_thresh')
    # it's too low gray, doesn't work
    # Find contours in the image
    black, ctrs, hier = cv2.findContours(img_thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    show(black, 'black')

    # Get rectangles contains each contour
    rects = [cv2.boundingRect(ctr) for ctr in ctrs]
    i = 0
    for rect in rects:
         cv2.rectangle(image, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3)
         show(image, 'rect')
         # Make the rectangular region around the digit
         extractedImg = img_thresh[rect[1]:(rect[1]+rect[3]), rect[0]:(rect[0]+rect[3])]
         # Resize the image
         extractedImg = resize(extractedImg, 28)
         extractedImg = cv2.dilate(extractedImg, (3, 3))

         if type == 'JULIEN':
             extractedImg = cv2.bitwise_not(extractedImg)
             #show(extractedImg, 'JULIEN')

         save(extractedImg,"../ressources/result"+str(i)+".png")
         i = i+1


def preprocessGAB(filename, type='FASMY'):
    image = cv2.imread(filename)
    extract(image, type)


if __name__ == "__main__":
    name = "image1"
    filename = "../ressources/" + name + ".png "
    preprocessGAB(filename)
