# -*- coding: utf-8 -*-
"""
@author: FeuilladeJu
"""
from matplotlib import pyplot as plt
from matplotlib import patches

from skimage.feature import hog
from skimage import measure
from skimage import morphology

from sklearn.datasets import fetch_mldata
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

import numpy as np
import pickle
import cv2

import os
import os.path

class KNNDigits():
    def __init__(self, image):
        self.PATH_IMAGE = image
        self.PATH_SAV='digit_model.sav'
        
        #Va télécharger les données MNIST si il n'existe pas
        mnist = fetch_mldata('mnist-original', data_home="data")
        
        x = np.array(mnist.data, 'int16')
        y = np.array(mnist.target, 'int')
        
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
        
        if os.path.isfile(self.PATH_SAV) and os.access(self.PATH_SAV, os.R_OK):
            pass
        else:
            # Ces deux lignes sert à créer le modèle .sav qui est le résultat de l'entrainement du modèle
            self.modelTrain(x_train,y_train)
            
#        im ,t = self.scoreKnn(x_test,y_test)
        self.predictionKnn = self.rectangleImage(cv2.imread(self.PATH_IMAGE), 10) 
        
    def __str__(self):
        return str(self.predictionKnn)

    #On utilise le model MNIST pour entrainer notre modèle
    def modelTrain(self, x_train, y_train):
        list_hog_fd = []
        for feature in x_train:
            fd = hog(feature.reshape((28, 28)), orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1),
                     visualise=False)
            list_hog_fd.append(fd)
    
        x_train = np.array(list_hog_fd, 'float64')
    
        knn = KNeighborsClassifier()
    
        knn.fit(x_train, y_train)
        #Sauvegarder le modèle
        pickle.dump(knn, open(self.PATH_SAV, 'wb'))
    
#    #Obtient le pourcentage de test réussis
#    def scoreKnn(self, x_test, y_test):
#        # load the model from disk
#        knn = pickle.load(open(self.PATH_SAV, 'rb'))
#        list_hog_fd = []
#        for feature in x_test:
#            fd = hog(feature.reshape((28, 28)), orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1),
#                     visualise=False)
#            list_hog_fd.append(fd)
#    
#        x_test = np.array(list_hog_fd, 'float64')
#    
#        score = knn.score(x_test, y_test)
#        print("Le score est : ")
#        print(np.round(score * 100, 2), "%")
#    
#        return x_test, y_test
    
    #La prediction avec l'algo de KNN
    def predictionKnn(self, image):
        knn = pickle.load(open(self.PATH_SAV, 'rb'))
        expected = knn.predict(image)
        return expected[0]
    
    #Va traiter l'image et ensuite trouver le nombre de chiffres sur l'image
    def inputImage(self, image,k = 0):
        imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        (thresh, im_bw) = cv2.threshold(imgray, 90, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        im_bw = np.array(255-im_bw, dtype=bool)
        cleaned = morphology.remove_small_objects(im_bw, min_size=20, connectivity=2)
        cleaned = np.array(cleaned, dtype=int)
        cleaned = 255+cleaned
        label, n = measure.label(cleaned, neighbors=8, background=255, return_num=True, connectivity=2)
        print("Nombres de chiffres : ",n)
        x = []
        y = []
        numbers = []
        ph=[]
        rect=[]
        for i in range(1, n + 1):
            for r in range(label.shape[0]):
                for c in range(label.shape[1]):
                    if label[r, c] == i:
                        x.append(r)
                        y.append(c)
    
            digit = im_bw[min(x): max(x), min(y): max(y)]
    
            rect.append([(min(y), min(x)), (max(y) - min(y)), (max(x) - min(x))])
            padd_y = 0
            padding = np.zeros([digit.shape[0]+padd_y, digit.shape[1] + k], dtype='float64')
            padding[padd_y//2:padding.shape[0]-padd_y//2, k//2:padding.shape[1] - k//2] = digit
            ph.append(padding)
    
            re_digit= cv2.resize(np.array(padding,dtype='float64'), (28, 28), interpolation=cv2.INTER_AREA)
            re_digit = cv2.dilate(re_digit, (3, 3))
    
            roi_hog_fd = hog(re_digit, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualise=False)
    
            numbers.append( np.array([roi_hog_fd], 'float64'))
            x = []
            y = []
    
        return numbers,ph,rect
    
    #Va mettre les limites du rectangle autour des chiffres
    def limitImage(self, rects, nums):
        xx = []
        yy = []
        for n in range(len(nums)):
            x = rects[n][0][0]
            y = rects[n][0][1]
            xx.append(x)
            yy.append(y)
    
        max_x = np.max(xx)
        max_y = np.max(yy)
    
        digits = np.zeros((max_x + 5, max_y + 5), np.object)
    
        return digits
    
    #Va mettre un rectangle autour de chaque chiffre et prédire ces derniers
    def rectangleImage(self, image, padd):
        tabPredic = []
        fig, ax = plt.subplots(1)
        ax.imshow(image)
    
        nums, ph, rects = self.inputImage(image, padd)
        digits = self.limitImage(rects, nums)
        for n in range(len(nums)):
            rect = patches.Rectangle(rects[n][0], rects[n][1], rects[n][2], linewidth=2, edgecolor='r',
                                     facecolor='none')
            
            ax.add_patch(rect)
            ex = self.predictionKnn(nums[n])
            tabPredic.append(int(ex))
    
            digits[rects[n][0][0]][rects[n][0][1]] = [ex]
#            ax.text(rects[n][0][0], rects[n][0][1] -10, str(int(ex)), style='italic')
        
        plt.axis('off')
        fig.savefig('imgResult.png')
        return tabPredic


# = KNNDigits('../ressources/image2.png')
#print(t)