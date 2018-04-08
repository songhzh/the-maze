import pygame
from game_manager import GameManager
from menu import Menu


pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Man\'s Labyrinth')

gameExit = False
generated = False

gm = GameManager()

while not gameExit:
    if not gm.maze.generated:
        gm.generate_maze()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        gm.handle_event(event)

    pygame.display.update() # draw to screen
    clock.tick(60) # fps limit

pygame.quit()
quit()
