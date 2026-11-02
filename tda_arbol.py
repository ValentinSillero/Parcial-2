"""Arbol binario de busqueda AVL, con los metodos usados en clase."""

from tda_cola import Cola, arribo, atencion, cola_vacia


class Node:
    def __init__(self, value=None, other_values=None):
        self.value = value
        self.left = None
        self.right = None
        self.other_values = other_values
        self.height = 0


class BinaryTree:
    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        return root.height

    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = max(left_height, right_height) + 1

    def insert_node(self, value, other_value=None):
        def __insert_node(root, value, other_value):
            if root is None:
                root = Node(value, other_value)
            elif value < root.value:
                root.left = __insert_node(root.left, value, other_value)
            else:
                root.right = __insert_node(root.right, value, other_value)
            root = self.auto_balance(root)
            self.update_height(root)
            return root

        self.root = __insert_node(self.root, value, other_value)

    def search(self, value):
        def __search(root, value):
            if root is None:
                return None
            if root.value == value:
                return root
            if value < root.value:
                return __search(root.left, value)
            return __search(root.right, value)

        return __search(self.root, value)

    def auto_balance(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        return aux

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            return self.simple_rotation(root, True)
        root.right = self.simple_rotation(root.right, True)
        return self.simple_rotation(root, False)

    def inorden(self):
        """Devuelve los registros ordenados segun la clave del arbol."""
        resultado = []

        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                resultado.append(root.other_values)
                __inorden(root.right)

        __inorden(self.root)
        return resultado

    def by_level(self):
        """Recorre por nivel utilizando una cola, como en clase."""
        resultado = []
        pendientes = Cola()
        if self.root is not None:
            arribo(pendientes, self.root)
        while not cola_vacia(pendientes):
            node = atencion(pendientes)
            resultado.append(node.other_values)
            if node.left is not None:
                arribo(pendientes, node.left)
            if node.right is not None:
                arribo(pendientes, node.right)
        return resultado

    def proxy_search(self, prefix):
        """Busca nombres que contengan el texto, igual que proxy_search de clase."""
        resultado = []
        prefix = prefix.lower()

        def __proxy_search(root):
            if root is not None:
                __proxy_search(root.left)
                if prefix in root.value:
                    resultado.append(root.other_values)
                __proxy_search(root.right)

        if prefix:
            __proxy_search(self.root)
        return resultado
