"""Ejercicio 1: tres arboles AVL para los Pokemon de nueve generaciones."""

import random
from datos_pokemon import DATOS_POKEMON
from tda_arbol import BinaryTree


TIPOS = (
    "Normal",
    "Fuego",
    "Agua",
    "Eléctrico",
    "Planta",
    "Hielo",
    "Lucha",
    "Veneno",
    "Tierra",
    "Volador",
    "Psíquico",
    "Bicho",
    "Roca",
    "Fantasma",
    "Dragón",
    "Siniestro",
    "Acero",
    "Hada",
)


# Solo se declaran factores distintos de 1. La tabla corresponde al sistema de
# 18 tipos vigente desde la sexta generacion.
EFECTIVIDAD = {
    "Normal": {"Roca": 0.5, "Fantasma": 0, "Acero": 0.5},
    "Fuego": {
        "Fuego": 0.5, "Agua": 0.5, "Planta": 2, "Hielo": 2,
        "Bicho": 2, "Roca": 0.5, "Dragón": 0.5, "Acero": 2,
    },
    "Agua": {
        "Fuego": 2, "Agua": 0.5, "Planta": 0.5, "Tierra": 2,
        "Roca": 2, "Dragón": 0.5,
    },
    "Eléctrico": {
        "Agua": 2, "Eléctrico": 0.5, "Planta": 0.5, "Tierra": 0,
        "Volador": 2, "Dragón": 0.5,
    },
    "Planta": {
        "Fuego": 0.5, "Agua": 2, "Planta": 0.5, "Veneno": 0.5,
        "Tierra": 2, "Volador": 0.5, "Bicho": 0.5, "Roca": 2,
        "Dragón": 0.5, "Acero": 0.5,
    },
    "Hielo": {
        "Fuego": 0.5, "Agua": 0.5, "Planta": 2, "Hielo": 0.5,
        "Tierra": 2, "Volador": 2, "Dragón": 2, "Acero": 0.5,
    },
    "Lucha": {
        "Normal": 2, "Hielo": 2, "Veneno": 0.5, "Volador": 0.5,
        "Psíquico": 0.5, "Bicho": 0.5, "Roca": 2, "Fantasma": 0,
        "Siniestro": 2, "Acero": 2, "Hada": 0.5,
    },
    "Veneno": {
        "Planta": 2, "Veneno": 0.5, "Tierra": 0.5, "Roca": 0.5,
        "Fantasma": 0.5, "Acero": 0, "Hada": 2,
    },
    "Tierra": {
        "Fuego": 2, "Eléctrico": 2, "Planta": 0.5, "Veneno": 2,
        "Volador": 0, "Bicho": 0.5, "Roca": 2, "Acero": 2,
    },
    "Volador": {
        "Eléctrico": 0.5, "Planta": 2, "Lucha": 2, "Bicho": 2,
        "Roca": 0.5, "Acero": 0.5,
    },
    "Psíquico": {
        "Lucha": 2, "Veneno": 2, "Psíquico": 0.5,
        "Siniestro": 0, "Acero": 0.5,
    },
    "Bicho": {
        "Fuego": 0.5, "Planta": 2, "Lucha": 0.5, "Veneno": 0.5,
        "Volador": 0.5, "Psíquico": 2, "Fantasma": 0.5,
        "Siniestro": 2, "Acero": 0.5, "Hada": 0.5,
    },
    "Roca": {
        "Fuego": 2, "Hielo": 2, "Lucha": 0.5, "Tierra": 0.5,
        "Volador": 2, "Bicho": 2, "Acero": 0.5,
    },
    "Fantasma": {
        "Normal": 0, "Psíquico": 2, "Fantasma": 2, "Siniestro": 0.5,
    },
    "Dragón": {"Dragón": 2, "Acero": 0.5, "Hada": 0},
    "Siniestro": {
        "Lucha": 0.5, "Psíquico": 2, "Fantasma": 2,
        "Siniestro": 0.5, "Hada": 0.5,
    },
    "Acero": {
        "Fuego": 0.5, "Agua": 0.5, "Eléctrico": 0.5, "Hielo": 2,
        "Roca": 2, "Acero": 0.5, "Hada": 2,
    },
    "Hada": {
        "Fuego": 0.5, "Lucha": 2, "Veneno": 0.5, "Dragón": 2,
        "Siniestro": 2, "Acero": 0.5,
    },
}


class Pokemon:
    def __init__(self, numero, nombre, tipos, debilidades, megaevolucion, gigamax):
        self.numero = numero
        self.nombre = nombre
        self.tipos = tipos
        self.debilidades = debilidades
        self.megaevolucion = megaevolucion
        self.gigamax = gigamax

    def __str__(self):
        return (
            f"#{self.numero:04d} {self.nombre} | Tipos: {', '.join(self.tipos)} | "
            f"Debilidades: {', '.join(self.debilidades)} | "
            f"Mega: {self.megaevolucion} | Gigamax: {self.gigamax}"
        )


def calcular_debilidades(tipos):
    """Con dos tipos se combinan los factores de efectividad."""
    debilidades = []
    for ataque in TIPOS:
        factor = 1
        for tipo in tipos:
            factor *= EFECTIVIDAD[ataque].get(tipo, 1)
        if factor > 1:
            debilidades.append(ataque)
    return debilidades


def cargar_pokemon():
    pokemones = []
    for dato in DATOS_POKEMON:
        pokemon = Pokemon(
            dato["numero"], dato["nombre"], dato["tipos"],
            calcular_debilidades(dato["tipos"]),
            dato["megaevolucion"], dato["gigamax"]
        )
        pokemones.append(pokemon)
    return pokemones


def crear_arboles(pokemones):
    arbol_nombre = BinaryTree()
    arbol_numero = BinaryTree()
    arbol_tipo = BinaryTree()

    orden = pokemones.copy()
    random.shuffle(orden)
    for pokemon in orden:
        arbol_nombre.insert_node(pokemon.nombre.lower(), pokemon)
        arbol_numero.insert_node(pokemon.numero, pokemon)
        for tipo in pokemon.tipos:
            nodo = arbol_tipo.search(tipo)
            if nodo is None:
                arbol_tipo.insert_node(tipo, [pokemon])
            else:
                nodo.other_values.append(pokemon)

    for lista in arbol_tipo.inorden():
        lista.sort(key=lambda pokemon: pokemon.nombre.lower())
    return arbol_nombre, arbol_numero, arbol_tipo


def mostrar_nombres(titulo, pokemones):
    print("\n" + titulo)
    for pokemon in pokemones:
        print(f"  #{pokemon.numero:04d} {pokemon.nombre}")


def main():
    pokemones = cargar_pokemon()
    arbol_nombre, arbol_numero, arbol_tipo = crear_arboles(pokemones)

    print("EJERCICIO 1 - POKEMON")
    print("Pokemon cargados:", len(pokemones))

    nodo = arbol_numero.search(25)
    print("\nBusqueda por numero 25:")
    if nodo is not None:
        print(nodo.other_values)

    print("\nBusqueda por proximidad 'bul':")
    for pokemon in arbol_nombre.proxy_search("bul"):
        print(pokemon)

    for tipo in ("Fantasma", "Fuego", "Acero", "Eléctrico"):
        nodo = arbol_tipo.search(tipo)
        if nodo is not None:
            mostrar_nombres("Pokemon de tipo " + tipo + ":", nodo.other_values)

    mostrar_nombres("Listado por numero:", arbol_numero.inorden())
    mostrar_nombres("Listado por nombre:", arbol_nombre.inorden())
    mostrar_nombres("Listado por nivel del arbol de nombres:", arbol_nombre.by_level())

    for nombre in ("Jolteon", "Lycanroc", "Tyrantrum"):
        nodo = arbol_nombre.search(nombre.lower())
        if nodo is not None:
            atacante = nodo.other_values
            debiles = []
            for pokemon in arbol_nombre.inorden():
                if pokemon.numero != atacante.numero:
                    for tipo in atacante.tipos:
                        if tipo in pokemon.debilidades:
                            debiles.append(pokemon)
                            break
            mostrar_nombres("Debiles frente a " + nombre + ":", debiles)

    print("\nCantidad de Pokemon por tipo:")
    # Se recorre el arbol de tipos para obtener cada clave y su cantidad.
    def mostrar_cantidad_tipo(root):
        if root is not None:
            mostrar_cantidad_tipo(root.left)
            print(f"  {root.value}: {len(root.other_values)}")
            mostrar_cantidad_tipo(root.right)

    mostrar_cantidad_tipo(arbol_tipo.root)

    cantidad_mega = 0
    cantidad_gigamax = 0
    for pokemon in pokemones:
        if pokemon.megaevolucion:
            cantidad_mega += 1
        if pokemon.gigamax:
            cantidad_gigamax += 1
    print("\nPokemon con megaevolucion:", cantidad_mega)
    print("Pokemon con Gigamax:", cantidad_gigamax)


if __name__ == "__main__":
    main()
