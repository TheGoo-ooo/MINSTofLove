from sklearn.externals import joblib

def predict(X):
    test_classifier = joblib.load('trained_neural_network.pkl')
    if len(X) == 1:
        value = X
    else:
        value = X
    prediction = test_classifier.predict(value)
    return prediction
