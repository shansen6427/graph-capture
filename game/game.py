
"""
Game body
"""

import pygame
from capmap import Capmap
from node import Node

class GraphCapture():
    def __init__(self, pygameModule):
        self._game_map = None
        self._game_nodes = []
        self._num_nodes = 0
        self._pygame = pygameModule
        
    def game(self):
        self._pygame.init()

        # display
        screen = self._pygame.display.set_mode((640,480))
        self._pygame.display.set_caption("game screen")

        background = self._pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((255, 255, 0))

        # map initialization
        self._game_map = Capmap()
        self._game_map.useDefaultMap()

        # create node surfaces
        for node in self._game_map.getNodes():
            n = GameNode(node)
            n.createSurface((139, 137, 137))
            self._game_nodes.append(n)
        num_nodes = len(self._game_nodes)

        # generate paths (between nodes)
        paths = createPaths(self._game_nodes)
       
        # game loop
        game_alive = True
        clock = self._pygame.time.Clock()

        while game_alive:
            clock.tick(30)

            for event in self._pygame.event.get():
                # exit game triggered (exits game)
                if event.type == self._pygame.QUIT:
                    game_alive = False
                    self._pygame.quit()
                    raise SystemExit

            """
            draw all objects in following order:
            - background
            - draw paths directly onto background
            - nodes
            - active troops
            """
            screen.blit(background, (0, 0))

            for path in paths:
                self._pygame.draw.line(background, (0, 0, 0), path[0], path[1], 5)
            
            for node in self._game_nodes:
                screen.blit(node.surface, (node.x, node.y))
        
            self._pygame.display.flip()
            # end game loop
            

    def createPaths(self, nodes = None):
        if(nodes == None or len(nodes) == 0):
            # !!! print console error message
            self._pygame.quit()
            raise SystemExit
    
        paths = []

        for node in nodes:
            for edge in node.getEdges():
                # place path endpoints in middle of each node surface
                # (nodes x and y are located at the top-left corner of
                #   their surface)
                path = ((node.getX() + node.getSize()/2,
                         node.getY() + node.getSize()/2),
                        (nodes[edge].getX() + nodes[edge].getSize()/2,
                             nodes[edge].getY() + nodes[edge].getSize()/2))
                paths.append(path)

        return paths

class GameNode(Node):

    def __init__(self, node):
        Node.__init__(self, node.getName(), node.getSize(),
                      node.getX(), node.getY(), node.getEdges())
        self._surface = None

    def createSurface(self, rgb = (0, 0, 0)):
        self._surface = pygame.Surface((self.size, self.size))
        self._surface = self._surface.convert()
        self._surface.fill(rgb)

    def getSurface(self):
        return self._surface

if __name__ == '__main__':
    game = GraphCapture(pygame)
    GraphCapture.game()
                
