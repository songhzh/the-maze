import pygame

CELL_SIZE = 30
WALL_SIZE = 2
PLAYER_SIZE = CELL_SIZE - WALL_SIZE
BACKGROUND_COLOR = (0, 0, 0)  # Black
WALL_COLOR = (255, 255, 255)  # White


vert_wall = pygame.Surface((WALL_SIZE, CELL_SIZE))
vert_wall.fill(WALL_COLOR)

hor_wall = pygame.Surface((CELL_SIZE, WALL_SIZE))
hor_wall.fill(WALL_COLOR)


def draw_cell(screen, cell):
    cell_surface = pygame.Surface((CELL_SIZE, CELL_SIZE))
    cell_surface.fill(BACKGROUND_COLOR)

    if cell.north is None:
        cell_surface.blit(hor_wall, (0, 0))
    if cell.south is None:
        cell_surface.blit(hor_wall, (0, PLAYER_SIZE))
    if cell.west is None:
        cell_surface.blit(vert_wall, (0, 0))
    if cell.east is None:
        cell_surface.blit(vert_wall, (PLAYER_SIZE, 0))

    pos = cell.x * CELL_SIZE, cell.y * CELL_SIZE
    screen.blit(cell_surface, pos)

def draw_player(screen, player):
    # player is a cell
    player_surface = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
    player_surface.fill((255, 0, 0))

    pos = player.x * CELL_SIZE, player.y * CELL_SIZE
    screen.blit(player_surface, pos)
