"""TDA Heap minimo usado como cola de prioridad por el TDA Grafo.

Conserva los nombres del capitulo XII: ``Heap``, ``agregar``, ``quitar``,
``flotar``, ``hundir``, ``heap_vacio``, ``arribo`` y ``atencion``. Cada
elemento de la cola se almacena como ``[prioridad, dato]``.
"""

from math import inf


class Heap(object):
    """Monticulo binario minimo representado mediante un vector."""

    def __init__(self, tamanio):
        self.tamanio = 0
        self.vector = [None] * max(1, tamanio)


def intercambio(vector, indice_1, indice_2):
    vector[indice_1], vector[indice_2] = vector[indice_2], vector[indice_1]


def _prioridad(elemento):
    return elemento[0]


def flotar(heap, indice):
    """Flota un elemento mientras su prioridad sea menor que la del padre."""
    while indice > 0:
        padre = (indice - 1) // 2
        if _prioridad(heap.vector[indice]) >= _prioridad(heap.vector[padre]):
            break
        intercambio(heap.vector, indice, padre)
        indice = padre


def hundir(heap, indice):
    """Hunde un elemento hasta restaurar el orden del monticulo minimo."""
    while True:
        hijo_izq = (indice * 2) + 1
        if hijo_izq >= heap.tamanio:
            break
        hijo_der = hijo_izq + 1
        menor = hijo_izq
        if (
            hijo_der < heap.tamanio
            and _prioridad(heap.vector[hijo_der]) < _prioridad(heap.vector[hijo_izq])
        ):
            menor = hijo_der
        if _prioridad(heap.vector[indice]) <= _prioridad(heap.vector[menor]):
            break
        intercambio(heap.vector, indice, menor)
        indice = menor


def agregar(heap, dato):
    """Agrega un elemento al monticulo y lo flota."""
    if heap.tamanio == len(heap.vector):
        heap.vector.extend([None] * max(1, len(heap.vector)))
    heap.vector[heap.tamanio] = dato
    flotar(heap, heap.tamanio)
    heap.tamanio += 1


def quitar(heap):
    """Quita y devuelve el elemento de menor prioridad."""
    if heap.tamanio == 0:
        return None
    intercambio(heap.vector, 0, heap.tamanio - 1)
    heap.tamanio -= 1
    dato = heap.vector[heap.tamanio]
    heap.vector[heap.tamanio] = None
    if heap.tamanio > 0:
        hundir(heap, 0)
    return dato


def cantidad_elementos(heap):
    return heap.tamanio


def heap_vacio(heap):
    return heap.tamanio == 0


def heap_lleno(heap):
    return heap.tamanio == len(heap.vector)


def arribo(heap, dato, prioridad):
    """Arriba un dato a la cola utilizando una prioridad."""
    agregar(heap, [prioridad, dato])


def atencion(heap):
    """Atiende el frente y devuelve solamente el dato, como en el capitulo XII."""
    elemento = quitar(heap)
    return None if elemento is None else elemento[1]


def cambiar_prioridad(heap, indice, prioridad):
    """Cambia la prioridad y reacomoda el elemento."""
    prioridad_anterior = heap.vector[indice][0]
    heap.vector[indice][0] = prioridad
    if prioridad < prioridad_anterior:
        flotar(heap, indice)
    elif prioridad > prioridad_anterior:
        hundir(heap, indice)


def buscar(heap, buscado):
    """Busca un vertice por ``info`` dentro de los datos de Dijkstra."""
    for indice in range(heap.tamanio):
        dato = heap.vector[indice][1]
        vertice = dato[0] if isinstance(dato, (list, tuple)) else dato
        if getattr(vertice, "info", vertice) == buscado:
            return indice
    return None


# Variantes usadas por los algoritmos de grafos del capitulo XIII. En este
# caso ``atencion_h`` conserva tambien la prioridad para Dijkstra y los AEM.
arribo_h = arribo


def atencion_h(heap):
    return quitar(heap)


buscar_h = buscar


def prioridad_infinita():
    """Devuelve infinito para inicializar Dijkstra."""
    return inf
