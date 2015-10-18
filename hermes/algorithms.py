# -*- coding: utf-8 -*-
from hermes.exceptions import PathNotFoundException


def enumerate_edges(path):
    """
    Given a path yields pairs of vertices that each one forms an edge.
    For example a path [1, 2, 3, 4, 5] will return (1,2) (2, 3) (3, 4) and (4, 5)
    """
    for idx, vertex in enumerate(path):
        try:
            yield vertex, path[idx+1]
        except IndexError:
            # There are no more edges in the path
            return


def total_path_cost(graph, path):
    """
    Given a Graph and a path of Vertices return the total cost of the path.
    If the path is not valid then Throws PathNotFoundException
    """

    cost = 0
    for vertex, next_vertex in enumerate_edges(path):
        edge = graph.get_edge(vertex, next_vertex)
        if edge is None:
            raise PathNotFoundException()
        cost += edge.element
    return cost
