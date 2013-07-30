
"""
  capmap.py
  The map class.  Capmap reads graph files (as yet unnamed), turns them
  into map objects and returns that to the game engine.  The engine
  can then call various functions in the map to update it.  Capmap
  contains most of the game state.
"""

from node import Node

class Capmap(object):

    def __init__(self):
        self._nodes = []

    def getNodes(self):
        # make copy of nodes list
        nodes = [Node(n.getName(), n.getSize(), n.getX(),
                      n.getY(), n.getEdges()) for
                 n in self._nodes]
        return nodes
        
    def useDefaultMap(self):
        n1 = Node(0, 20, 100, 100, [1])
        n2 = Node(1, 20, 300, 300, [0])
        self._nodes.extend([n1, n2])
