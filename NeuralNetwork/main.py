from dnn import NeuralNetwork

dnn = NeuralNetwork()
dnn.initLayer(*[2, 2, 2])
dnn.setActivation(*[dnn.tanh, dnn.tanh, dnn.softmax])
dnn.feedForward()

print(dnn)
print("\nOutput: " + str(dnn.getOutput()))

print("done!")
