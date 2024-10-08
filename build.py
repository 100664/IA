from Helper import *
from Node import *
from Encomenda import *

import math
from queue import Queue, PriorityQueue
import heapq

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
        self.graph[node.node_id] = []


    def add_edge(self, node1, node2):
        self.graph[node1.node_id].append(node2.node_id)
        self.graph[node2.node_id].append(node1.node_id)

    def find_node_id_by_morada(self, morada):
        for node in self.nodes:
            if node.node_id == morada:
                return node.node_id
        return None

    def get_node_by_id(self, node_id):
        for node in self.nodes:
            if node.node_id == node_id:
                return node
        return None
    
    def manhattan_distance(self, node1, node2):
        return abs(node1.x - node2.x) + abs(node1.y - node2.y)
    
    def heuristic(self, node, goal_node):
        return self.manhattan_distance(node, goal_node)
    
    def chebyshev_distance(self, node1, node2):
        return max(abs(node1.x - node2.x), abs(node1.y - node2.y))

    def heuristic_chebyshev(self, node, goal_node):
        return self.chebyshev_distance(node, goal_node)
    
    
    @staticmethod
    def obter_encomenda_por_id(id_input, lista_encomendas):
        for encomenda in lista_encomendas:
            if encomenda.get_id() == id_input:
                return encomenda
        return None

    def check_collision(self, path, transportadora1):
        for node_id in path:
            if node_id in transportadora1:
                return True
        return False
    
    def reconstruct_path(self, came_from, start_node_id, goal_node_id):
        current_node_id = goal_node_id
        path = [current_node_id]

        while current_node_id != start_node_id:
            current_node_id = came_from[current_node_id]
            path.insert(0, current_node_id)

        return path
    
    def euclidean_distance(self, node1, node2):
        return math.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)

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
                # Conecte os nodos usando listas para evitar duplicatasa
                if neighbor_node.node_id not in self.graph[node.node_id]:
                    self.graph[node.node_id].append(neighbor_node.node_id)
                if node.node_id not in self.graph[neighbor_node.node_id]:
                    self.graph[neighbor_node.node_id].append(node.node_id)

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


#-----------------------funções de procura---------------------------------#

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

#-----------------------função de procura informada (A*)---------------------------------#

    def a_star(self, start_node_id, goal_node_id, heuristic_type="manhattan"):
        start_node = self.get_node_by_id(start_node_id)
        goal_node = self.get_node_by_id(goal_node_id)
        
        if start_node and goal_node:
            open_set = PriorityQueue()
            open_set.put((0, start_node))
            came_from = {}
            g_score = {node.node_id: math.inf for node in self.nodes}
            g_score[start_node.node_id] = 0

            while not open_set.empty():
                _, current_node = open_set.get()

                if current_node == goal_node:
                    return self.reconstruct_path(came_from, start_node_id, goal_node_id)

                for neighbor_id in self.graph[current_node.node_id]:
                    neighbor_node = self.get_node_by_id(neighbor_id)
                    tentative_g_score = g_score[current_node.node_id] + 1

                    if tentative_g_score < g_score[neighbor_node.node_id]:
                        g_score[neighbor_node.node_id] = tentative_g_score

                        if heuristic_type == "manhattan":
                            priority = tentative_g_score + self.manhattan_distance(neighbor_node, goal_node)
                        elif heuristic_type == "chebyshev":
                            priority = tentative_g_score + self.chebyshev_distance(neighbor_node, goal_node)
                        else:
                            raise ValueError("Invalid heuristic type")

                        open_set.put((priority, neighbor_node))
                        came_from[neighbor_node.node_id] = current_node.node_id

            return None
        else:
            print("Nó inicial ou nó objetivo não encontrado.")
            return None
           
#-----------------------função greedy ---------------------------------#   

    def greedy_best_first_search(self, start_node_id, goal_node_id, heuristic_type="manhattan"):
        start_node = self.get_node_by_id(start_node_id)
        goal_node = self.get_node_by_id(goal_node_id)
        
        if start_node and goal_node:
            open_set = PriorityQueue()
            
            if heuristic_type == "manhattan":
                open_set.put((self.heuristic(start_node, goal_node), start_node))
            elif heuristic_type == "chebyshev":
                open_set.put((self.heuristic_chebyshev(start_node, goal_node), start_node))
            else:
                raise ValueError("Invalid heuristic type")

            came_from = {}

            while not open_set.empty():
                _, current_node = open_set.get()

                if current_node == goal_node:
                    return self.reconstruct_path(came_from, start_node_id, goal_node_id)

                for neighbor_id in self.graph[current_node.node_id]:
                    neighbor_node = self.get_node_by_id(neighbor_id)

                    if neighbor_node.node_id not in came_from:
                        if heuristic_type == "manhattan":
                            open_set.put((self.manhattan_distance(neighbor_node, goal_node), neighbor_node))
                        elif heuristic_type == "chebyshev":
                            open_set.put((self.chebyshev_distance(neighbor_node, goal_node), neighbor_node))
                        else:
                            raise ValueError("Invalid heuristic type")

                        came_from[neighbor_node.node_id] = current_node.node_id

            return None
        else:
            print("Nó inicial ou nó objetivo não encontrado.")
            return None


        
    
#-----------------------função de print (just 1)---------------------------------#       

    def print_paths_for_all_encomendas(self, start_node_id, encomendas, search_algorithm='dfs', heuristic_type = "manhattan"):
        all_paths = {}
        
        for encomenda in encomendas:
            goal_node_id = self.find_node_id_by_morada(encomenda.morada)
            path = None

            if search_algorithm == 'dfs':
                path = self.dfs(start_node_id, goal_node_id)
            elif search_algorithm == 'bfs':
                path = self.bfs(start_node_id, goal_node_id)
            elif search_algorithm == 'a_star':
                path = self.a_star(start_node_id, goal_node_id, heuristic_type)
            elif search_algorithm == 'greedy':
                path = self.greedy_best_first_search(start_node_id, goal_node_id, heuristic_type)

            if path:
                all_paths[encomenda.id] = path
            else:
                print(f"Não foi possível encontrar um caminho para a encomenda com ID {encomenda.id}")
                return {}

        return all_paths

    
    def find_best_path(self, all_paths):
        best_encomenda_id, best_path = min(all_paths.items(), key=lambda item: (
            len(item[1]),
            getattr(item[1][-1], 'get_peso', lambda: 0)(),
            getattr(item[1][-1], 'get_id', lambda: 0)()
        ), default=(None, None))
        return best_encomenda_id, best_path
    
    def calculate_and_print_best_path(self, ponto_inicial, lista_encomendas, search_algorithm='dfs', heuristic_type = "manhattan"):
        ordered_deliveries = []
        ponto_atual = ponto_inicial

        while lista_encomendas:
            all_paths = self.print_paths_for_all_encomendas(ponto_atual, lista_encomendas, search_algorithm,heuristic_type)
            if (all_paths == {}):
                return []
            else:
                best_id, best_path = self.find_best_path(all_paths)

                if best_id:
                    best_encomenda = next(encomenda for encomenda in lista_encomendas if encomenda.get_id() == best_id)
                    ordered_deliveries.append((best_encomenda.get_id(), best_path))
                    lista_encomendas.remove(best_encomenda)
                    ponto_atual = best_encomenda.get_morada()
        return ordered_deliveries
    
    def get_specific_encomenda_path(self, target_encomenda_id, ordered_deliveries):
        target_encomenda_id = str(target_encomenda_id)
        for encomenda_id, path in ordered_deliveries:
            if str(encomenda_id) == target_encomenda_id:
                return path
        return []
  

#-----------------------função de procura não Informada - BFS (evita colisões)---------------------------------#

    def bfs_2nd(self, start_node_id, goal_node_id, player1_path):
        # Inicializa as variáveis
        visited = set()
        queue = Queue()
        queue.put([start_node_id])
        collisions = []  # Lista para rastrear os nodos de colisão

        while not queue.empty():
            path = queue.get()
            node_id = path[-1]

            if node_id not in visited:
                visited.add(node_id)

                if node_id == goal_node_id:
                    return path, collisions

                if node_id != 0:  # Ignora o nodo especial 0
                    # Verificar colisões com o caminho do player 1
                    if self.check_collision([node_id], player1_path):
                        collisions.append(node_id)
                        continue  # Ignora este nodo e tenta próximo

                for neighbor_id in self.graph[node_id]:
                    if neighbor_id not in visited:
                        new_path = list(path)
                        new_path.append(neighbor_id)
                        queue.put(new_path)

        return [], collisions

    def check_collision(self, path, player1_path):
        for node_id in path:
            if node_id in player1_path:
                return True
        return False

        
#-----------------------função de procura informada - DFS (evita colisões)---------------------------------#
    
    def dfs_2nd(self, start_node_id, goal_node_id, player1_path):
        visited = set()
        stack = [ [start_node_id] ]
        collisions = []  # Lista para rastrear os nodos de colisão

        while stack:
            path = stack.pop()
            node_id = path[-1]

            if node_id not in visited:
                visited.add(node_id)

                if node_id == goal_node_id:
                    return path, collisions

                if node_id != 0:  # Ignora o nodo especial 0
                    # Verificar colisões com o caminho do player 1
                    if self.check_collision([node_id], player1_path):
                        collisions.append(node_id)
                        continue  # Ignora este nodo e tenta próximo

                # Adiciona vizinhos não visitados à pilha
                for neighbor_id in self.graph[node_id]:
                    if neighbor_id not in visited:
                        new_path = list(path)
                        new_path.append(neighbor_id)
                        stack.append(new_path)

        return [], collisions

#-----------------------função de procura informada - A* (evita colisões)---------------------------------#

    def a_estrela_2nd(self, start_node_id, goal_node_id, player1_path):
        open_set = [(0, start_node_id, [])]  # (f_cost, node_id, path)
        closed_set = set()
        collisions = []  # Lista para rastrear os nodos de colisão

        while open_set:
            f_cost, current_node_id, path = heapq.heappop(open_set)

            if current_node_id in closed_set:
                continue

            path = path + [current_node_id]

            if current_node_id == goal_node_id:
                return path, collisions

            closed_set.add(current_node_id)

            if current_node_id != 0:  # Ignora o nodo especial 0
                # Verificar colisões com o caminho do player 1
                if self.check_collision([current_node_id], player1_path):
                    collisions.append(current_node_id)
                    continue  # Ignora este nodo e tenta próximo

            for neighbor_id in self.graph[current_node_id]:
                if neighbor_id not in closed_set:
                    g_cost = len(path)
                    h_cost = self.heuristic(self.get_node_by_id(neighbor_id), self.get_node_by_id(goal_node_id))
                    f_cost = g_cost + h_cost
                    heapq.heappush(open_set, (f_cost, neighbor_id, path))

        return [], collisions
    
#-----------------------função de procura informada - greedy (evita colisões)---------------------------------#

    def greedy_2nd(self, start_node_id, goal_node_id, player1_path):
        open_set = [(0, start_node_id, [])]  # (h_cost, node_id, path)
        closed_set = set()
        collisions = []  # Lista para rastrear os nodos de colisão

        while open_set:
            h_cost, current_node_id, path = heapq.heappop(open_set)

            if current_node_id in closed_set:
                continue

            path = path + [current_node_id]

            if current_node_id == goal_node_id:
                return path, collisions

            closed_set.add(current_node_id)

            if current_node_id != 0:  # Ignora o nodo especial 0
                # Verificar colisões com o caminho do player 1
                if self.check_collision([current_node_id], player1_path):
                    collisions.append(current_node_id)
                    continue  # Ignora este nodo e tenta próximo

            for neighbor_id in self.graph[current_node_id]:
                if neighbor_id not in closed_set:
                    h_cost = self.heuristic(self.get_node_by_id(neighbor_id), self.get_node_by_id(goal_node_id))
                    heapq.heappush(open_set, (h_cost, neighbor_id, path))

        return [], collisions

#-----------------------printar_grafo sem colisions---------------------------------#

    def get_node_index_by_id(self, node_id):
        for i, node in enumerate(self.nodes):
            if node.node_id == node_id:
                return i
        return None

    def draw_directed_path(self, path):
        G = nx.DiGraph()
        for node_id in self.graph.keys():
            G.add_node(node_id, pos=(self.get_node_by_id(node_id).x, -self.get_node_by_id(node_id).y))
        for i in range(len(path) - 1):
            node_from, node_to = path[i], path[i + 1]
            G.add_edge(node_from, node_to)
        node_colors = {node: 'green' if node in path else 'skyblue' for node in G.nodes}
        pos = nx.get_node_attributes(G, 'pos')
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, font_size=8, node_color=list(node_colors.values()), edge_color='gray', connectionstyle='arc3,rad=0.1', arrows=True, arrowstyle='->', arrowsize=20)

        plt.show()

#---------------------Draw colision------------------------------------------#

    def draw_filtered_path_with_collisions(self, path, collisions):
        filtered_collisions = self.filter_collisions(path, collisions) 
        G = nx.DiGraph()
        for node_id in self.graph.keys():
            G.add_node(node_id, pos=(self.get_node_by_id(node_id).x, -self.get_node_by_id(node_id).y))
        for i in range(len(path) - 1):
            node_from, node_to = path[i], path[i + 1]
            G.add_edge(node_from, node_to)

        node_colors = {node: 'green' if node in path else 'skyblue' for node in G.nodes}
        edge_colors = {edge: 'black' for edge in G.edges}
        edges_to_remove = []
        for collision_node in filtered_collisions:
            if collision_node in G.nodes:
                node_colors[collision_node] = 'red'
                edges_to_remove.extend(G.out_edges(collision_node)) 
        G.remove_edges_from(edges_to_remove)

        pos = nx.get_node_attributes(G, 'pos')
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, font_size=8,
                node_color=list(node_colors.values()), edge_color=list(edge_colors.values()),
                connectionstyle='arc3,rad=0.1', arrows=True, arrowstyle='->', arrowsize=10)

        plt.show()


    def filter_collisions(self, path, collisions):
        filtered_collisions = []
        if (path == []):
            return collisions
        else:
            for collision_node in collisions:
                close_to_path = any(self.euclidean_distance(self.get_node_by_id(path_node), self.get_node_by_id(collision_node)) <= 1 for path_node in path)

                if close_to_path:
                    filtered_collisions.append(collision_node)

            return filtered_collisions
