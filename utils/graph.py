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

    def adjacents(self, v):
        if v not in self.graph:
            raise Exception('vertex not in the graph')

        return self.graph[v]

    def edges(self):
        all_edges = set()

        for v in self.vertices():
            for u in self.graph[v]:
                if (u, v) not in all_edges and (v, u) not in all_edges:
                    all_edges.add((v, u))

        return list(all_edges)
