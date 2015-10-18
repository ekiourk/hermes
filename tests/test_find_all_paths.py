from expects import expect, equal, contain
from hermes import Graph, Vertex, Edge
from hermes.algorithms import find_paths


class When_we_want_to_find_the_number_of_paths_between_two_vertices:
    def given_a_graph(self):
        """
           ------------5---------->
          /                        \
        (A)--3-->(B)--1-->(C)--1-->(D)
                  \                /
                   -------3------->
        """

        self.graph = Graph()
        self.vertexA = Vertex(element="Vertex A")
        self.vertexB = Vertex(element="Vertex B")
        self.vertexC = Vertex(element="Vertex C")
        self.vertexD = Vertex(element="Vertex D")

        self.edgeAB = Edge(self.vertexA, self.vertexB, element=3)
        self.edgeAD = Edge(self.vertexA, self.vertexD, element=5)
        self.edgeBC = Edge(self.vertexB, self.vertexC, element=1)
        self.edgeCD = Edge(self.vertexC, self.vertexD, element=1)
        self.edgeBD = Edge(self.vertexB, self.vertexD, element=3)

        self.graph.add_edge(self.edgeAB)
        self.graph.add_edge(self.edgeAD)
        self.graph.add_edge(self.edgeBC)
        self.graph.add_edge(self.edgeCD)
        self.graph.add_edge(self.edgeBD)

    def because_we_want_all_available_paths_from_A_to_B(self):
        self.paths = find_paths(self.graph, self.vertexA, self.vertexD)

    def it_should_return_the_correct_list_of_available_paths(self):
        expected_paths = [
            [self.vertexA, self.vertexD],
            [self.vertexA, self.vertexB, self.vertexD],
            [self.vertexA, self.vertexB, self.vertexC, self.vertexD]
        ]
        for path in expected_paths:
            expect(self.paths).to(contain(path))


class When_we_want_to_find_the_number_of_paths_between_two_vertices_in_a_cyclic_graph:
    def given_a_graph(self):
        """
            -----------5---------->
           /        <--2---       \
          /        /       \       \
        (A)--3-->(B)--1-->(C)--1-->(D)
         \        \       /        /
          \        <-----/--3------
           -----2------>/
        """

        self.graph = Graph()
        self.vertexA = Vertex(element="Vertex A")
        self.vertexB = Vertex(element="Vertex B")
        self.vertexC = Vertex(element="Vertex C")
        self.vertexD = Vertex(element="Vertex D")

        self.edgeAB = Edge(self.vertexA, self.vertexB, element=3)
        self.edgeAD = Edge(self.vertexA, self.vertexD, element=5)
        self.edgeAC = Edge(self.vertexA, self.vertexC, element=2)
        self.edgeBC = Edge(self.vertexB, self.vertexC, element=1)
        self.edgeCB = Edge(self.vertexC, self.vertexB, element=2)
        self.edgeCD = Edge(self.vertexC, self.vertexD, element=1)
        self.edgeDB = Edge(self.vertexD, self.vertexB, element=3)

        self.graph.add_edge(self.edgeAB)
        self.graph.add_edge(self.edgeAD)
        self.graph.add_edge(self.edgeAC)
        self.graph.add_edge(self.edgeBC)
        self.graph.add_edge(self.edgeCD)
        self.graph.add_edge(self.edgeDB)

    def because_we_want_all_available_paths_from_A_to_B(self):
        self.paths = find_paths(self.graph, self.vertexA, self.vertexD)

    def it_should_return_the_correct_list_of_available_paths(self):
        expected_paths = [
            [self.vertexA, self.vertexD],
            [self.vertexA, self.vertexC, self.vertexD],
            [self.vertexA, self.vertexB, self.vertexC, self.vertexD]
        ]
        for path in expected_paths:
            expect(self.paths).to(contain(path))