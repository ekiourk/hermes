from expects import expect, equal, raise_error
from hermes import Graph, Vertex, Edge
from hermes.algorithms import shortest_path


class When_we_want_to_find_the_path_with_the_smaller_cost:
    def given_a_graph(self):

        self.graph = Graph()
        self.vertex1 = Vertex(element="Vertex 1")
        self.vertex2 = Vertex(element="Vertex 2")
        self.vertex3 = Vertex(element="Vertex 3")
        self.vertex4 = Vertex(element="Vertex 4")

        self.edge12 = Edge(self.vertex1, self.vertex2, element=3)
        self.edge23 = Edge(self.vertex2, self.vertex3, element=1)
        self.edge34 = Edge(self.vertex3, self.vertex4, element=1)
        self.edge24 = Edge(self.vertex2, self.vertex4, element=1)

        self.graph.add_edge(self.edge12)
        self.graph.add_edge(self.edge23)
        self.graph.add_edge(self.edge34)
        self.graph.add_edge(self.edge24)

    def because_we_calculate_the_most_cost_effective_path(self):
        self.path, self.cost = shortest_path(self.graph, self.vertex1, self.vertex4)

    def it_should_return_the_shortest_path(self):
        expected_path = [self.vertex1, self.vertex2, self.vertex4]
        expect(self.path).to(equal(expected_path))

    def it_should_return_the_correct_cost_of_the_shortest_path(self):
        expect(self.cost).to(equal(4))


class When_we_want_to_find_the_path_with_the_smaller_cost_on_a_more_compicated_graph:
    def given_a_graph(self):

        self.graph = Graph()
        self.vertex1 = Vertex(element="Vertex 1")
        self.vertex2 = Vertex(element="Vertex 2")
        self.vertex3 = Vertex(element="Vertex 3")
        self.vertex4 = Vertex(element="Vertex 4")

        self.edge12 = Edge(self.vertex1, self.vertex2, element=3)
        self.edge23 = Edge(self.vertex2, self.vertex3, element=1)
        self.edge34 = Edge(self.vertex3, self.vertex4, element=2)
        self.edge24 = Edge(self.vertex2, self.vertex4, element=10)

        # Add special case of edge that is looping from vertex2 to itself
        self.edge22 = Edge(self.vertex2, self.vertex2, element=1)

        self.graph.add_edge(self.edge12)
        self.graph.add_edge(self.edge23)
        self.graph.add_edge(self.edge34)
        self.graph.add_edge(self.edge24)
        self.graph.add_edge(self.edge22)

    def because_we_calculate_the_most_cost_effective_path(self):
        self.path, self.cost = shortest_path(self.graph, self.vertex1, self.vertex4)

    def it_should_return_the_shortest_path(self):
        expected_path = [self.vertex1, self.vertex2, self.vertex3, self.vertex4]
        expect(self.path).to(equal(expected_path))

    def it_should_return_the_correct_cost_of_the_shortest_path(self):
        expect(self.cost).to(equal(6))


class When_we_want_to_find_the_path_when_it_is_unreachable:
    def given_a_graph(self):

        self.graph = Graph()
        self.vertex1 = Vertex(element="Vertex 1")
        self.vertex2 = Vertex(element="Vertex 2")
        self.vertex3 = Vertex(element="Vertex 3")
        self.vertex4 = Vertex(element="Vertex 4")

        self.edge12 = Edge(self.vertex1, self.vertex2, element=3)
        self.edge23 = Edge(self.vertex2, self.vertex3, element=1)
        self.edge43 = Edge(self.vertex4, self.vertex3, element=1)
        self.edge42 = Edge(self.vertex4, self.vertex2, element=1)

        self.graph.add_edge(self.edge12)
        self.graph.add_edge(self.edge23)
        self.graph.add_edge(self.edge43)
        self.graph.add_edge(self.edge42)

    def because_we_calculate_the_shortest_path_to_an_unreachable_vertex(self):
        self.path, self.cost = shortest_path(self.graph, self.vertex1, self.vertex4)

    def it_should_return_the_shortest_path(self):
        expect(self.path).to(equal([]))

    def it_should_return_the_correct_cost_of_the_shortest_path(self):
        expect(self.cost).to(equal(float("inf")))


class When_we_want_to_find_the_shortest_path_for_non_existing_vertices:
    def given_a_graph(self):

        self.graph = Graph()
        self.vertex1 = Vertex(element="Vertex 1")
        self.vertex2 = Vertex(element="Vertex 2")

    def because_we_calculate_the_most_cost_effective_path(self):
        self.callback = lambda: shortest_path(self.graph, self.vertex1, self.vertex2)

    def it_should_raise_an_error(self):
        expect(self.callback).to(raise_error(TypeError))