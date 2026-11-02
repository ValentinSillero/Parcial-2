"""Grafo no dirigido con vertices, aristas, Dijkstra y Prim."""

from math import inf
from tda_heap import Heap, arribo_h, atencion_h, buscar_h, cambiar_prioridad, heap_vacio
from tda_pila import Pila, apilar, desapilar, pila_vacia


class Graph(list):
    class _nodeVertex:
        def __init__(self, value, other_values=None):
            self.value = value
            self.other_values = other_values
            self.edges = []

    class _nodeEdge:
        def __init__(self, weight, destination):
            self.weight = weight
            self.destination = destination

    def __init__(self, is_dir=True):
        super().__init__()
        self.is_dir = is_dir

    def search(self, value):
        for vertex in self:
            if vertex.value == value:
                return vertex
        return None

    def add_vertex(self, value, other_values=None):
        self.append(self._nodeVertex(value, other_values))
        self.sort(key=lambda vertex: vertex.value)

    def add_edge(self, weight, origin, destination):
        vertex_origin = self.search(origin)
        vertex_destination = self.search(destination)
        if vertex_origin is None or vertex_destination is None:
            return
        vertex_origin.edges.append(self._nodeEdge(weight, destination))
        vertex_origin.edges.sort(key=lambda edge: edge.destination)
        if not self.is_dir and origin != destination:
            vertex_destination.edges.append(self._nodeEdge(weight, origin))
            vertex_destination.edges.sort(key=lambda edge: edge.destination)

    def dijkstra(self, origin):
        """Dijkstra con monticulo minimo y pila, como el ejemplo del profesor."""
        no_visited = Heap(len(self))
        path = Pila()

        for vertex in self:
            distance = 0 if vertex.value == origin else inf
            arribo_h(no_visited, [vertex.value, vertex, None], distance)

        while not heap_vacio(no_visited):
            current = atencion_h(no_visited)
            distance = current[0]
            vertex = current[1][1]
            apilar(path, [current[1][0], distance, current[1][2]])
            if distance != inf:
                for edge in vertex.edges:
                    pos = buscar_h(no_visited, edge.destination)
                    if pos is not None and distance + edge.weight < no_visited.vector[pos][0]:
                        no_visited.vector[pos][1][2] = vertex.value
                        cambiar_prioridad(no_visited, pos, distance + edge.weight)
        return path

    def shortest_path(self, origin, destination):
        """Reconstruye el camino usando la pila devuelta por Dijkstra."""
        path = self.dijkstra(origin)
        result = []
        cost = None
        current_destination = destination

        while not pila_vacia(path):
            value = desapilar(path)
            if value[0] == current_destination:
                if cost is None:
                    cost = value[1]
                result.append(value[0])
                current_destination = value[2]
                if current_destination is None:
                    break
        result.reverse()
        if not result or result[0] != origin or cost == inf:
            return [], inf
        return result, cost

    def prim(self, origin):
        """Arbol de expansion minima empezando en el vertice indicado."""
        if self.search(origin) is None:
            return [], 0
        visited = {origin}
        pending = Heap(len(self))
        tree = []
        total = 0

        for edge in self.search(origin).edges:
            arribo_h(pending, [origin, edge.destination], edge.weight)

        while not heap_vacio(pending) and len(visited) < len(self):
            current = atencion_h(pending)
            weight = current[0]
            first, second = current[1]
            if second not in visited:
                visited.add(second)
                tree.append((first, second, weight))
                total += weight
                for edge in self.search(second).edges:
                    if edge.destination not in visited:
                        arribo_h(pending, [second, edge.destination], edge.weight)
        return tree, total
