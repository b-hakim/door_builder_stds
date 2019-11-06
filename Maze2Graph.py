# todo: get a map as input, transform the map to a graph based on BFS algorithm.
#       For each edge calculate the cost and for each node, calculate the Heuristic
from Maze import MazeCellType


class Maze2Graph:
    def __init__(self, maze_2d, cell_size):
        self.maze = maze_2d
        self.cell_size = cell_size

    def transform2Graph(self):
        graph_nodes = [[row, col] for row in range(len(self.maze)) for col in range(len(self.maze[row]))
                 if self.maze[row][col] == MazeCellType.DOOR]
        start = [[row, col] for row in range(len(self.maze)) for col in range(len(self.maze[row]))
                 if self.maze[row][col] == MazeCellType.START_DOOR][0]
        target = [[row, col] for row in range(len(self.maze)) for col in range(len(self.maze[row]))
                 if self.maze[row][col] == MazeCellType.TARGET_DOOR][0]

        graph_nodes.insert(0, start)
        graph_nodes.append(target)

        graph_edges = []

        for i in range(len(graph_nodes)):
            graph_edges.append([])

        ## Student Code: Build Graph,
        # for each node,
        #   find the reachable doors. Hint: use DFS on the given array
        #   Add an edge between the current node and each reachable doors
        #
        #
        #
        ##############################################################

        ## Output for Test Case: debugging_level.lvl
        # Comment/remove this line when you are done
        return graph_nodes, [[2], [2, 3], [0, 1], [1]]
        #########################################################################################

        return graph_nodes, graph_edges
