import numpy as np

class Game(object):     
    
    def __init__(self):        
        self.numberOfZeros = 16
        self.board = np.zeros((4,4))        
        self.gameOver = False   
        self.score = 0
        self.giveRandomTile()
        self.giveRandomTile()         
        
    def moveLeft(self):
        for j in range(0,4):
            i = 0
            i2 = i+1
            while i < 4:
                if self.board[j,i2] == 0:
                    i2 += 1
                elif self.board[j,i] == 0:
                    self.board[j,i] = self.board[j,i2]
                    self.board[j,i2] = 0 
                    i2 = i+2
                elif self.board[j,i] != self.board[j,i2]:
                    i += 1
                    i2 = i+1
                else: 
                    self.score += 2*self.board[j,i]
                    self.board[j,i] = 2*self.board[j,i]
                    self.board[j,i2] = 0 
                    self.numberOfZeros += 1
                    i += 1
                    i2 = i+1
                if i2 > 3:
                    break 
                
    def moveRight(self):
        for j in range(0,4):
            i = 3
            i2 = i-1
            while i < 4:
                if self.board[j,i2] == 0:
                    i2 -= 1
                elif self.board[j,i] == 0:
                    self.board[j,i] = self.board[j,i2]
                    self.board[j,i2] = 0 
                    i2 = i-2
                elif self.board[j,i] != self.board[j,i2]:
                    i -= 1
                    i2 = i-1
                else :
                    self.score += 2*self.board[j,i]
                    self.board[j,i] = 2*self.board[j,i]
                    self.board[j,i2] = 0 
                    self.numberOfZeros += 1
                    i -= 1
                    i2 = i-1
                if i2 < 0:
                    break 
                
    def moveUp(self):
        for j in range(0,4):
            i = 0
            i2 = i+1
            while i < 4:
                if self.board[i2,j] == 0:
                    i2 += 1
                elif self.board[i,j] == 0:
                    self.board[i,j] = self.board[i2,j]
                    self.board[i2,j] = 0 
                    i2 = i+2
                elif self.board[i,j] != self.board[i2,j]:
                    i += 1
                    i2 = i+1
                else:
                    self.score += 2*self.board[i,j]
                    self.board[i,j] = 2*self.board[i,j]
                    self.board[i2,j] = 0 
                    self.numberOfZeros += 1
                    i += 1
                    i2 = i+1
                if i2 > 3:
                    break 
        
    def moveDown(self):
        for j in range(0,4):
            i = 3
            i2 = i-1
            while i < 4:
                if self.board[i2,j] == 0:
                    i2 -= 1
                elif self.board[i,j] == 0:
                    self.board[i,j] = self.board[i2,j]
                    self.board[i2,j] = 0 
                    i2 = i-2
                elif self.board[i,j] != self.board[i2,j]:
                    i -= 1
                    i2 = i-1
                else:
                    self.score += 2*self.board[i,j]
                    self.board[i,j] = 2*self.board[i,j]
                    self.board[i2,j] = 0 
                    self.numberOfZeros += 1
                    i -= 1
                    i2 = i-1
                if i2 < 0:
                    break 
        
    def giveRandomTile(self):
        if self.numberOfZeros == 0: 
            self.gameOver = True
            return
        currentTileNumber = 0
        newTileNumber = np.random.randint(0,self.numberOfZeros)
        for i in range(0,4):
            for j in range(0,4):
                if self.board[i,j] == 0:
                    if currentTileNumber == newTileNumber:
                        self.board[i,j] = 2
                        self.numberOfZeros -= 1
                        return 
                    else:
                        currentTileNumber += 1
    
                        
    def getNumberOfZeros(self):
        return self.numberOfZeros
    def getBoard(self, lessThanOne = None):
        if lessThanOne:   
            output = []
            for y in self.board:
                for x in y:                    
                    output.append(x)
            return output/np.amax(self.board)
        else:
            return self.board
    def getGameOver(self):
        return self.gameOver
    def getScore(self):
        return self.score
    
    def setNumberOfZeros(self,inputZeros):
        self.numberOfZeros = inputZeros
    def setBoard(self, inputBoard):
        self.board = inputBoard
    def setGameOver(self,inputGameOver):
        self.gameOver = inputGameOver
    def setScore(self,inputScore):
        self.score = inputScore
        
    def makeMove(self,input):
        if self.gameOver: return
        if input == 0:
            self.moveUp()
            self.giveRandomTile()
        elif input == 1:
            self.moveDown()
            self.giveRandomTile()            
        elif input == 2:
            self.moveLeft()
            self.giveRandomTile()
        elif input == 3:
            self.moveRight()
            self.giveRandomTile()
        else:
            print("Something messed up!!")
            
    def reset(self):        
        self.numberOfZeros = 16
        self.board = np.zeros((4,4))        
        self.gameOver = False   
        self.score = 0
        self.giveRandomTile()
        self.giveRandomTile()      
                
                

        

