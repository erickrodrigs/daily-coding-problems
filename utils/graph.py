from queue import Queue


class Graph:
    def __init__(self):
        self.graph = dict()

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = list()

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.graph[u].append(v)
        self.graph[v].append(u)

    def vertices(self):
        return self.graph.keys()

    def edges(self):
        all_edges = set()

        for v in self.vertices():
            for u in self.graph[v]:
                if (u, v) not in all_edges and (v, u) not in all_edges:
                    all_edges.add((v, u))

        return list(all_edges)

    def bfs(self):
        visited = dict()

        for vertex in self.graph.keys():
            visited[vertex] = False

        queue = Queue()
        queue.put(self.graph.keys()[0])

        while not queue.empty():
            v = queue.get()
            visited[v] = True
            adjacents = self.graph[v]

            for adj in adjacents:
                if not visited[adj]:
                    queue.put(adj)

    def dfs(self):
        def dfs_helper(vertex, visited):
            visited[vertex] = True
            adjacents = self.graph[vertex]

            for adj in adjacents:
                if not visited[adj]:
                    dfs_helper(adj, visited)

        visited = dict()

        for vertex in self.graph.keys():
            visited[vertex] = False

        vertex = self.graph.keys()[0]
        dfs_helper(vertex, visited)
