import numpy as np

class ActivationFunction:
    """ A set of activation funcitons used by NeuralNetwork class."""
    @staticmethod
    def sigmoid(*values, derivate=False):
        if derivate is True:
            return [(np.exp(-x))/ float(np.power(1+np.exp(-x), 2))
                    for x in values]
        return [1/float(1+np.exp(-x)) for x in values]

    @staticmethod
    def tanh(*values, derivate=False):
        if derivate is True:
            return [1/float(np.power(np.cosh(x),2)) for x in values]
        return [np.tanh(x) for x in values]

    @staticmethod
    def softmax(*values, derivate=False):
        if derivate is True:
            print("(Softmax) This function has no derivative "+
                  " asigned to it for now.")
            return 1
        return np.exp(values) / float(sum(np.exp(values)))

    @staticmethod
    def relu(*values, derivate=False):
        if derivate is True:
            return [ 0 if x<0 else 1 for x in values]
        return [np.maximum(0, x) for x in values]

    @staticmethod
    def none(*values, derivate=False):
        if derivate is True:
            return [1 for x in values]
        return values
