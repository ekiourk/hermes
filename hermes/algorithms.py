# -*- coding: utf-8 -*-


def total_path_cost(graph, path):
    """
    Given a Graph and a path of Vertices return the total cost of the path.
    If the path is not valid then Throws PathNotFoundException
    """

    cost = 0
    for idx, vertex in enumerate(path):
        try:
            next_vertex = path[idx+1]
        except IndexError:
            return cost
        edge = graph.vertices[vertex][next_vertex]
        cost += edge.element
    return cost
