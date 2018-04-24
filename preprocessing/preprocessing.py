##########################################
# https://docs.opencv.org/3.1.0/dd/d49/tutorial_py_contour_features.html
# https://www.pyimagesearch.com/2017/02/13/recognizing-digits-with-opencv2-and-python/
import numpy as np
import cv2

from imutils.perspective import four_point_transform
from imutils import contours
import imutils


def resize(img, size):
    resImg = cv2.resize(img, (size, size), interpolation=cv2.INTER_CUBIC)
    return resImg


def show(img, title):
    print("Image :", img.shape)
    cv2.imshow(title, img)
    cv2.waitKey(0)


def save(img):
    cv2.imwrite("../ressources/result.png", img)
    cv2.destroyAllWindows()
    print("Saved image")


def extract(image):

    show(image, "Normal")
    # Load an color image black and grey
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGBA2GRAY)
    show(gray_image, "Normal en gris")

    blurred = cv2.GaussianBlur(gray_image, (5, 5), 0)
    edge = cv2.Canny(blurred, 50, 200, 255)

    #show(edge, "Edge")

    contours = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if imutils.is_cv2() else contours[1]
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    displayContours = None

    # loop over the contour
    for i in contours:
        # approximate the contour
        perimeter = cv2.arcLength(i, True)
        approximation = cv2.approxPolyDP(i, 0.1 * perimeter, True)

        if len(approximation) == 4:
            displayContours = approximation
            break

    warped = four_point_transform(gray_image, displayContours.reshape(4, 2))
    output = four_point_transform(image, displayContours.reshape(4, 2))

    print("Extracted image")

    return warped, output

if __name__ == "__main__":
    name = "trois"
    filename = "../ressources/" + name + ".png "
    image = cv2.imread(filename)

    gray = cv2.cvtColor(image, cv2.COLOR_RGBA2GRAY)

    (thresh, black_image) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    contours = cv2.findContours(black_image, 1, 2)
    cnt = contours[0]
    show(black_image, "Black")
    x, y, w, h = cv2.boundingRect(cnt)
    #x:x+w, y:y+h
    newImage = image[y:(y+h), x:(x+w)]
    print("x y h w", x, y, h, w)
    show(newImage, "new")
    newImage_gray = cv2.cvtColor(newImage, cv2.COLOR_RGBA2GRAY)
    show(newImage_gray, "newgrey")
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    show(image, "new rectangle")
    (height, width) = image.shape[:2]
    if height > 28 or width > 28:
        #warped, output = extract(newImage)
        warped = newImage_gray
        output = newImage

    else:
        warped = gray
        output = image

    show(warped, "after Extracted image grey")
    show(output, "after Extracted image")


    thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    show(thresh, "Thresh")
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 2))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    show(thresh, "Thresh opening")
    thresh = cv2.threshold(warped, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    show(thresh, "Thresh final")

    save(resize(thresh, 28))
