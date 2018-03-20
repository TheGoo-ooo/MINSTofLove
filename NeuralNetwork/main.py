from dnn import NeuralNetwork
from backprop import BackPropagation

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
backprop = BackPropagation(dnn, input_data, solution)

dnn.initLayer(*[2, 3, 1])
dnn.setActivation(*[dnn.none, dnn.tanh, dnn.relu])
dnn.feedForward()

backprop.initOutput()


print(backprop)
print(dnn)
print("\nOutput: " + str(dnn.getOutput()))

print("done!")
