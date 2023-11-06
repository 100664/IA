from Helper import *

class Graph:

    def __init__ (self, path):

        self.nodes = []
        self.graph = {}
        #self.h = {}
        self.helper = Helper(path)
        encomenda_pi = self.helper.get_encomenda_pi()
        fst_node = Node(0, encomenda_pi[0], encomenda_pi[1])
