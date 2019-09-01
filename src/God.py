import Creature as cr
import numpy as np
import copy
from Creature import Creature

def creatureSort(creatureList):    
    sortThis = [(creatureList[x],creatureList[x].getFitness()) for x in range(0,len(creatureList))]
    for x in range(0,len(sortThis)-1):
        maxFIndex = x
        for y in range(x,len(sortThis)):
            if sortThis[maxFIndex][1] < sortThis[y][1]:
                maxFIndex = y
            if maxFIndex != x :  swap(sortThis, maxFIndex, x)
            
        output = []
        for x in range(0,len(sortThis)):
            output.append(sortThis[x][0])
        return output
    
def swap(array,index1,index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def newPopulation(creatures,learningRate, savePercent):
    newCreatures = []
    maxPop = len(creatures)
    cNum = int(savePercent*maxPop/100)+1
    for x in range(0,cNum):
        newCreatures.append(creatures[x])
        creatureTemp = copy.deepcopy(creatures[x])
        creatureTemp.mutate(learningRate)
        newCreatures.append(creatureTemp)
    cNum += cNum-2
    gradientFactor = .9
    while len(newCreatures) < maxPop:
        if np.random.random() < (cNum/maxPop)*gradientFactor:
            newCreatures.append(creatures[x])
            creatureTemp = copy.deepcopy(creatures[x])
            creatureTemp.mutate(learningRate)
            newCreatures.append(creatureTemp)
            cNum += 2
        if cNum > maxPop:
            creatureTemp = copy.deepcopy(creatures[0])
            creatureTemp.mutate(learningRate)
            newCreatures.append(creatureTemp)
        cNum += 1
    return newCreatures
    
def printMaths(creatures,choice):
    if choice == 1:
        print("Highest Score: ")
        print(creatures[0].getGame().getScore())
    elif choice == 2:
        scores = [creatures[x].getGame().getScore() for x in range(0,len(creatures))]
        print("Average Score: ")
        print(np.average(scores))
    elif choice == 3:
        print("Best Stuff's Board: ")
        print(creatures[0].getGame.getBoard())
    else:
        print("Highest Score: ")
        print(creatures[0].getGame().getScore())
        scores = [creatures[x].getGame().getScore() for x in range(0,len(creatures))]
        print("Average Score: ")
        print(np.average(scores))
        print("Best Stuff's Board: ")
        print(creatures[0].getGame().getBoard())
        print("Best Stuff's Decisions")
        print(creatures[0].getBrain().feedForward((creatures[0].getGame().getBoard(True))))
        print("Worst Stuff's Decisions")
        print(creatures[999].getBrain().feedForward((creatures[0].getGame().getBoard(True))))
          
    
    
    
def runItAllBobby(brainArray,populationSize,learningRate,iterations):
    population = []
    for i in range(0,populationSize):
        population.append(cr.Creature(brainArray))    
    for i in range(0,iterations):
        population = creatureSort(population)
        printMaths(population,5)        
        population = newPopulation(population,learningRate,10)
        
        
runItAllBobby([16,32,16,4],10000,5,1000000)