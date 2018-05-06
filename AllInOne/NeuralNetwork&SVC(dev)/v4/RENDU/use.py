# Import the modules
from sklearn.externals import joblib
import numpy as np

def predict(X):
    # Load the classifier
    clf = joblib.load("digits_cls.pkl")

    # Predict love.
    nbr = clf.predict(np.array([X], 'float64'))
    return nbr
