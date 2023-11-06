from Helper import *

class Graph:

    def __init__ (self, path):

        self.nodes = []
        self.graph = {}
        #self.h = {}
        self.helper = Helper(path)
        encomenda_pi = self.helper.get_encomenda_pi()
        node1 = Node(0, encomenda_pi[0], encomenda_pi[1]) # O node tem o 0 pois a posição de onde parte a encomenda ficará no grafo com o indice 0
        self.nodes.append(node1) #coloco o nodolo de onde parte a encomeda na lista de nodulos
        self.graph[0]=list() #o graph[0] é uma lista vazias pois o nodo1 de id = 0 nao tem "conexões"
        

