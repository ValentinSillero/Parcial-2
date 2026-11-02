"""TDA Pila dinamica siguiendo la interfaz del capitulo VI del libro."""


class nodoPila(object):
    """Nodo simplemente enlazado de la pila."""

    info, sig = None, None


class Pila(object):
    """Pila LIFO con un puntero a la cima."""

    def __init__(self):
        self.cima = None
        self.tamanio = 0


def apilar(pila, dato):
    """Apila el dato sobre la cima."""
    nodo = nodoPila()
    nodo.info = dato
    nodo.sig = pila.cima
    pila.cima = nodo
    pila.tamanio += 1


def desapilar(pila):
    """Desapila y devuelve el elemento de la cima."""
    dato = None
    if pila.cima is not None:
        dato = pila.cima.info
        pila.cima = pila.cima.sig
        pila.tamanio -= 1
    return dato


def pila_vacia(pila):
    """Devuelve True si la pila no contiene elementos."""
    return pila.cima is None


def en_cima(pila):
    """Devuelve el elemento de la cima sin quitarlo."""
    return None if pila.cima is None else pila.cima.info


def tamanio(pila):
    """Devuelve la cantidad de elementos de la pila."""
    return pila.tamanio
