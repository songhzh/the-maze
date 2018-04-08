import pygame
import time
from maze import Maze
from display import *


width = 10
length = 10
height = 1

pygame.init()
print('WASD for movement!')
print('Q: down, E: up!')
print('up / down to peek at layers!')
white = (255, 255, 255)
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((width*30, length*30))  # TODO: fix
pygame.display.set_caption('The Maze')

maze = Maze(width, length, height)

gameExit = False
mazeGenerated = False
clock = pygame.time.Clock()

moveKeys = {pygame.K_w: (0, -1, 0), pygame.K_s: (0, 1, 0),
            pygame.K_a: (-1, 0, 0), pygame.K_d: (1, 0, 0),
            pygame.K_q: (0, 0, -1), pygame.K_e: (0, 0, 1)}
scrollKeys = {pygame.K_UP: 1, pygame.K_DOWN: -1}

prev, curr = maze.get_player(), maze.get_player()
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
        elif event.type == pygame.KEYDOWN and maze.generated:
            if event.key in moveKeys:
                # move player
                prev, curr = maze.player_move(*moveKeys[event.key])
                if layer != curr.z:
                    # change layers
                    layer = curr.z
                    print('Moving to layer', layer + 1)
                    draw_layer(gameDisplay, maze.get_layer(curr.z))
                else:
                    # update last cell
                    draw_cell(gameDisplay, prev)

                if curr.get_pos() == maze.end_cell.get_pos():
                    draw_win(gameDisplay, width, length)

            elif event.key in scrollKeys:
                new_layer = layer + scrollKeys[event.key]

                if layer !=  maze.check_layer(new_layer):
                    layer = new_layer
                    print('Peeking at layer', layer + 1)
                    draw_layer(gameDisplay, maze.get_layer(layer))

            if event.key in moveKeys or event.key in scrollKeys:
                # update player and screen
                if layer == maze.get_player().z:
                    draw_player(gameDisplay, maze.get_player())

                pygame.display.update()

    clock.tick(60) # fps limit


pygame.quit()
quit()
