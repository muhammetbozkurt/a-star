from pygame.locals import *
import pygame
import sys
import numpy as np
import os

from collectiveMind import CollectiveMind
from node import Node

from time import sleep

class Visalizer(CollectiveMind):

    def __init__(self, fileName):
        super().__init__(fileName)
        self.windowHeight = (len(self.initialNode.state.world)) * 50
        self.windowWidth = (len(self.initialNode.state.world[0])) * 50
        
    
    def on_init(self, node : Node):
        pygame.init()
        self.displaySurf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        
        numberOfAgents = len(node.state.agents)

        #there could be more than one agent so we need more than one image for agents and goals
        self.agentImages = []
        self.goalImages = []
        
        agents = os.listdir("agents")
        goals = os.listdir("goals") 
        for i in range(numberOfAgents):
            print(f"agents/{agents[i]}")
            img = pygame.image.load(f"agents/{agents[i]}").convert()
            img = pygame.transform.scale(img, (50,50))
            self.agentImages.append(img)

            print(f"goals/{goals[i]}")
            img = pygame.image.load(f"goals/{goals[i]}").convert()
            img = pygame.transform.scale(img, (50,50))
            self.goalImages.append(img)

        self.block = pygame.image.load("block.png").convert()
        self.block = pygame.transform.scale(self.block, (50,50))
    
        pygame.display.set_caption('Pygame pythonspot.com example')

        self.pathNodes = []

        while(node is not self.initialNode):
            self.pathNodes.append(node)
            node = node.parentNode
        self.pathNodes.append(node)

        self.pathNodes.reverse()

    
    def draw(self, state):
        #state = self.pathNodes[0].state.world

        #draw walls
        walls = np.where(state.world == 'W')
        for y,x in zip(walls[0], walls[1]):
            self.displaySurf.blit(self.block,( x * 50 , y * 50))
        
        #draw agents and goals
        agents = state.agents
        for i in range(len(agents)):
            if(not agents[i].succesful):
                y, x = agents[i].reward[0] * 50, agents[i].reward[1] * 50
                self.displaySurf.blit(self.goalImages[i], (x, y))

            y, x = agents[i].position[0] * 50, agents[i].position[1] * 50
            self.displaySurf.blit(self.agentImages[i], (x, y))

    def visualize(self):
        i = 0
        for node in self.pathNodes:
            state = node.state
            self.displaySurf.fill((255, 255, 255))
            self.draw(state)
            pygame.display.flip()
            pygame.image.save(self.displaySurf,f"saves/{i}.png")
            sleep(0.5)
            i += 1




def main():
    mind = Visalizer(sys.argv[1])
    a = mind.aStar()
    mind.on_init(a)
    mind.visualize()
    
if __name__ == "__main__":
    main()
    