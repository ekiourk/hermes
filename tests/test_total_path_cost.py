from expects import expect, equal, raise_error
from hermes import Graph, Vertex, Edge
from hermes.algorithms import total_path_cost
from hermes.exceptions import PathNotFoundException


class When_we_want_to_find_the_cost_of_a_path:
    def given_a_graph_and_a_path(self):
        """
                            <--4---
                           /       \
        (A)--1-->(B)--2-->(C)--3-->(D)
                  \                /
                   <-------5-------
        """

        self.graph = Graph()
        self.vertexA = Vertex(element="Vertex A")
        self.vertexB = Vertex(element="Vertex B")
        self.vertexC = Vertex(element="Vertex C")
        self.vertexD = Vertex(element="Vertex D")

        self.edgeAB = Edge(self.vertexA, self.vertexB, element=1)
        self.edgeBC = Edge(self.vertexB, self.vertexC, element=2)
        self.edgeCD = Edge(self.vertexC, self.vertexD, element=3)
        self.edgeDC = Edge(self.vertexD, self.vertexC, element=4)
        self.edgeDB = Edge(self.vertexD, self.vertexB, element=5)

        self.graph.add_edge(self.edgeAB)
        self.graph.add_edge(self.edgeBC)
        self.graph.add_edge(self.edgeCD)
        self.graph.add_edge(self.edgeDC)
        self.graph.add_edge(self.edgeDB)

        self.path = [self.vertexA, self.vertexB, self.vertexC, self.vertexD]

    def because_we_calculate_the_cost_of_the_path(self):
        self.cost = total_path_cost(self.graph, self.path)

    def it_should_return_the_correct_cost(self):
        expect(self.cost).to(equal(6))


class When_we_want_to_find_the_cost_of_a_path_that_does_not_exist:
    def given_a_graph_and_a_path_that_is_not_valid(self):
        """
        (A)--1-->(B)<--2--(C)
        """

        self.graph = Graph()
        self.vertexA = Vertex(element="Vertex A")
        self.vertexB = Vertex(element="Vertex B")
        self.vertexC = Vertex(element="Vertex C")

        self.edgeAB = Edge(self.vertexA, self.vertexB, element=1)
        self.edgeCB = Edge(self.vertexC, self.vertexB, element=2)
        self.graph.add_edge(self.edgeAB)
        self.graph.add_edge(self.edgeCB)

        self.path = [self.vertexC, self.vertexB, self.vertexA]

    def because_we_calculate_the_cost_of_the_invlid_path(self):
        self.callback = lambda: total_path_cost(self.graph, self.path)

    def it_should_raise_an_error(self):
        expect(self.callback).to(raise_error(PathNotFoundException))


class When_we_want_to_find_the_cost_on_an_empty_graph:
    def given_an_empty_graph_and_a_path_that_is_not_valid(self):

        self.graph = Graph()
        self.vertexA = Vertex(element="Vertex A")
        self.vertexB = Vertex(element="Vertex B")

        self.edgeAB = Edge(self.vertexA, self.vertexB, element=1)

        self.path = [self.vertexA, self.vertexB]

    def because_we_calculate_the_cost_of_the_invlid_path(self):
        self.callback = lambda: total_path_cost(self.graph, self.path)

    def it_should_raise_an_error(self):
        expect(self.callback).to(raise_error(PathNotFoundException))
