# Undirected Adj List
class Graph:
    def __init__(self, adjacency_list=None):
        if adjacency_list is None:
            adjacency_list = {}
        self.al = adjacency_list

    def add_edge(self, v1, v2):
        try:
            self.al[v1].append(v2)
        except KeyError:
            self.al[v1] = [v2]

        try:
            self.al[v2].append(v1)
        except KeyError:
            self.al[v2] = [v1]

    def display_graph(self):
        print(self.al)

    def bfs(self, vertex=0, visited=None):
        if visited is None:
            visited = []
        queue = []
        visited.append(vertex)
        queue.append(vertex)
        while queue:
            temp = queue.pop(0)

            for neighbor in self.al[temp]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.append(neighbor)

        return visited

    def dfs(self, vertex=0, visited=None):
        if visited is None:
            visited = []
        visited.append(vertex)

        for neighbor in self.al[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

        return visited


# Undirected Adj Matrix
class Graph(object):
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for _ in range(size)])
        self.size = size

    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        else:
            self.adjMatrix[v1][v2] = 1
            self.adjMatrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val), end=" ")
            print()

        # With Library (Directed)


import networkx as nx
import matplotlib.pyplot as plt

# Untuk membuat graph dengan nodes dan edge
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 4)
G.add_edge(2, 5)
G.add_edge(3, 6)
G.add_edge(4, 7)

print("Nodes:", G.nodes())
print("Edges:", G.edges())

# Ngeplot graphnya
nx.draw(G, with_labels=True)
plt.show()

# Ngeprint secara BFS
bfs_result = list(nx.bfs_edges(G, source=1))
print("BFS Traversal:", bfs_result)

# Ngeprint secara DFS
dfs_result = list(nx.dfs_edges(G, source=1))
print("DFS Traversal:", dfs_result)
