
"""
  node.py
  The node class represents capture nodes on the graph.  Captures nodes
  generate troops and can send these troops to capture other nodes.
  One player must control all nodes to achieve victory.
"""

class Node(object):

    def __init__(self, name = 0, size = 2, x = 0, y = 0, edges = []):
        self._name = name
        self._size = size
        self._x = x
        self._y = y
        self._edges = edges

    def __eq__(self, n):
        return (self._name == n.getName() and
            self._size == n.getSize() and
            self._x == n.getX() and
            self._y == n.getY() and
            set(self._edges) == set(n.getEdges()))

    def getName(self):
        return self._name

    def getSize(self):
        return self._size

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def getEdges(self):
        return list(self._edges)
