from enum import Enum
from Maze2Graph import Maze2Graph


class GraphAlgorithm(Enum):
    ASTAR = 1,
    DIJKSTRA = 2


class Graph:
    def __init__(self, maze, algorithm_type):
        self.graph_nodes, self.graph_edges = Maze2Graph(maze.maze_cells, maze.cell_size).transform2Graph()
        self.graph_algorithm = algorithm_type

    def find_shortest_path(self):
        ## Path for the debugging_level.lvl
        # remove this line when running your code.
        return [self.graph_nodes[0], self.graph_nodes[2], self.graph_nodes[1], self.graph_nodes[3]]
        ########################

        if self.graph_algorithm == GraphAlgorithm.ASTAR:
            return self.__run_astar()

        if self.graph_algorithm == GraphAlgorithm.DIJKSTRA:
            return self.__run_dijkstra()

    def __run_astar(self):
        pass

    def __run_dijkstra(self):
        pass

