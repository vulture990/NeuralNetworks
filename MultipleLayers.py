#Y= W*X +B ; Y as the output ,W the weight matrice,B the biases coloumn


"""
E:error
From the forward propagation system of equations and the chain rule
 caluculus we can easily deduce equation to adjust factors for backpropagation:


Equation for the backpropagation goes like this:


 (1) ∂E/∂W=∂E/∂Y * X.transposed
 (2) ∂E/∂B=∂E/∂Y
 (3)∂E/∂X= W.transposed * ∂E/∂y

"""

from layer import Layer
import numpy as np
class MultipleLayers(Layer):
    def __init__(self,input_size,output_size):
        #constructor generate random weights and biases columns at first hand
        self.w=np.random.randn(output_size,input_size)
        self.b=np.random.randn(output_size,1)

    def forward(self, input):
        self.input=input
        return np.dot(self.w,self.input)

    def backward(self, output_gradient, learning_rate):
        pass  
