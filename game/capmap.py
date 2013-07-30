"""
  capmap.py
  The map class.  Capmap reads graph files (as yet unnamed), turns them
  into map objects and returns that to the game engine.  The engine
  can then call various functions in the map to update it.  Capmap
  contains most of the game state.
"""

from node import Node

class Capmap():

    def __init__(self):
        self.nodes = []
        
    def default_map(self):
        n1 = Node(0, 20, 100, 100, [1])
        n2 = Node(1, 20, 300, 300, [0])
        self.nodes.extend([n1, n2])
