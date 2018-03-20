from dnn import NeuralNetwork
import numpy as np

# Work in progress...

class BackPropagation:
    """
    Back propagation using partial derivatives.
    ---------------------------------------------
    Co: costFunction
    y: solution
    a(L): partial derivative of a neuronself.
    w(L): weight
    b(L): bias
    L: a given layer from 0 to n
    ---------------------------------------------
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
        self.cost = []
        # d: derivative
        self.da = []
        self.db = []
        self.dw = []


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


    def initAll(self):
        self.initOutput()
        self.initCost()
        self.initDa()
        self.initDb()
        self.initDw()


    def initOutput(self):
        """ Gives every input data to the network and saves the output."""
        for i in range(len(self.input_data)):
            self.dnn.layers[0] = self.input_data[i]
            self.dnn.feedForward()
            self.output[i] = self.dnn.getOutput()


    def initCost(self):
        self.cost = self.getCost()


    def initDa(self):
        self.da = np.delete(np.empty_like(self.dnn.layers), 0)
        for i in range(0, len(self.da)):
            self.da[i] = np.zeros(len(self.dnn.layers[i+1]))


    def initDb(self):
        self.db = np.empty_like(self.dnn.bias)
        for i in range(0, len(self.db)):
            self.db[i] = np.zeros(len(self.dnn.bias[i]))


    def initDw(self):
        self.dw = np.empty_like(self.dnn.weights)
        for i in range(0, len(self.dw)):
            self.dw[i] = np.empty_like(self.dnn.weights[i])
            for j in range(0, len(self.dw[i])):
                self.dw[i][j] = np.zeros(len(self.dnn.weights[i][j]))


    def getCost(self):
        """ Calculate the 'cost', error squared."""
        return np.array([np.power(self.output[i]-self.solution[i],2)
                for i in range(len(self.solution))])


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
