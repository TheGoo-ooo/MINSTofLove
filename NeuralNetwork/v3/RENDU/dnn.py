'''
    Neural Network Trainning
    by Florian Fasmeyer
    HES-SO, He-arc Neuchâtel
    06.05.2018
'''

import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics

# Load data.
dataset = datasets.fetch_mldata("MNIST Original")

# Prepare data.
images_and_labels = list(zip(dataset.data, dataset.target))
n_samples = len(dataset.data)
data = dataset.data.reshape((n_samples, -1))
X = data
y = dataset.target

# Prepare cross validation.
from sklearn.model_selection import ShuffleSplit
cv = ShuffleSplit(n_splits=50, test_size=0.20, random_state=0)

# Multi-layer Preceptron classifier.
from sklearn.neural_network import MLPClassifier
classifier = MLPClassifier(
    solver='lbfgs',
    activation='tanh',
    learning_rate='adaptive',
    )
from sklearn.model_selection import cross_val_score
scores = cross_val_score(classifier, X, y, cv=cv)

# Using cross validation.
plt.plot(scores)
plt.ylim(0, 1.01)
plt.show()
print("avg, min, max:")
print(scores.mean(), scores.min(), scores.max())

# Without cross validation.
import math
size_training_data = math.ceil(n_samples * 0.75)
size_testing_data = n_samples - size_training_data
    # Train Network.
classifier.fit(data[:size_training_data], dataset.target[:size_training_data])
    # Test Network.
expected = dataset.target[size_testing_data:]
predicted = classifier.predict(data[size_testing_data:])
    # Get metrics.
print("Classification report for classifier:\n%s\n"
      % (metrics.classification_report(expected, predicted)))


# Save trained network.
from sklearn.externals import joblib
classifier.fit(X,y) # Train with all the data avaliable (final version)
joblib.dump(classifier, 'trained_neural_network.pkl')

# Example load and use network.
test_classifier = joblib.load('trained_neural_network.pkl')
prediction = test_classifier.predict(X[0:1])
print(prediction)
print(y[0])
if y[0] == prediction[0]:
    print("Prediction match expected result")
