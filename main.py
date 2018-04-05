import pygame
from maze import Maze
from cell import Cell
from display import draw_cell, draw_player


width = 20
length = 20
height = 20

pygame.init()
print('WASD for movement!')
white = (255, 255, 255)
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((width*30, length*30))  # TODO: fix

pygame.display.set_caption('The Maze')

maze = Maze(width, length, height, gameDisplay)
delay = 1/(width * height * 1000)
if delay < 0.01:
    delay = 0

gameExit = False
mazeGenerated = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                maze.player_move(0, -1)
            elif event.key == pygame.K_a:
                maze.player_move(-1, 0)
            elif event.key == pygame.K_s:
                maze.player_move(0, 1)
            elif event.key == pygame.K_d:
                maze.player_move(1, 0)

    if not mazeGenerated:
        mazeGenerated = maze.generate(delay)

    draw_player(gameDisplay, maze.get_player())

    pygame.display.update()

pygame.quit()
quit()
