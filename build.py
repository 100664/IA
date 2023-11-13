from Helper import *
from Node import *

import math
from queue import Queue, LifoQueue

import networkx as nx
import matplotlib.pyplot as plt

class Build:
    def __init__(self, path):
        self.nodes = []
        self.graph = {}
        self.coordinates_to_node = {}
        self.helper = Helper(path)

#--------------------------------criação dos nodos e conexões----------------#

    def expand_graph(self):
        e_x, e_y = self.helper.get_encomenda_pi()
        node_e = Node(0, e_x, e_y)
        self.nodes.append(node_e)
        self.graph[0] = []
        self.coordinates_to_node[(e_x, e_y)] = node_e

        destinations = {}  # Dicionário para armazenar nodos destino (1 a 9)

        for y, line in enumerate(self.helper.map):
            for x, symbol in enumerate(line):
                coordinates = (x, y)

                if symbol == '-':
                    new_node = self.add_node_if_not_exists(coordinates)

                    # Conecte o novo nó aos nós vizinhos (caminhos possíveis)
                    self.connect_nodes(new_node, x, y)

                elif symbol.isdigit() and 1 <= int(symbol) <= 9:
                    node_id = int(symbol)
                    new_node = self.add_node_if_not_exists(coordinates, node_id)
                    destinations[node_id] = new_node

        # Mantenha as conexões já existentes
        for node_id, connections in self.graph.items():
            for neighbor_id in connections:
                neighbor_node = self.get_node_by_id(neighbor_id)
                if neighbor_node:
                    self.connect_nodes(neighbor_node, neighbor_node.x, neighbor_node.y)

        # Conecte todos os destinos entre si
        self.connect_destinations(destinations)

    def add_node_if_not_exists(self, coordinates, node_id=None):
        new_node = self.coordinates_to_node.get(coordinates)

        if new_node is None:
            if node_id is None:
                node_id = len(self.nodes) + 10
            new_node = Node(node_id, *coordinates)
            self.nodes.append(new_node)
            self.graph[node_id] = []
            self.coordinates_to_node[coordinates] = new_node

        return new_node

    def connect_destinations(self, destinations):
        for node_id, node in destinations.items():
            if node is not None:
                x, y = node.x, node.y
                for dest_id, dest_node in destinations.items():
                    if dest_node is not None and dest_node != node:
                        dist = abs(dest_node.x - x) + abs(dest_node.y - y)
                        if dist == 1 and dest_node.node_id not in self.graph[node_id]:
                            self.graph[node_id].append(dest_node.node_id)
                            self.graph[dest_node.node_id].append(node_id)


    def connect_nodes(self, node, x, y):
        # Conecte o nó aos nós vizinhos (caminhos possíveis)
        possible_neighbors = [
        (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1),
        (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)
        ]
        for neighbor_x, neighbor_y in possible_neighbors:
            coordinates = (neighbor_x, neighbor_y)
            neighbor_node = self.coordinates_to_node.get(coordinates)

            if neighbor_node:
                # Conecte os nodos usando listas para evitar duplicatas
                if neighbor_node.node_id not in self.graph[node.node_id]:
                    self.graph[node.node_id].append(neighbor_node.node_id)
                if node.node_id not in self.graph[neighbor_node.node_id]:
                    self.graph[neighbor_node.node_id].append(node.node_id)

    def get_node_by_id(self, node_id):
        for node in self.nodes:
            if node.node_id == node_id:
                return node
        return None

#-----------------------prints + desenhos---------------------------------#

    def visualize_graph(self, directed=False):
        G = nx.Graph() if not directed else nx.DiGraph()

        for node in self.nodes:
            G.add_node(node.node_id, pos=(node.x, -node.y))  # Invertemos o eixo y para corresponder à representação do mapa

        for node_id, connections in self.graph.items():
            for neighbor_id in connections:
                G.add_edge(node_id, neighbor_id)

        pos = nx.get_node_attributes(G, 'pos')

        labels = {node.node_id: node.node_id for node in self.nodes}

        nx.draw(G, pos, with_labels=True, labels=labels, font_weight='bold', node_size=700, font_size=8, node_color='skyblue', edge_color='gray', arrowsize=20, connectionstyle='arc3,rad=0.1')

        plt.show()

    def print_graph (self):
        for node in self.nodes:
            print(f"Node {node.node_id} - Coordenadas: ({node.x}, {node.y})")
            print(f"Conexões: {list(self.graph[node.node_id])}")

#---------------------------------procura não informada (DFS)------------------------------#

    def dfs(self, start_node, goal_node):
        parent = {}
        distances = {node.node_id: self.distance(node, goal_node) for node in self.nodes}

        def dfs_recursive(current_node):
            if current_node == goal_node:
                return True

            neighbors = self.graph[current_node]
            neighbors.sort(key=lambda neighbor_id: distances[neighbor_id], reverse=True)

            for neighbor_id in neighbors:
                if neighbor_id not in parent:
                    parent[neighbor_id] = current_node
                    if dfs_recursive(neighbor_id):
                        return True

            return False

        parent[start_node] = None
        dfs_recursive(start_node)

        if goal_node not in parent:
            return None

        path = []
        current_node = goal_node
        while current_node is not None:
            path.append(current_node)
            current_node = parent[current_node]

        return path[::-1]