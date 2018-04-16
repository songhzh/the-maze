import pygame
from game_manager import GameManager

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Man\'s Labyrinth')

gameExit = False
generated = False

# Initialize the game manager
gm = GameManager()

while not gameExit:
    # Keep generating the maze if not done generating
    if not gm.maze.generated:
        gm.generate_maze()

    # Handle user events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        gm.handle_event(event)

    gm.menu.update(gm.disp)
    pygame.display.update() # draw to screen
    clock.tick(60) # fps limit

pygame.quit()
quit()
