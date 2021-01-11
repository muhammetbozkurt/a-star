import sys
from collectiveMind import CollectiveMind


def main():
    mind = CollectiveMind(sys.argv[1])
    a = mind.aStar()
    if(len(sys.argv)<3):
        mind.path(a)
    else:
        mind.path(a, sys.argv[2])

        
if __name__ == "__main__":
    main()