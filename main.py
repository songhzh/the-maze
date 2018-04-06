import pygame
import time
from maze import Maze
from display import *


width = 20
length = 20
height = 1

pygame.init()
print('WASD for movement!')
white = (255, 255, 255)
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((width*30, length*30))  # TODO: fix

pygame.display.set_caption('The Maze')

maze = Maze(width, length, height)

gameExit = False
mazeGenerated = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                maze.player_move(0, -1, 0)
            elif event.key == pygame.K_a:
                maze.player_move(-1, 0, 0)
            elif event.key == pygame.K_s:
                maze.player_move(0, 1, 0)
            elif event.key == pygame.K_d:
                maze.player_move(1, 0, 0)

    if not maze.generated:
        changed_cells = maze.generate()
        draw_layer(gameDisplay, maze.get_layer())

    draw_player(gameDisplay, maze.get_player())

    pygame.display.update()


pygame.quit()
quit()
