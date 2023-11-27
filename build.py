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

#------------auxiliares----------------#

    def add_node(self, node):
        self.nodes.append(node)
        self.graph[node.node_id] = []  # Use node.node_id como chave


    def add_edge(self, node1, node2):
        self.graph[node1.node_id].append(node2.node_id)
        self.graph[node2.node_id].append(node1.node_id)



#--------------------------------criação dos nodos e conexões----------------#

    def expand_graph(self):
        e_x, e_y = self.helper.get_encomenda_pi()
        node_e = Node(0, e_x, e_y)
        self.add_node(node_e)
        self.graph[0] = []
        self.coordinates_to_node[(e_x, e_y)] = node_e

        destinations = {}

        for y, line in enumerate(self.helper.map):
            for x, symbol in enumerate(line):
                coordinates = (x, y)

                if symbol == '-':
                    new_node = self.add_node_if_not_exists(coordinates)
                    self.connect_nodes(new_node, x, y)

                elif symbol.isdigit() and 1 <= int(symbol) <= 9:
                    node_id = int(symbol)
                    new_node = self.add_node_if_not_exists(coordinates, node_id)
                    destinations[node_id] = new_node

        for node_id, connections in self.graph.items():
            for neighbor_id in connections:
                neighbor_node = self.get_node_by_id(neighbor_id)
                if neighbor_node:
                    self.connect_nodes(neighbor_node, neighbor_node.x, neighbor_node.y)

        self.connect_destinations(destinations)


    def add_node_if_not_exists(self, coordinates, node_id=None):
        new_node = self.coordinates_to_node.get(coordinates)

        if new_node is None:
            if node_id is None:
                node_id = len(self.nodes) + 10
            new_node = Node(node_id, *coordinates)
            self.add_node(new_node)
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

    def visualize_graph(self):#, directed=False):
        G = nx.Graph() #if not directed else nx.DiGraph()

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

#-----------------------função de procura não informada (DFS)---------------------------------#

    def dfs(self, start_node_id, goal_node_id, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(start_node_id)
        path = path + [start_node_id]

        if start_node_id == goal_node_id:
            return path

        for neighbor_id in self.graph[start_node_id]:
            if neighbor_id not in visited:
                new_path = self.dfs(neighbor_id, goal_node_id, visited, path)
                if new_path:
                    return new_path

        return None

    def find_path_dfs(self, start_node_id, goal_node_id):
        start_node = self.get_node_by_id(start_node_id)
        goal_node = self.get_node_by_id(goal_node_id)
        if start_node and goal_node:
            return self.dfs(start_node.node_id, goal_node.node_id)
        else:
            print("Nó inicial ou nó objetivo não encontrado.")
            return None

#-----------------------função de procura não informada (BFS)---------------------------------#

    def bfs(self, start_node_id, goal_node_id):
        visited = set()
        queue = Queue()
        queue.put([start_node_id])

        while not queue.empty():
            path = queue.get()
            node_id = path[-1]

            if node_id not in visited:
                visited.add(node_id)

                if node_id == goal_node_id:
                    return path

                for neighbor_id in self.graph[node_id]:
                    new_path = list(path)
                    new_path.append(neighbor_id)
                    queue.put(new_path)

        return None
    
    def find_path_bfs(self, start_node_id, goal_node_id):
        start_node = self.get_node_by_id(start_node_id)
        goal_node = self.get_node_by_id(goal_node_id)
        if start_node and goal_node:
            return self.bfs(start_node.node_id, goal_node.node_id)
        else:
            print("Nó inicial ou nó objetivo não encontrado.")
            return None

#-----------------------printar_grafo DFS e BFS---------------------------------#

    def get_node_index_by_id(self, node_id):
        for i, node in enumerate(self.nodes):
            if node.node_id == node_id:
                return i
        return None

    def highlight_path(self, path):
        node_colors = {node.node_id: 'skyblue' for node in self.nodes}

        for node_id in path:
            if node_id in node_colors:
                node_colors[node_id] = 'green'

        G = nx.Graph()

        for i, node in enumerate(self.nodes):
            G.add_node(node.node_id, pos=(node.x, -node.y), color=node_colors[node.node_id])

        for node_id, connections in self.graph.items():
            for neighbor_id in connections:
                if node_id in path and neighbor_id in path:
                    G.add_edge(node_id, neighbor_id, color='green')
                else:
                    G.add_edge(node_id, neighbor_id, color='gray')

        pos = nx.get_node_attributes(G, 'pos')
        edge_colors = nx.get_edge_attributes(G, 'color')

        labels = {node.node_id: node.node_id for node in self.nodes}

        nx.draw(G, pos, with_labels=True, labels=labels, font_weight='bold', node_size=700, font_size=8, node_color=list(node_colors.values()))

        for edge, color in edge_colors.items():
            nx.draw_networkx_edges(G, pos, edgelist=[edge], edge_color=color, arrows=True, connectionstyle='arc3,rad=0.1')

        plt.show()

