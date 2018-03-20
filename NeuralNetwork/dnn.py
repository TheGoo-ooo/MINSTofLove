import numpy as np
import numpy.random as rdm

class NeuralNetwork:
    """
    A neural network made for study and trainning purposes. Simple and easy
    to read. Meant for the newbies in the field. Have fun!

    Author:
        Florian Fasmeyer
        He-Arc/HES-SO
        Neuchâtel - Suisse

    Recommendation:
        Understanding Activation Functions in Neural Networks:
        https://medium.com/the-theory-of-everything/understanding-activation-
            functions-in-neural-networks-9491262884e0

        But what *is* a Neural Network? | Chapter 1, deep learning:
        https://www.youtube.com/watch?v=aircAruvnKk&t=187s&ab_channel
            =3Blue1Brown

    Credits:
        Avinash Sharma V - for the article on activation functions (medium.com).
        3Blue1Brown - for the video course on deep learning (Youtube).
    """

    def __init__(self):
        self.__current_layer = 0
        self.layers = []
        self.bias = []
        self.weights = []
        self.activation_func = []


    def __str__(self):
        """ A simple display for small networks."""

        accu = "NeuralNetwork Object: " + str(len(self.layers)) + " layers.\n"

        accu += "Layers:\n"
        for i in range(len(self.layers)):
            accu += (str(i) + ": " + str(self.layers[i]) + "\n")

        accu += "Bias:\n"
        for i in range(len(self.bias)):
            accu += (str(i) + ": " + str(self.bias[i]) + "\n")

        accu += "Weights:\n"
        for i in range(len(self.weights)):
            accu += (str(i) + ":\n" + str(self.weights[i]) + "\n")

        return accu

# Activation funcitons.
    def sigmoid(self, *values, derivate=False):
        if derivate is True:
            return [(np.exp(-x))/ float(np.power(1+np.exp(-x), 2))
                    for x in values]
        return [1/float(1+np.exp(-x)) for x in values]


    def tanh(self, *values, derivate=False):
        if derivate is True:
            return [1/float(np.power(np.cosh(x),2)) for x in values]
        return [np.tanh(x) for x in values]


    def softmax(self, *values, derivate=False):
        if derivate is True:
            print("(Softmax) This function has no derivative "+
                  " asigned to it for now.")
            return 1
        return np.exp(values) / float(sum(np.exp(values)))



    def relu(self, *values, derivate=False):
        if derivate is True:
            return [ 0 if x<0 else 1 for x in values]
        return [np.maximum(0, x) for x in values]

    def none(self, *values, derivate=False):
        if derivate is True:
            return [1 for x in values]
        return values

# Public funcitons.
    def feedForward(self):
        self.layers[0] = np.array(
            self.activation_func[0](*self.layers[0]))

        for i in range(len(self.layers)-1):
            self.layers[i+1] = self.layers[i].dot(self.weights[i])+ self.bias[i]
            self.layers[i+1] = np.array(
                self.activation_func[i+1](*self.layers[i+1]))


    def initLayer(self, *neurons_per_layers):
        for nb_neurons in neurons_per_layers:
            self.__makeLayer(nb_neurons)
        self.__current_layer = 0


    def getOutput(self):
        self.feedForward()
        return self.layers[len(self.layers)-1]


    def setActivation(self, *func, index=None):
        if len(func) == len(self.activation_func):
            for i in range(len(self.activation_func)):
                self.activation_func[i] = func[i]
        elif len(func) == 1 and index is None:
            for i in range(len(self.activation_func)):
                self.activation_func[i] = func[0]
        elif len(func) == 1 and index is not None:
            self.activation_func[index] = func[0]
        else:
            print("Warning! Could not modify the activation function.")
            print("Try naming function attributs: setActivation(index=...).")

# "Private" funcitons.
    def __makeLayer(self, nb_neurons):
        # Create layer.
        self.layers.append(np.zeros(nb_neurons))

        if self.__current_layer is not 0:
            last_layer_len = len(self.layers[self.__current_layer-1])

            # Create bias
            bias_potential = last_layer_len -1
            self.bias.append(
                bias_potential * (2*rdm.random_sample(nb_neurons)-1))

            # Create weight[-1; 1] with last layer.
            self.weights.append(
                2*rdm.random_sample((last_layer_len, nb_neurons))-1)

        # Set default activation function.
        self.activation_func.append(self.relu)

        self.__current_layer += 1
