"""
Author:
    Florian Fasmeyer
    He-Arc/HES-SO
    Neuchâtel - Suisse

Credits:
    Avinash Sharma V - https://medium.com/the-theory-of-everything/
        understanding-activation-functions-in-neural-networks-9491262884e0.
    3Blue1Brown - https://www.youtube.com/watch?v=aircAruvnKk&t=187s&ab_
        channel=3Blue1Brown.
    Paul Ami Jeanbourquin - Clean python advices.
"""

import numpy as np
import numpy.random as rdm
from activation import ActivationFunction as af

class NeuralNetwork:
    """ A deep neural network with a varying number of layersself.

    Args:
        layers (Layer[]): Layers that compose the network.
    """
    def __init__ (self, layers):
        self.layers = layers
        self.weight = NeuralNetwork.initWeight(layers)


    def feedForward(self):
        for i in range(len(self.layers)-1):
            result=self.layers[i+1]
            result.z = self.layers[i].a.dot(self.weight[i]) + result.bias
            result.a = np.matrix(
                [result.activation(x) for x in result.z.A[0]]).transpose()


    def getOutput(self):
        return self.layers[len(self.layers)-1].a.A[0]


    def setInput(self, input):
        if len(input) != self.layers[0].a.shape[1]:
            return None
        self.layers[0].a = np.matrix(input)


    @staticmethod
    def initWeight(layers):
        weight = []
        for i in range(len(layers)-1):
            l1, l2 = layers[i].z.shape[1], layers[i+1].z.shape[1]
            weight.append(np.matrix(np.random.rand(l1, l2)))
        return weight


class Layer:
    """ A layer with neurons, biases and an activation function.

    Args :
        nb_neurons : The number of neurons within that layer.
        random : Wheter or not the biases are initialised, else bias=0 (input).
        bias : If random is true, how strong will the biases be [-bias;bias].
        activation: The activation function of the layer.

    Attributes :
        z : A matrix of float. The value of each neurons within the layer
            before applying the activation function.
        a : A matrix of float. The value of each neurons after the activation
            function has been applied.
        bias : A matrix of float. The bias of each neurons.
        nb_neurons : Number of neurons in the layer.
        activation : The activation function used for this layer.
    """
    def __init__ (self, nb_neuron, *, random=True, bias=1, activation=af.tanh):
        self.z = np.matrix(np.zeros(nb_neuron))
        self.a = np.matrix(np.zeros(nb_neuron))
        self.activation = activation
        self.nb_neurons = nb_neuron
        if random is True:
            self.bias = np.matrix((2*rdm.rand(1, nb_neuron)-1)*bias)
        else:
            self.bias = np.matrix(np.zeros(nb_neuron))


    def __str__ (self):
        accu = "Layer : " +str(self.nb_neurons)+ " neurons\n"
        accu += "Activation function : " + self.activation.__name__ + "\n"
        accu += "Z : " + str(self.z) + "\n"
        accu += "A : " + str(self.a) + "\n"
        accu += "Bias : " + str(self.bias) + "\n"
        return accu


    @staticmethod
    def createLayers(
        neurons_per_layers, *, activation=af.tanh, random=True):
        """ Returns an array of x Layers with y neurons.
            Args:
                neurons_per_layers : An array with a number of neurons for each
                    layers. i.e: [2, 2, 2, 1], 2 inputs, 4 hidden, 1 output
        """
        npl = neurons_per_layers
        layers = [Layer.createInputLayer(npl[0])]
        layers.extend([Layer(
            npl[i], bias=npl[i-1], random=random, activation=activation)
                       for i in range(1, len(npl))])
        return layers


    @staticmethod
    def createInputLayer(nb_neuron):
        """ Creates an input layer, no bullshit."""
        return Layer(nb_neuron=nb_neuron, random=False, activation=af.none)
