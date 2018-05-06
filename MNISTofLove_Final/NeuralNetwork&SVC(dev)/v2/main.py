import numpy as np
from dnn import NeuralNetwork, Layer
from activation import ActivationFunction as af
from backpropagation import BackPropagation

input =     [[1, 1], [1, 0]]
solution =  [[1],    [0]]

layers = Layer.createLayers([2, 3, 3, 1])
dnn = NeuralNetwork(layers)
bp = BackPropagation(dnn, input, solution)

bp.propagate()



"""
Show layers in dnn
------------------
for layer in layers:
    print(layer)
"""
