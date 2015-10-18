# -*- coding: utf-8 -*-
from hermes.exceptions import PathNotFoundException


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
        try:
            edge = graph.vertices[vertex][next_vertex]
        except KeyError:
            raise PathNotFoundException()
        cost += edge.element
    return cost
