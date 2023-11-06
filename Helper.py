from parsezim import parse
from Node import *

from colorama import Fore, Back, Style

class Helper: 

    def __init__ (self, path):
        self.path = path    
        self.map = parse(path)

    def get_encomenda_pi(self):
        x = -1
        for line in self.map:
            x += 1
            y = -1
            for pos in self.map[x]:
                y += 1
                if (pos == 'E'):
                    return [y,x]
