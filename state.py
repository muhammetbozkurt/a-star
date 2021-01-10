import itertools
import numpy as np

from copy import deepcopy
from agent import Agent


class State:
    def __init__(self, world, agents : list = list()):
        self.world = deepcopy(world)
        self.agents = deepcopy(agents)
        
        
    def __eq__(self, anotherState):
        
        if(len(self.agents) != len(anotherState.agents)):
            return False
        
        #ayni sira ile tutuluyorlar
        for agent1, agent2 in zip(self.agents,anotherState.agents):
            if(not (agent1 == agent2)):
                return False

        return True

    def findPositions(self):
        rewardsPositions = dict()
        agentsPositons = dict()
        for height in range(len(self.world)):
            for width in range(len(self.world[0])):
                if(self.world[height,width].find("G")>-1):
                    rewardsPositions[self.world[height,width]] = np.array([height, width])
                elif(self.world[height,width].find("A")>-1):
                    agentsPositons[self.world[height,width]] = np.array([height, width])
        
        for key, item in agentsPositons.items():
            self.agents.append(Agent(key, item, rewardsPositions["G"+key[1:]]))
    
    def isSuccesful(self):
        
        for agent in self.agents:
            if(not agent.isSuccesful()):
                return False
            
        return True
    
    def printAgents(self):
        for i in self.agents:
            print(i)
    
    def copy(self):
        return State(self.world, self.agents)

    def nextPosibleMoves(self):
        listOfMoveLists = list()
        for agent in self.agents:
            listOfMoveLists.append(agent.getPosibleMoves(self.world))
        return list(itertools.product(*listOfMoveLists))