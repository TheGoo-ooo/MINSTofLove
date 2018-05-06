import numpy as np
from dnn import NeuralNetwork
from backprop import BackPropagation
from activation import ActivationFunction as af

input_data =[
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0]
]

solution = [
    [1],
    [0],
    [0],
    [0]
]

dnn = NeuralNetwork()
bp = BackPropagation(dnn, input_data, solution)

dnn.initLayer(*[2, 3, 1])
dnn.setActivation(*[af.none, af.tanh, af.relu])
dnn.feedForward()

bp.propagate()
#print(dnn)

print("done!")
