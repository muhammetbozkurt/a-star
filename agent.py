from utils import *


class Agent:

    def __init__(self, name = "", position = None, rewardPosition = None, succesful:bool = False):
        self.name = name
        self.position = position.copy()
        self.reward = rewardPosition.copy()
        self.succesful = succesful
        self.rewardName = "G" + self.name[1:]
    
    def getPosibleMoves(self, world):
        #if(self.succesful):
        #    return [Action.PASS]
        posibleMoves =  list()

        nextPos = self.position + np.array([-1,0])
        height = len(world)
        width  = len(world[0])
        if(nextPos[0]>=0 and (world[tuple(nextPos)] == "E" or world[tuple(nextPos)] == self.rewardName ) ):
            posibleMoves.append(Action.UP)
            
        nextPos = self.position + np.array([1,0])
        if(nextPos[0]<height and (world[tuple(nextPos)] == "E" or world[tuple(nextPos)] == self.rewardName )):
            posibleMoves.append(Action.DOWN)
            
        nextPos = self.position + np.array([0,1])
        if(nextPos[1]<width and (world[tuple(nextPos)] == "E" or world[tuple(nextPos)] == self.rewardName )):
            posibleMoves.append(Action.RIGHT)
        
        nextPos = self.position + np.array([0,-1])
        if(nextPos[1]>=0 and (world[tuple(nextPos)] == "E" or world[tuple(nextPos)] == self.rewardName )):
            posibleMoves.append(Action.LEFT)
        
        posibleMoves.append(Action.PASS)
        
        return posibleMoves
    
    def move(self, action : Action, world):
        nextPos = np.array([0,0])
        if(action == Action.UP ):
            nextPos = self.position + np.array([-1,0])
        elif(action == Action.DOWN):
            nextPos = self.position + np.array([1,0])
        elif(action == Action.RIGHT):
            nextPos = self.position + np.array([0,1])
        elif(action == Action.LEFT):
            nextPos = self.position + np.array([0,-1])
        else:
            return True

        if(world[tuple(nextPos)] == "E" or world[tuple(nextPos)] == self.rewardName):
            world[tuple(self.position)] = "E"
            self.position = nextPos
            world[tuple(self.position)] = self.name
            return True
        else:
            return False
    
    def isSuccesful(self):
        if(self.succesful == True):
            return True
        self.succesful = np.all(self.position == self.reward)
        return self.succesful
    
    def __eq__(self, anotherAgent):
        return np.all(self.position == anotherAgent.position) and self.name == anotherAgent.name and self.succesful == anotherAgent.succesful
    
    def __str__(self):
        return f"-----------------\nName: {self.name}\npos: {self.position}\n"+ \
                f"goal: {self.reward}\nsucces: {self.isSuccesful()}\n-----------------"
    
    def distance(self):
        """
        Manhattan distance
        """
        return sum(abs(self.position - self.reward))

    def distaceEuclid(self):
        """
        Euclidian Distance
        """
        return np.linalg.norm(self.position - self.reward)