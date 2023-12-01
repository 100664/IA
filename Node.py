class Node:
    def __init__(self, node_id, x, y):
        self.node_id = int (node_id)
        self.x = x
        self.y = y

    def __lt__(self, other):
        
        return self.node_id < other.node_id

    








    #importante: a heurística vai ser a distância de Manhattan, ou seja, eu vou calcular
    #  a distância entre o nó atual/nó partida e o nó destino e depoi vou usar essa conta 
    # para para fazer a procura.

    # temos que tratar as colisões como se o nodo estivesse ocupado, ou seja, como se fosse uma parede. Claramente o 
    #boneco só terá percepção disso quando "bater com o nariz" no nodo que já está ocupado.