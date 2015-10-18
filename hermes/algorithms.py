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


def dijkstra(graph, origin, destination):
    """
    Given a graph, an origin and a destination
    returns the shortest path from origin to destination.

    done_vertices is a list of the vertices that we know the shortest path to them from origin
    distances dict keep the distances for the done vertices
    """

    done_vertices = []
    distances = {}
    predecessors = {}

    while origin != destination:
        if not done_vertices:
            # in the first run we put the distance from origin to itself as 0
            distances[origin] = 0

        # visit the neighbours
        neighbours = graph.get_neighbour_vertices(origin)
        for neighbor in neighbours:
            if neighbor not in done_vertices:
                new_distance = distances[origin] + neighbours[neighbor]
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = origin

        done_vertices.append(origin)  # mark as a done vertex

        # At this point we iterate through the non done vertices
        # and find the vertex with the lowest distance.
        # We set that vertex as the new origin
        undone_vertices = {}
        for vertex in graph.vertices:
            if vertex not in done_vertices:
                undone_vertices[vertex] = distances.get(vertex, float('inf'))
        origin = min(undone_vertices, key=undone_vertices.get)

    # We build the shortest path and return it
    path = []
    pred = destination
    while pred is not None:
        path.append(pred)
        pred = predecessors.get(pred, None)

    try:
        total_distance = distances[destination]
    except KeyError:
        return [], float("inf")

    # path at that point has the vertices from destination to origin order, so we reverse it
    path.reverse()
    return path, total_distance


def shortest_path(graph, origin, destination, algorithm=dijkstra):

    if origin not in graph:
        raise TypeError('Origin Vertex not found in the Graph.')
    if destination not in graph:
        raise TypeError('Destination Vertex not found in the Graph.')

    return algorithm(graph, origin, destination)
