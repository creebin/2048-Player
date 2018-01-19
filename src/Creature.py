from Stuff import Brain,Game 
import numpy as np

class Creature(object):
    def __init__(self,inputArray):
        self.brain = Brain.Brain(inputArray)
        self.game = Game.Game()
        self.playGame()
        self.fitness = self.game.getScore()
        
    def playGame(self):
        while not self.game.getGameOver():
            self.game.makeMove(self.brain.decision(self.game.getBoard(True)))
        
    def mutate(self,learningRate):
        self.brain.mutate(learningRate)
        self.playGame()
        self.fitness = self.game.getScore()
            
    def getBrain(self):
        return self.brain
    def getFitness(self):
        return self.fitness
    def getGame(self):
        return self.game
    def setBrain(self,Brain):
        self.brain = Brain
    def setGame(self,game):
        self.game = game