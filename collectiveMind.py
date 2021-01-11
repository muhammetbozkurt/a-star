import numpy as np
import time

from state import State
from node import Node
from utils import *
from queue import PriorityQueue


class CollectiveMind:
    def __init__(self, fileName : str):
        self.initialWorld = self.readInputs(fileName)
        self.initialState = State(self.initialWorld)
        self.initialState.findPositions()
        self.initialNode = Node(self.initialState)
    
    def readInputs(self, fileName):
        global HEIGHT, WIDTH
        data = open(fileName,"r")
        HEIGHT, WIDTH, numOfAgent = [int(info) for info in data.readline().split()]
        data = [[j for j in i.split()] for i in data.read().split("\n")]
        return np.array(data)

    def path(self, node:Node, outputFileName : str = "output.txt"):
        moves = list()
        
        
        while(node.parentNode is not self.initialNode):
            moves.append(node.actionTaken)
            node = node.parentNode
        moves.append(node.actionTaken)
        moves.reverse()

        numOfAgents = len(node.state.agents)
        indexes = list()
        for i in range(1,numOfAgents+1):
            agentName = f"A{i}"
            for j in range(numOfAgents):
                if(node.state.agents[j].name == agentName):
                     indexes.append(j)
        
        file = open(outputFileName ,"w")
        file.write(f"{len(moves)} {numOfAgents}\n")

        for move in moves:
            line = ""
            for i in range(numOfAgents):
                #line = line + f"{action2Str(move[indexes[i]])}" if(i == 0) else  line + f" {action2Str(move[indexes[i]])}"
                line = line + f"{action2Str(move[indexes[i]])}"
            file.write(line + "\n")

        return moves


        
    
    def bfs(self):
        start_time = time.time()
        frontier= list()
        seen = list()
        pathFound = False
        i = 0
        numberOfTotalGeneratedNode = 1
        maxNodeKept = 0 

        frontier.append(self.initialNode)
        while(frontier and not pathFound):
            s = frontier.pop(0) 
            
            neighbours = s.createChildren()
            numberOfTotalGeneratedNode += len(neighbours)

            for neighbour in neighbours:
                maxNodeKept = max(len(frontier), maxNodeKept)
                if(neighbour in seen):
                    continue
                seen.append(neighbour)
                pathFound = neighbour.isSuccesful()
                i += 1
                if(pathFound):
                    print("Number of nodes generated ",numberOfTotalGeneratedNode)
                    print("Number of nodes expanded ",i)
                    print("Maximum number of nodes kept in the memory ", maxNodeKept)
                    print("Running time ", time.time() - start_time," seconds\n")
                    return neighbour
                frontier.append(neighbour)
        return False

            

    def dfs(self):
        start_time = time.time()
        frontier= list()
        seen = list()
        pathFound = False
        i = 0
        numberOfTotalGeneratedNode = 1
        maxNodeKept = 0

        frontier.append(self.initialNode)
        while(frontier and not pathFound):
            s = frontier.pop(0) 
            
            neighbours = s.createChildren()
            numberOfTotalGeneratedNode += len(neighbours)
            for neighbour in neighbours:
                maxNodeKept = max(len(frontier), maxNodeKept)
                if(neighbour in seen):
                    continue
                seen.append(neighbour)
                pathFound = neighbour.isSuccesful()
                i += 1

                if(pathFound):
                    print("Number of nodes generated ",numberOfTotalGeneratedNode)
                    print("Number of nodes expanded ",i)
                    print("Maximum number of nodes kept in the memory ", maxNodeKept)
                    print("Running time ", time.time() - start_time," seconds")
                    return neighbour
                frontier.insert(0,neighbour)
        return False
    
    def aStar(self):
        start_time = time.time()
        frontier= PriorityQueue()
        seen = list()
        pathFound = False
        i = 0
        numberOfTotalGeneratedNode = 1
        maxNodeKept = 0 
        lenOfFrontier = 1

        frontier.put(self.initialNode)
        
        while(frontier and not pathFound):
            s = frontier.get()
            lenOfFrontier -= 1
            neighbours = s.createChildren()
            numberOfTotalGeneratedNode += len(neighbours)

            for neighbour in neighbours:
                maxNodeKept = max(lenOfFrontier, maxNodeKept)
                if(neighbour in seen):
                    continue
                seen.append(neighbour)
                pathFound = neighbour.isSuccesful()
                i += 1
                if(pathFound):
                    print("Number of nodes generated ",numberOfTotalGeneratedNode)
                    print("Number of nodes expanded ",i)
                    print("Maximum number of nodes kept in the memory ", maxNodeKept)
                    print("Running time ", time.time() - start_time," seconds")
                    return neighbour
                lenOfFrontier += 1
                frontier.put( neighbour)
        return False