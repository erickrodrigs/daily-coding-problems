"""
This problem was asked by Facebook. (MEDIUM)

A graph is minimally-connected if it is connected and there is no edge that can
be removed while still leaving the graph connected. For example, any binary
tree is minimally-connected.

Given an undirected graph, check if the graph is minimally-connected. You can
choose to represent the graph as either an adjacency matrix or adjacency list.
"""

from utils.graph import Graph


def dfs(vertex, graph, visited, removed_edge):
    visited[vertex] = True

    for adj in graph.adjacents(vertex):
        if (vertex, adj) == removed_edge or (adj, vertex) == removed_edge:
            continue

        if not visited[adj]:
            dfs(adj, graph, visited, removed_edge)


def count_components(graph, removed_edge):
    visited = dict()
    for vertex in graph.vertices():
        visited[vertex] = False

    components = 0

    for vertex in graph.vertices():
        if not visited[vertex]:
            components += 1
            dfs(vertex, graph, visited, removed_edge)

    return components


def is_minimally_connected(graph):
    # check whether the graph is connected
    if count_components(graph, None) > 1:
        return False

    # check removing one edge per iteration
    for edge in graph.edges():
        if count_components(graph, edge) > 1:
            return True

    return False


def test_minimally_connected():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)
    graph.add_edge(3, 7)
    assert is_minimally_connected(graph) == True


def test_is_not_minimally_connected():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)
    assert is_minimally_connected(graph) == False


def test_graph_is_not_connected():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)
    graph.add_vertex(7)
    assert is_minimally_connected(graph) == False


"""
SOLUTION:
v = number of vertices
e = number of edges

- time complexity: O(e * (v + e))
- space complexity: O(v * e)
"""
