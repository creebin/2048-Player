import numpy as np

class NeuralNet(object):
    
    
    def __init__(self,array):
        self.Weights = [np.random.random((row,col)) for row,col in zip(array[:-1],array[1:])]
        self.Biases = [np.random.random((1,col)) for col in array[1:]]
        
    
    def feedForward(self, inputt, weight= None, bias = None):
        if weight is not None:
            output = inputt
            for w,b in zip(weight,bias):
                output = sigmoid(np.dot(output,w)+b)
            return output
        else:
            output = inputt
            for w,b in zip(self.Weights,self.Biases):
                output = sigmoid(np.dot(output,w)+b)
            return output
        
    def backPropogate(self):
        
    def getWeights(self):
        return self.Weights
    
    def getBiases(self):
        return self.Biases
    
        
def sigmoid(a):
    return 1/(1+np.exp(a)) 
    
