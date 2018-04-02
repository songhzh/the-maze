import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('The Maze')

gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)

    pygame.draw.rect(gameDisplay, black, [10, 10, 300, 300])

    pygame.display.update()

pygame.quit()
quit()
