class Node:
    def __init__(self, node_id, x, y):
        self.node_id = int (node_id)
        self.x = x
        self.y = y

    def __lt__(self, other):
        
        return self.node_id < other.node_id