from sklearn.externals import joblib
from skimage.feature import hog
from sklearn import datasets
from skimage.feature import hog
from sklearn.svm import LinearSVC
import numpy as np

def predict(X):
    test_classifier = joblib.load('trained_model.pkl')

    list_hog_fd = []
    for feature in X:
        fd = hog(feature.reshape((28, 28)), orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualise=False)
        list_hog_fd.append(fd)
    hog_features = np.array(list_hog_fd, 'float64')

    prediction = test_classifier.predict(hog_features)
    return prediction
