import pygame
import time
from maze import Maze
from cell import Cell
from display import draw_cell

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('The Maze')

maze = Maze(10, 10)

gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)

    for cell in maze:
        draw_cell(gameDisplay, cell)

    pygame.display.update()
    maze.random_merge()
    time.sleep(0.05)

pygame.quit()
quit()
