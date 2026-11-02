"""TDA Cola dinamica siguiendo la interfaz del capitulo VII del libro."""


class nodoCola(object):
    """Nodo simplemente enlazado de la cola."""

    def __init__(self):
        self.info = None
        self.sig = None


class Cola(object):
    """Cola FIFO con punteros al frente y al final."""

    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0


def arribo(cola, dato):
    """Agrega el dato al final de la cola."""
    nodo = nodoCola()
    nodo.info = dato
    if cola.frente is None:
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamanio += 1


def atencion(cola):
    """Quita y devuelve el elemento ubicado en el frente."""
    dato = None
    if cola.frente is not None:
        dato = cola.frente.info
        cola.frente = cola.frente.sig
        cola.tamanio -= 1
        if cola.frente is None:
            cola.final = None
    return dato


def cola_vacia(cola):
    """Devuelve True si la cola no contiene elementos."""
    return cola.frente is None


def tamanio(cola):
    """Devuelve la cantidad de elementos de la cola."""
    return cola.tamanio
