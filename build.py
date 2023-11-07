from Helper import *
from Node import *

import math
from queue import Queue

import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
import matplotlib.pyplot as plt  # ide

class Build:

    def __init__ (self, path):

        self.nodes = []
        self.graph = {}
        #self.h = {}
        self.helper = Helper(path)
        encomenda_pi = self.helper.get_encomenda_pi()
        node1 = Node(0, encomenda_pi[0], encomenda_pi[1]) # O node tem o 0 pois a posição de onde parte a encomenda ficará no grafo com o indice 0
        self.nodes.append(node1) #coloco o nodolo de onde parte a encomeda na lista de nodulos
        self.graph[0]= [] #o graph[0] é uma lista vazias pois o nodo1 de id = 0 nao tem "conexões"

    def expand_graph(self):
        # Passo 1: Encontre as coordenadas da letra "E"
        e_x, e_y = self.helper.get_encomenda_pi()

        # Passo 2: Crie um nó com ID 0 nas coordenadas da letra "E"
        node_e = Node(0, e_x, e_y)
        #self.nodes.append(node_e)
        self.graph[0] = []

        # Passo 3 e 4: Percorra as linhas da lista de strings
        # para criar nós para caminhos "-" e conectá-los
        for y, line in enumerate(self.helper.map):
            for x, symbol in enumerate(line):
                if symbol == 'E':
                   break
                if symbol == '-':
                    node_id = len(self.nodes)+9  # Novo ID único
                    new_node = Node(node_id, x, y)
                    self.nodes.append(new_node)
                    self.graph[node_id] = []

                    # Conecte o novo nó aos nós vizinhos (caminhos possíveis)
                    self.connect_nodes(new_node, x, y)

                elif symbol.isdigit() and 1 <= int(symbol) <= 9:
                    # Passo 5: Crie nós para destinos (números 1 a 9)
                    node_id = int(symbol)
                    new_node = Node(node_id, x, y)
                    self.nodes.append(new_node)
                    self.graph[node_id] = []

    def connect_nodes(self, node, x, y):
        # Conecte o nó aos nós vizinhos (caminhos possíveis)
        possible_neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for neighbor_x, neighbor_y in possible_neighbors:
            for existing_node in self.nodes:
                if (existing_node.x, existing_node.y) == (neighbor_x, neighbor_y):
                    self.graph[node.node_id].append(existing_node.node_id)
                    self.graph[existing_node.node_id].append(node.node_id)

