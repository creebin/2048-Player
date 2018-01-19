import numpy as np
from Creature.NeuralNet import NeuralNet


class Brain(NeuralNet):
    def mutate(self):
        for x in range(0,len(self.Weights)):
            for y in range(0,len(self.Weights[x])):
                for z in range(0,len(self.Weights[x][y])):
                    if np.random.random() <.1:
                        self.Weights[x][y][z] += np.random.randn()
        for x in range(0,len(self.Biases)):
            for y in range(0,len(self.Biases[x])):
                for z in range(0,len(self.Biases[x][y])):
                    if np.random.random() <.1:
                        self.Biases[x][y][z] += np.random.randn()
    
    def decision(self, board):
        return self.feedForward(board).argmax()
    
jimmy = Brain([4,4,4])
print("weights!!")
print(jimmy.getWeights())
print("Biasess!!")
print(jimmy.getBiases())

jimmy.mutate()
print("weights!!")
print(jimmy.getWeights())
print("Biasess!!")
print(jimmy.getBiases())
        
    
    