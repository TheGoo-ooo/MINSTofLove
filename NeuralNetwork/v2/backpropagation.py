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
from dnn import Layer
from activation import ActivationFunction as af

class BackPropagation:
    def __init__ (self, dnn, input, solution):
        self.dnn = dnn
        self.bpLayers = BackPropagation.initBackPropLayer(dnn)
        self.input = np.matrix(input)
        self.solution = np.matrix(solution)


    def propagate(self):
        i=0

        j=len(self.bpLayers)-1

        self.dnn.setInput(self.input[i])
        self.dnn.feedForward()

        self.bpLayers[j].a = self.pDerivCostToA(i)
        while(j>0):
            self.bpLayers[j].z = self.pDerivAToZ(j+1)
            self.bpLayers[j].bias = self.pDerivZToB(j+1)#* z * al(last)
            self.bpLayers[j-1].a = self.pDerivZToNextA(j+1)#* z * al(laast)
            j-=1
        self.bpLayers[j].z = self.pDerivAToZ(j+1)


    def pDerivCostToA(self, i):
        return np.matrix(2*(self.dnn.getOutput() - self.solution.A[i]))


    def pDerivAToZ(self, i):
        layer = self.dnn.layers[i]
        return np.matrix(layer.activation(layer.z.A[0]))


    def pDerivZToNextA(self, i):
        bias = self.dnn.weight[i-1]
        return (bias.sum(axis=1, dtype='float')/len(bias.A[0])).transpose()


    def pDerivZToB(self, i):
        layer = self.dnn.layers[i]
        return np.matrix( np.full((1,len(layer.bias.A[0])),1) )


    def pDerivZToW(self, i):
        # Each weight is a special snowflake!
        pass



    @staticmethod
    def initBackPropLayer(dnn):
        neurons_per_layers = []
        for i in range(len(dnn.layers)-1):
            neurons_per_layers.append(dnn.layers[i+1].nb_neurons)

        bpLayers = Layer.createLayers(
            neurons_per_layers, activation=af.none, random=False)
        return bpLayers
