import pygame
import time
from maze import Maze
from display import *


width = 5
length = 5
height = 3

pygame.init()
print('WASD for movement!')
print('Q: down, E: up!')
white = (255, 255, 255)
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((width*60, length*60))  # TODO: fix

pygame.display.set_caption('The Maze')

maze = Maze(width, length, height)

gameExit = False
mazeGenerated = False
clock = pygame.time.Clock()
moveKeys = {pygame.K_w: (0, -1, 0), pygame.K_s: (0, 1, 0),
            pygame.K_a: (-1, 0, 0), pygame.K_d: (1, 0, 0),
            pygame.K_q: (0, 0, -1), pygame.K_e: (0, 0, 1)}
layer = maze.get_player().z

while not gameExit:
    if not maze.generated:
        changed_cells = maze.generate()

        if changed_cells is not None:
            c1, c2 = changed_cells
            # only draws cells in current layer
            if c1.z == layer:
                draw_cell(gameDisplay, c1)
            if c2.z == layer:
                draw_cell(gameDisplay, c2)
        else:
            # end generation, show player
            draw_player(gameDisplay, maze.get_player())

        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.KEYDOWN:
            if event.key in moveKeys:
                # move player
                prev, curr = maze.player_move(*moveKeys[event.key])
                if prev.z != curr.z:
                    # change layers
                    # TODO: draw this the same way as maze generation?
                    draw_layer(gameDisplay, maze.get_layer(curr.z))
                else:
                    # update last cell
                    draw_cell(gameDisplay, prev)

                # update player and screen
                draw_player(gameDisplay, curr)
                pygame.display.update()

    clock.tick(60) # fps limit


pygame.quit()
quit()
