# a-star

![Figure 1](https://github.com/muhammetbozkurt/a-star/blob/main/gifs/2.gif)


The problem of reaching the targets of different agents collectively was implemented using the a star algorithm. There are implemetions of problem using DFS and BFS but they are inactive for now. Initial states given program as command line argument. Example inputs are given in [inputs](https://github.com/muhammetbozkurt/a-star/blob/main/gifs/2.gif) folder.

Our agents can move to up, down, right, left one cell if that cell is empty. I determined state as how map look like after necessary action taken, it includes map, agents’ positions and rewards’ positions.
It may seems like odd to you that agent moves after they reach their rewards. However, it is necessary for some example and give more flexibility to collective mind. Aim of the program is all agents reaching their rewards and doing this in least amount of time. Total manhattan distance and total euclidean distance was used as heuristic function for testing. Total manhattan distance was used in finale version because after comparing them, the total manhattan distance function being more suitable than the total euclidean distance for our problem was easily noticed. It needs to generate nodes almost half of euclidean distance one. Moreover, it is way faster. I think main reason is total manhattan distance is more close to the number of moves that are required to reach goal state.



To run and visualize output:

    python visualize.py filename

To run and just get directions to finish map:

    python testCollectiveMind.py filename

output file will be output.txt or

    python testCollectiveMind.py filename output.txt


Some visualized examples:

![Figure 2](https://github.com/muhammetbozkurt/a-star/blob/main/gifs/1.gif)


![Figure 3](https://github.com/muhammetbozkurt/a-star/blob/main/gifs/3.gif)


![Figure 4](https://github.com/muhammetbozkurt/a-star/blob/main/gifs/0.gif)


![Figure 5](https://github.com/muhammetbozkurt/a-star/blob/main/gifs/4.gif)
