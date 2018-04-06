import pygame
from game_manager import GameManager

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Man\'s Labyrinth')

gameExit = False
generated = False

gm = GameManager()

while not gameExit:
    if not generated:
        generated = gm.generate_maze()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        elif event.type == pygame.KEYDOWN and generated:
            gm.get_input(event.key) # player movement or layer peek

    pygame.display.update() # draw to screen
    clock.tick(60) # fps limit

pygame.quit()
quit()
