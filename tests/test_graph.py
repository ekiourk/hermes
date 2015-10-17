from expects import expect, equal, have_len


class Graph(dict):

    def add_vertex(self, vertex):
        if vertex not in self:
            self[vertex] = {}

    def add_edge(self, edge):
        self.add_vertex(edge.origin)
        self.add_vertex(edge.destination)
        self[edge.origin][edge.destination] = edge

    @property
    def vertices(self):
        return self

    @property
    def edges(self):
        for vertex, vertex_destintations in self.vertices.items():
            for vertex_dest, edge in vertex_destintations.items():
                yield edge


class Vertex:
    def __init__(self, element):
        self.element = element

    def __repr__(self):
        return self.element


class Edge:
    def __init__(self, origin, destination, element):
        self.origin = origin
        self.destination = destination
        self.element = element

    def __repr__(self):
        return self.element


class When_we_want_to_work_with_a_simple_graph:

    def given_an_empty_graph(self):
        self.graph = Graph()

    def because_we_configure_the_graph_with_vertices_and_edges(self):
        self.vertex1 = Vertex(element="Vertex 1")
        self.vertex2 = Vertex(element="Vertex 2")
        self.vertex3 = Vertex(element="Vertex 3")

        self.edge12 = Edge(self.vertex1, self.vertex2, element="6")
        self.edge23 = Edge(self.vertex2, self.vertex3, element="4")

        self.graph.add_edge(self.edge12)
        self.graph.add_edge(self.edge23)

    def it_should_have_the_correct_number_of_vertices(self):
        expect(self.graph.vertices).to(have_len(3))

    def it_should_have_the_correct_number_of_edges(self):
        expect(self.graph.edges).to(have_len(2))

    def it_should_have_the_correct_configuration(self):
        expect(self.graph).to(equal({
            self.vertex1: {self.vertex2: self.edge12},
            self.vertex2: {self.vertex3: self.edge23},
            self.vertex3: {}}))


class When_we_want_to_work_with_a_graph_with_cycles:

    def given_an_empty_graph(self):
        self.graph = Graph()

    def because_we_configure_the_graph_with_vertices_and_edges(self):
        self.vertex1 = Vertex(element="Vertex 1")
        self.vertex2 = Vertex(element="Vertex 2")
        self.vertex3 = Vertex(element="Vertex 3")
        self.vertex4 = Vertex(element="Vertex 4")

        self.edge12 = Edge(self.vertex1, self.vertex2, element="1")
        self.edge23 = Edge(self.vertex2, self.vertex3, element="2")
        self.edge34 = Edge(self.vertex3, self.vertex4, element="3")
        self.edge43 = Edge(self.vertex4, self.vertex3, element="4")
        self.edge42 = Edge(self.vertex4, self.vertex2, element="5")

        self.graph.add_edge(self.edge12)
        self.graph.add_edge(self.edge23)
        self.graph.add_edge(self.edge34)
        self.graph.add_edge(self.edge43)
        self.graph.add_edge(self.edge42)

    def it_should_have_the_correct_number_of_vertices(self):
        expect(self.graph.vertices).to(have_len(4))

    def it_should_have_the_correct_number_of_edges(self):
        expect(self.graph.edges).to(have_len(5))

    def it_should_have_the_correct_configuration(self):
        expect(self.graph).to(equal({
            self.vertex1: {self.vertex2: self.edge12},
            self.vertex2: {self.vertex3: self.edge23},
            self.vertex3: {self.vertex4: self.edge34},
            self.vertex4: {self.vertex3: self.edge43,
                           self.vertex2: self.edge42},
        }))