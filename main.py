import pygame
from maze import Maze
from cell import Cell
from display import draw_cell

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('The Maze')

maze = Maze(20, 20)

gameExit = False
mazeGenerated = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)

    for cell in maze:
        draw_cell(gameDisplay, cell)

    if not mazeGenerated:
        mazeGenerated = maze.generate(0.01)

    pygame.display.update()

pygame.quit()
quit()
