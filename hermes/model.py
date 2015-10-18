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

    def get_edge(self, origin, destination):
        try:
            return self.vertices[origin][destination]
        except KeyError:
            return


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
        return "'{origin}' -({element})-> '{destination}'".format(**self.__dict__)
