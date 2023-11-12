class Node:
    def __init__(self, node_id, x, y):
        self.node_id = node_id
        self.x = x
        self.y = y
        self.connections = []

    def __str__(self):
        return f"Node {self.node_id} - Coordenadas: ({self.x}, {self.y})\nConexões: {self.connections}"