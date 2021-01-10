import numpy as np
from enum import IntEnum


HEIGHT, WIDTH = 0,0
def readInputs(fileName : str = "test.txt"):
    global HEIGHT, WIDTH
    data = open(fileName,"r")
    HEIGHT, WIDTH, numOfAgent = [int(info) for info in data.readline().split()]
    data = [[j for j in i.split()] for i in data.read().split("\n")]
    return np.array(data)


class Action(IntEnum):
    UP = 1
    DOWN = -1
    LEFT = 3
    RIGHT = -3
    PASS = 0

def action2Str(action : Action):
    if(action == Action.UP):
        return "U"
    if(action == Action.DOWN):
        return "D"
    if(action == Action.RIGHT):
        return "R"
    if(action == Action.LEFT):
        return "L"
    if(action == Action.PASS):
        return "P"
