#!/usr/bin/env python3

from hermes import Graph, Edge, Vertex
from hermes.algorithms import total_path_cost, shortest_path, find_paths, find_paths_equal_to_size, find_paths_lt_hours
from hermes.exceptions import PathNotFoundException


def total_path_cost_days(*args, **kwargs):
    try:
        return "{} days".format(total_path_cost(*args, **kwargs))
    except PathNotFoundException:
        return "not possible"


shipping_graph = Graph()

new_york = Vertex(element="New York")
liverpool = Vertex(element="Liverpool")
casablanca = Vertex(element="Casablanca")
buenos_aires = Vertex(element="Buenos Aires")
cape_town = Vertex(element="Cape Town")


shipping_graph.add_edge(Edge(buenos_aires, new_york, element=6))
shipping_graph.add_edge(Edge(buenos_aires, casablanca, element=5))
shipping_graph.add_edge(Edge(buenos_aires, cape_town, element=4))
shipping_graph.add_edge(Edge(new_york, liverpool, element=4))
shipping_graph.add_edge(Edge(liverpool, casablanca, element=3))
shipping_graph.add_edge(Edge(liverpool, cape_town, element=6))
shipping_graph.add_edge(Edge(casablanca, liverpool, element=3))
shipping_graph.add_edge(Edge(casablanca, cape_town, element=6))
shipping_graph.add_edge(Edge(cape_town, new_york, element=8))


"""
What is the total journey time for the following direct routes (your model should indicate if the journey is invalid):

- Buenos Aires -> New York -> Liverpool
- Buenos Aires -> Casablanca -> Liverpool
- Buenos Aires -> Cape Town -> New York -> Liverpool -> Casablanca
- Buenos Aires -> Cape Town -> Casablanca
"""

print("Total journey time for Buenos Aires -> New York -> Liverpool is {}".format(
    total_path_cost_days(shipping_graph, [buenos_aires, new_york, liverpool])
))

print("Total journey time for Buenos Aires -> Casablanca -> Liverpool is {}".format(
    total_path_cost_days(shipping_graph, [buenos_aires, casablanca, liverpool])
))

print("Total journey time for Buenos Aires -> Cape Town -> New York -> Liverpool -> Casablanca is {}".format(
    total_path_cost_days(shipping_graph, [buenos_aires, cape_town, new_york, liverpool, casablanca])
))

print("Total journey time for Buenos Aires -> Cape Town -> Casablanca is {}".format(
    total_path_cost_days(shipping_graph, [buenos_aires, cape_town, casablanca])
))


"""
Find the shortest journey time for the following routes:

- Buenos Aires -> Liverpool

- New York -> New York
"""

_, journey = shortest_path(shipping_graph, buenos_aires, liverpool)
print("Shortest journey time for Buenos Aires -> Liverpool is {} days".format(journey))

_, journey = shortest_path(shipping_graph, new_york, new_york)
print("Shortest journey time for New York -> New York is {} days".format(journey))


"""
Find the number of routes from Liverpool to Liverpool with a maximum number of 3 stops.

Find the number of routes from Buenos Aires to Liverpool where exactly 4 stops are made.
"""

print("The number of routes from Liverpool to Liverpool with a maximum number of 3 stops are {}".format(
    len(list(find_paths(shipping_graph, liverpool, liverpool, 3)))
))

print("The number of routes from Buenos Aires to Liverpool where exactly 4 stops are made are {}".format(
    len(list(find_paths_equal_to_size(shipping_graph, buenos_aires, liverpool, 4)))
))

"""
Find the number of routes from Liverpool to Liverpool where the journey time is less than or equal to 25 days.
"""

print("The number of routes from Liverpool to Liverpool where the journey time is less than or equal to 25 days are {}".format(
    len(list(find_paths_lt_hours(shipping_graph, liverpool, liverpool, 25)))
))
