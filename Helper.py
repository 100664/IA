from parsezim import parse
from Node import *

class Helper:
    def __init__(self, path):
        self.path = path
        self.map = parse(path)

    def get_encomenda_pi(self):
        x = -1
        for line in self.map:
            x += 1
            y = -1
            for pos in self.map[x]:
                y += 1
                if pos == 'E':
                    return [y, x]

    def add_connection(self, node1, node2):
        # Adicione uma conexão entre node1 e node2
        if node1 and node2:
            node1.add_connection(node2)
            node2.add_connection(node1)

    def is_valid_position(self, x, y):
        # Verifique se a posição (x, y) é uma posição válida no mapa
        if 0 <= y < len(self.map) and 0 <= x < len(self.map[y]):
            return self.map[y][x] != 'X'  # Não é uma parede
        return False

    def is_destination(self, x, y):
        # Verifique se a posição (x, y) é um destino (número de 0 a 9)
        if 0 <= y < len(self.map) and 0 <= x < len(self.map[y]):
            return '0' <= self.map[y][x] <= '9'
        return False
