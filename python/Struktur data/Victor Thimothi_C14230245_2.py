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

    def find_bridges(self):
        visited = set()
        disc = {}  # menyimpan waktu sebuah node ditemukan
        low = {}   # waktu terendah yang dapat dicapai suatu node
        parent = {}  # menyimpan setiap parent dari node
        bridges = []  # menyimpan semua bridge yang ditemukan
        time = [0]  # untuk melacak waktu berjalan saat DFS

        # Inisialisasi DFS untuk setiap komponen terpisah dalam graf
        for vertex in self.al:
            if vertex not in visited:
                self.dfs_bridge(vertex, visited, disc, low, parent, bridges, time)

        return bridges

    def dfs_bridge(self, u, visited, disc, low, parent, bridges, time):
        # Tandai node sebagai dikunjungi dan catat waktu discovery
        visited.add(u)
        disc[u] = low[u] = time[0]
        time[0] += 1

        # Kunjungi semua tetangga dari u
        for v in self.al[u]:
            if v not in visited:  # Jika v belum dikunjungi
                parent[v] = u
                self.dfs_bridge(v, visited, disc, low, parent, bridges, time)

                # Perbarui low-link value dari u
                low[u] = min(low[u], low[v])

                # Jika low[v] > disc[u], maka (u, v) adalah bridge
                if low[v] > disc[u]:
                    bridges.append((u, v))

            elif v != parent.get(u):  # Jika v sudah dikunjungi dan bukan parent u
                low[u] = min(low[u], disc[v])


graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 0)
graph.add_edge(2, 0)
graph.add_edge(0, 3)
graph.add_edge(3, 4)
graph.display_graph()
bridges = graph.find_bridges()
print("Bridge(s) di graf:", bridges)