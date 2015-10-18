from expects import expect, equal, raise_error
from hermes import Graph, Vertex, Edge
from hermes.algorithms import total_path_cost
from hermes.exceptions import PathNotFoundException


class When_we_want_to_find_the_cost_of_a_path:
    def given_a_graph_and_a_path(self):

        self.graph = Graph()
        self.vertex1 = Vertex(element="Vertex 1")
        self.vertex2 = Vertex(element="Vertex 2")
        self.vertex3 = Vertex(element="Vertex 3")
        self.vertex4 = Vertex(element="Vertex 4")

        self.edge12 = Edge(self.vertex1, self.vertex2, element=1)
        self.edge23 = Edge(self.vertex2, self.vertex3, element=2)
        self.edge34 = Edge(self.vertex3, self.vertex4, element=3)
        self.edge43 = Edge(self.vertex4, self.vertex3, element=4)
        self.edge42 = Edge(self.vertex4, self.vertex2, element=5)

        self.graph.add_edge(self.edge12)
        self.graph.add_edge(self.edge23)
        self.graph.add_edge(self.edge34)
        self.graph.add_edge(self.edge43)
        self.graph.add_edge(self.edge42)

        self.path = [self.vertex1, self.vertex2, self.vertex3, self.vertex4]

    def because_we_calculate_the_cost_of_the_path(self):
        self.cost = total_path_cost(self.graph, self.path)

    def it_should_return_the_correct_cost(self):
        expect(self.cost).to(equal(6))


class When_we_want_to_find_the_cost_of_a_path_that_does_not_exist:
    def given_a_graph_and_a_path_that_is_not_valid(self):

        self.graph = Graph()
        self.vertex1 = Vertex(element="Vertex 1")
        self.vertex2 = Vertex(element="Vertex 2")
        self.vertex3 = Vertex(element="Vertex 3")

        self.edge12 = Edge(self.vertex1, self.vertex2, element=1)
        self.edge32 = Edge(self.vertex3, self.vertex2, element=2)
        self.graph.add_edge(self.edge12)
        self.graph.add_edge(self.edge32)

        self.path = [self.vertex3, self.vertex2, self.vertex1]

    def because_we_calculate_the_cost_of_the_invlid_path(self):
        self.callback = lambda: total_path_cost(self.graph, self.path)

    def it_should_raise_an_error(self):
        expect(self.callback).to(raise_error(PathNotFoundException))


class When_we_want_to_find_the_cost_on_an_empty_graph:
    def given_an_empty_graph_and_a_path_that_is_not_valid(self):

        self.graph = Graph()
        self.vertex1 = Vertex(element="Vertex 1")
        self.vertex2 = Vertex(element="Vertex 2")

        self.edge12 = Edge(self.vertex1, self.vertex2, element=1)

        self.path = [self.vertex1, self.vertex2]

    def because_we_calculate_the_cost_of_the_invlid_path(self):
        self.callback = lambda: total_path_cost(self.graph, self.path)

    def it_should_raise_an_error(self):
        expect(self.callback).to(raise_error(PathNotFoundException))
