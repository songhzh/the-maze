import pygame
from maze import Maze
from cell import Cell
from display import draw_cell

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('The Maze')

maze = Maze(3, 3)

gameExit = False
while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)
    for i in range(10):
        for j in range(10):
            draw_cell(gameDisplay, Cell((i*20, j*20)))

    pygame.display.update()

pygame.quit()
quit()
