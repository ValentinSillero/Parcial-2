"""Ejercicio 2: grafo no dirigido de personajes de Star Wars."""

from tda_grafo import Graph


PERSONAJES_EPISODIOS = {
    "Luke Skywalker": {3, 4, 5, 6, 7, 8, 9},
    "Darth Vader": {3, 4, 5, 6, 9},
    "Yoda": {1, 2, 3, 5, 6, 8, 9},
    "Boba Fett": {2, 4, 5, 6},
    "C-3PO": set(range(1, 10)),
    "Leia": {3, 4, 5, 6, 7, 8, 9},
    "Rey": {7, 8, 9},
    "Kylo Ren": {7, 8, 9},
    "Chewbacca": {3, 4, 5, 6, 7, 8, 9},
    "Han Solo": {4, 5, 6, 7, 9},
    "R2-D2": set(range(1, 10)),
    "BB-8": {7, 8, 9},
}


def cargar_grafo():
    grafo = Graph(is_dir=False)
    for nombre in PERSONAJES_EPISODIOS:
        grafo.add_vertex(nombre, PERSONAJES_EPISODIOS[nombre])

    nombres = list(PERSONAJES_EPISODIOS)
    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            compartidos = PERSONAJES_EPISODIOS[nombres[i]] & PERSONAJES_EPISODIOS[nombres[j]]
            if compartidos:
                grafo.add_edge(len(compartidos), nombres[i], nombres[j])
    return grafo


def main():
    grafo = cargar_grafo()
    print("EJERCICIO 2 - STAR WARS")
    print("Personajes cargados:", len(grafo))

    print("\nArboles de expansion minima (Prim):")
    for origen in ("C-3PO", "Yoda", "Leia"):
        arbol, total = grafo.prim(origen)
        print("\nDesde", origen)
        for primero, segundo, peso in arbol:
            print(f"  {primero} -- {segundo}: {peso}")
        print("  Peso total:", total)

    maximo = 0
    pares = []
    for vertex in grafo:
        for edge in vertex.edges:
            # Cada arista se recorre una sola vez (grafo no dirigido).
            if vertex.value < edge.destination:
                if edge.weight > maximo:
                    maximo = edge.weight
                    pares = [(vertex.value, edge.destination)]
                elif edge.weight == maximo:
                    pares.append((vertex.value, edge.destination))

    print("\nMaximo de episodios compartidos:", maximo)
    for primero, segundo in pares:
        print(" ", primero, "--", segundo)

    print("\nCaminos mas cortos (Dijkstra):")
    for origen, destino in (("C-3PO", "R2-D2"), ("Yoda", "Darth Vader")):
        camino, peso = grafo.shortest_path(origen, destino)
        print(f"  {origen} a {destino}: {' -> '.join(camino)} (peso: {peso})")

    print("\nPersonajes presentes en los nueve episodios:")
    for vertex in grafo:
        if len(vertex.other_values) == 9:
            print(" ", vertex.value)


if __name__ == "__main__":
    main()
