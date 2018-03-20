from dnn import NeuralNetwork

class BackPropagation:
    def __init__(self, *input_data, *solution, neural_network):
        self.input_data = input_date
        self.solution = solution
        self.dnn = neural_network
        self.output = []

    # Co = (a(L) - y)^2
    # z(L) = w(L)*a(L-1) + b(L)
    # a(L) = activ(z(L))

    # Influence de b sur Co
    # delta(Co,b(L)) = delta(z(L),b(L)) * delta(a(L),z(L)) * delta(Co,a(L))

    def initOutput():
        """ Gives every input data to the network and saves the output."""
        for i in range(len(input_data)):
            dnn.layers[0] = input_data[i]
            dnn.feedForward()
            output[i].append(dnn.getOutput())


    def getCost():
        """ Calculate the 'cost', error squared."""
        return np.power(output[self.dnn.getOutput()]-solution[i],2)


    def costDerivate():
        """ Partial derivative of cost over output."""
        return 2*(output-solution)


    def outputDerivate():
        """
        Partial derivative of output over z.
        """
        return derivateOfActivationFunction(z)


    def zDerivateOverWeight():
        """
        Partial derivative of z over weight.
        'z' being: sum(weight(i)*output(i-1)) + bias(i).
        """
        return a(L-1)


    def zDerivateOverBias():
        """
        Partial derivative of z over bias (always 1).
        'z' being: sum(weight(i)*output(i-1)) + bias(i).
        """
        return 1


    def zDerivateOverOutput():
        """
        Partial derivative of z over last output.
        'z' being: sum(weight(i)*output(i-1)) + bias(i).
        """
        return weight(L)

    pass
