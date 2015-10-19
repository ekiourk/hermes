from expects import expect, equal, raise_error
from hermes import Graph, Vertex, Edge
from hermes.algorithms import shortest_path


class When_we_want_to_find_the_path_with_the_smaller_cost:
    def given_a_graph(self):
        """
        (A)--3-->(B)--1-->(C)--1-->(D)
                  \                /
                   -------1------->
        """

        self.graph = Graph()
        self.vertexA = Vertex(element="Vertex A")
        self.vertexB = Vertex(element="Vertex B")
        self.vertexC = Vertex(element="Vertex C")
        self.vertexD = Vertex(element="Vertex D")

        self.edgeAB = Edge(self.vertexA, self.vertexB, element=3)
        self.edgeBC = Edge(self.vertexB, self.vertexC, element=1)
        self.edgeCD = Edge(self.vertexC, self.vertexD, element=1)
        self.edgeBD = Edge(self.vertexB, self.vertexD, element=1)

        self.graph.add_edge(self.edgeAB)
        self.graph.add_edge(self.edgeBC)
        self.graph.add_edge(self.edgeCD)
        self.graph.add_edge(self.edgeBD)

    def because_we_calculate_the_most_cost_effective_path(self):
        self.path, self.cost = shortest_path(self.graph, self.vertexA, self.vertexD)

    def it_should_return_the_shortest_path(self):
        expected_path = [self.vertexA, self.vertexB, self.vertexD]
        expect(self.path).to(equal(expected_path))

    def it_should_return_the_correct_cost_of_the_shortest_path(self):
        expect(self.cost).to(equal(4))


class When_we_want_to_find_the_path_with_the_smaller_cost_on_a_more_compicated_graph:
    def given_a_graph(self):
        """         1
                  / \
                  \ /
        (A)--3-->(B)--1-->(C)--2-->(D)
                  \                /
                   -------10------>
        """

        self.graph = Graph()
        self.vertexA = Vertex(element="Vertex A")
        self.vertexB = Vertex(element="Vertex B")
        self.vertexC = Vertex(element="Vertex C")
        self.vertexD = Vertex(element="Vertex D")

        self.edgeAB = Edge(self.vertexA, self.vertexB, element=3)
        self.edgeBC = Edge(self.vertexB, self.vertexC, element=1)
        self.edgeCD = Edge(self.vertexC, self.vertexD, element=2)
        self.edgeBD = Edge(self.vertexB, self.vertexD, element=10)

        # Add special case of edge that is looping from vertexB to itself
        self.edgeBB = Edge(self.vertexB, self.vertexB, element=1)

        self.graph.add_edge(self.edgeAB)
        self.graph.add_edge(self.edgeBC)
        self.graph.add_edge(self.edgeCD)
        self.graph.add_edge(self.edgeBD)
        self.graph.add_edge(self.edgeBB)

    def because_we_calculate_the_most_cost_effective_path(self):
        self.path, self.cost = shortest_path(self.graph, self.vertexA, self.vertexD)

    def it_should_return_the_shortest_path(self):
        expected_path = [self.vertexA, self.vertexB, self.vertexC, self.vertexD]
        expect(self.path).to(equal(expected_path))

    def it_should_return_the_correct_cost_of_the_shortest_path(self):
        expect(self.cost).to(equal(6))


class When_we_want_to_find_the_shortest_path_with_the_same_origin_and_destination:
    def given_a_graph(self):
        """
        (A)--1-->(B)--1-->(C)
         \                /
          <-------1-------
        """

        self.graph = Graph()
        self.vertexA = Vertex(element="Vertex A")
        self.vertexB = Vertex(element="Vertex B")
        self.vertexC = Vertex(element="Vertex C")

        self.edgeAB = Edge(self.vertexA, self.vertexB, element=1)
        self.edgeBC = Edge(self.vertexB, self.vertexC, element=1)
        self.edgeCA = Edge(self.vertexC, self.vertexA, element=1)

        self.graph.add_edge(self.edgeAB)
        self.graph.add_edge(self.edgeBC)
        self.graph.add_edge(self.edgeCA)

    def because_we_calculate_the_most_cost_effective_path(self):
        self.path, self.cost = shortest_path(self.graph, self.vertexA, self.vertexA)

    def it_should_return_the_shortest_path(self):
        expected_path = [self.vertexA, self.vertexB, self.vertexC, self.vertexA]
        expect(self.path).to(equal(expected_path))

    def it_should_return_the_correct_cost_of_the_shortest_path(self):
        expect(self.cost).to(equal(3))


class When_we_want_to_find_the_path_when_it_is_unreachable:
    def given_a_graph(self):
        """
        (A)--3-->(B)--1-->(C)<--1--(D)
                  \                /
                   <-------1-------
        """

        self.graph = Graph()
        self.vertexA = Vertex(element="Vertex A")
        self.vertexB = Vertex(element="Vertex B")
        self.vertexC = Vertex(element="Vertex C")
        self.vertexD = Vertex(element="Vertex D")

        self.edgeAB = Edge(self.vertexA, self.vertexB, element=3)
        self.edgeBC = Edge(self.vertexB, self.vertexC, element=1)
        self.edgeDC = Edge(self.vertexD, self.vertexC, element=1)
        self.edgeDB = Edge(self.vertexD, self.vertexB, element=1)

        self.graph.add_edge(self.edgeAB)
        self.graph.add_edge(self.edgeBC)
        self.graph.add_edge(self.edgeDC)
        self.graph.add_edge(self.edgeDB)

    def because_we_calculate_the_shortest_path_to_an_unreachable_vertex(self):
        self.path, self.cost = shortest_path(self.graph, self.vertexA, self.vertexD)

    def it_should_return_the_shortest_path(self):
        expect(self.path).to(equal([]))

    def it_should_return_the_correct_cost_of_the_shortest_path(self):
        expect(self.cost).to(equal(float("inf")))


class When_we_want_to_find_the_shortest_path_for_non_existing_vertices:
    def given_a_graph(self):

        self.graph = Graph()
        self.vertexA = Vertex(element="Vertex A")
        self.vertexB = Vertex(element="Vertex B")

    def because_we_calculate_the_most_cost_effective_path(self):
        self.callback = lambda: shortest_path(self.graph, self.vertexA, self.vertexB)

    def it_should_raise_an_error(self):
        expect(self.callback).to(raise_error(TypeError))