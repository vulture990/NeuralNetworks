#it ll be more neat and organized to treat the activation function as a layer

from layer import Layer
import numpy as np

class Activation(layer):
    def __init__(self, activation,activation_prime):
        self.activation=activation
        self.activation_prime=activation_prime

    def forward(self,input):
        self.input=input
        return self.activation(self.input)
    def backward(self,output_gradient,learning_rate):
        return np.multiply(output_gradient,self.activation_prime(self.input))
        ##multiply by element


