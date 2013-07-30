"""
Game body
"""

import pygame
from capmap import Capmap
from node import Node

def game():
    pygame.init()

    # display
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("game screen")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 0))

    # map initialization
    game_map = Capmap()
    game_map.default_map()

    # create node surfaces
    game_nodes = []
    for node in game_map.nodes:
        n = Game_Node(node)
        n.create_surface((139, 137, 137))
        game_nodes.append(n)
    num_nodes = len(game_nodes)

    # generate paths (between nodes)
    paths = create_paths(game_nodes)
    if paths == None:
        pygame.quit()
        # !!! print console message here
        raise SystemExit

    # game loop
    gameAlive = True
    clock = pygame.time.Clock()

    while gameAlive:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameAlive = False
                pygame.quit()
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
            pygame.draw.line(background, (0, 0, 0), path[0], path[1], 5)
            
        for node in game_nodes:
            screen.blit(node.surface, (node.x, node.y))
        
        pygame.display.flip()

def create_paths(nodes = None):
    if(nodes == None):
        return None
    
    paths = []

    for node in nodes:
        for edge in node.edges:
            path = ((node.x + node.size/2, node.y + node.size/2),
                    (nodes[edge].x + nodes[edge].size/2,
                         nodes[edge].y + nodes[edge].size/2))
            paths.append(path)

    return paths

class Game_Node(Node):

    def __init__(self, node = Node()):
        Node.__init__(self, node.name, node.size, node.x, node.y, node.edges)
        self.surface = None

    def create_surface(self, rgb = (0, 0, 0)):
        self.surface = pygame.Surface((self.size, self.size))
        self.surface = self.surface.convert()
        self.surface.fill(rgb)

if __name__ == '__main__':
    game()
                
