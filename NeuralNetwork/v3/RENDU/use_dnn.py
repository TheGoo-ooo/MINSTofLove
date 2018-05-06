from sklearn.externals import joblib

predict(X):
    test_classifier = joblib.load('trained_neural_network.pkl')
    if len(X) == 1:
        value = [X]
    else:
        value = X
    prediction = test_classifier.predict(value)
    return preduction
