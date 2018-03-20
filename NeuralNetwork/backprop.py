from dnn import NeuralNetwork
import numpy as np

# Work in progress...

class BackPropagation:
    """
    Co = (a(L) - y)^2
    z(L) = w(L)*a(L-1) + b(L)
    a(L) = activ(z(L))
    Influence de b sur Co
    deriv(Co,b(L)) = deriv(z(L),b(L)) * deriv(a(L),z(L)) * deriv(Co,a(L))
    """
    def __init__(self, neural_network, input_data=[], solution=[]):
        self.input_data = np.array(input_data).astype(float)
        self.solution = np.array(solution).astype(float)
        self.output = np.empty_like(self.solution)
        self.dnn = neural_network


    def __str__(self):
        """ A simple display for small input/output/solution."""

        accu = "BackPropagation Object: " + str(len(self.input_data[0]))
        accu +=  " input(s), " + str(len(self.output[0])) + " output(s).\n"

        accu += "Input data:\n"
        for i in range(len(self.input_data)):
            accu += (str(i) + ": " + str(self.input_data[i]) + "\n")

        accu += "Output data:\n"
        for i in range(len(self.output)):
            accu += (str(i) + ": " + str(self.output[i]) + "\n")

        accu += "Solution:\n"
        for i in range(len(self.solution)):
            accu += (str(i) + ": " + str(self.solution[i]) + "\n")

        return accu


    def initOutput(self):
        """ Gives every input data to the network and saves the output."""
        for i in range(len(self.input_data)):
            self.dnn.layers[0] = self.input_data[i]
            self.dnn.feedForward()
            self.output[i] = self.dnn.getOutput()


    def getCost(self):
        """ Calculate the 'cost', error squared."""
        return np.power(output[i]-solution[i],2)


    def costDerivate(self):
        """ Partial derivative of cost over output."""
        return 2*(self.solution -self.output)


    def outputDerivate(self):
        """
        Partial derivative of output over z.
        """
        return derivateOfActivationFunction(z)


    def zDerivateOverWeight(self):
        """
        Partial derivative of z over weight.
        'z' being: sum(weight(i)*output(i-1)) + bias(i).
        """
        return a(L-1)


    def zDerivateOverBias(self):
        """
        Partial derivative of z over bias (always 1).
        'z' being: sum(weight(i)*output(i-1)) + bias(i).
        """
        return 1


    def zDerivateOverOutput(self):
        """
        Partial derivative of z over last output.
        'z' being: sum(weight(i)*output(i-1)) + bias(i).
        """
        return weight(L)

    pass
