
class PathNotFoundException(Exception):
    pass


class OriginNotFoundException(TypeError):
    message = 'Origin Vertex not found in the Graph.'


class DestinationNotFoundException(TypeError):
    message = 'Destination Vertex not found in the Graph.'