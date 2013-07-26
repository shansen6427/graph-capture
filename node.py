"""
  node.py
  The node class represents capture nodes on the graph.  Captures nodes
  generate troops and can send these troops to capture other nodes.
  One player must control all nodes to achieve victory.
"""

class Node():

    def __init__(self, name = 0, size = 2, x = 0, y = 0, edges = []):
        self.name = name
        self.size = size
        self.x = x
        self.y = y
        self.edges = edges

    def __eq__(self, n):
        for x in range(len(self.edges)):
            if self.edges[x] != n.edges[x]:
                return false
 
        return (self.name == n.name and
            self.size == n.size and
            self.x == n.x and
            self.y == n.y)
