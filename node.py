from copy import deepcopy
from state import State
from utils import Action

class Node:
    def __init__(self,state : State, actionTaken : tuple = None , parentNode = None, actionNum : int = 0):#actionTaken can be converted to str
        self.parentNode = parentNode
        self.state = state.copy()
        self.actionTaken = deepcopy(actionTaken)
        self.actionNum = actionNum
    
    def createChildren(self):
        allPosiblemoves = self.state.nextPosibleMoves()
        self.children = list()
        if(self.actionTaken is not None):
            reverseMove = tuple(map(lambda x: Action(x * -1), self.actionTaken))
        
        for moves in allPosiblemoves:
            if((self.actionTaken is not None) and (moves == reverseMove)):
                continue
            if(moves == (Action.PASS, Action.PASS)):
                continue

            canActionTaken = True
            state = self.state.copy()
            for action, agent in zip(moves, self.state.agents):
                indexOfAgent = self.state.agents.index(agent)
                tempAgent = deepcopy(agent)
                canActionTaken = tempAgent.move(action, state.world) and canActionTaken
                tempAgent.isSuccesful()
                state.agents[indexOfAgent] = tempAgent

            
            if(canActionTaken):
                self.children.append(Node(state, moves, self, self.actionNum + 1))
    
        return self.children

    def isSuccesful(self):
        return self.state.isSuccesful()
                
    def __str__(self):
        return "-----------------" +\
                f"Parent: {id(self.parentNode)}\n"+ \
                f"succes: {self.isSuccesful()}\n" +\
                f"action: {self.actionTaken}\n" + \
                f"agents: {self.state.agents}\n" + \
                "-----------------"
    
    def __eq__(self, other):
        return self.state == other.state and self.actionTaken == other.actionTaken

    def heuristic(self):
        """
        first find total distace
        after finding total ddistance divide it to number of non succesful agents
        to find aprox number of moves to finish per not succesful agent
        """
        totalDist = 0
        notSucces = 0
        for agent in self.state.agents:
            if(not agent.isSuccesful()):
                notSucces += 1
                totalDist += agent.distance() 
        notSucces = notSucces if(notSucces != 0) else 1
        return int(totalDist)

    def __lt__(self, other):
        """
        action number to reach this node + heuristic 
        this function is evaluated when node put into priorityQueue
        """
        return self.heuristic() + self.actionNum < other.heuristic() + other.actionNum