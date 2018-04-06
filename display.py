import pygame

CELL_SIZE = 30
WALL_SIZE = 2
PATH_SIZE = CELL_SIZE // 2
BACKGROUND_COLOR = (0, 0, 0)  # Black

WALL_COLOR = (255, 255, 255)  # White
UP_COLOUR = (0, 255, 0) # Green
DOWN_COLOUR = (255, 0, 0) # Red

vert_wall = pygame.Surface((WALL_SIZE, CELL_SIZE))
vert_wall.fill(WALL_COLOR)

hor_wall = pygame.Surface((CELL_SIZE, WALL_SIZE))
hor_wall.fill(WALL_COLOR)

up_path = pygame.Surface((PATH_SIZE, WALL_SIZE))
up_path.fill(UP_COLOUR)

down_path = pygame.Surface((PATH_SIZE, WALL_SIZE))
down_path.fill(DOWN_COLOUR)

def draw_cell(screen, cell):
    cell_surface = pygame.Surface((CELL_SIZE, CELL_SIZE))
    cell_surface.fill(BACKGROUND_COLOR)

    if cell.north is None:
        cell_surface.blit(hor_wall, (0, 0))
    if cell.south is None:
        cell_surface.blit(hor_wall, (0, CELL_SIZE - WALL_SIZE))
    if cell.west is None:
        cell_surface.blit(vert_wall, (0, 0))
    if cell.east is None:
        cell_surface.blit(vert_wall, (CELL_SIZE - WALL_SIZE, 0))
    if cell.above is not None:
        cell_surface.blit(up_path, ((CELL_SIZE - PATH_SIZE) // 2, \
        CELL_SIZE // 3))
    if cell.below is not None:
        cell_surface.blit(down_path, ((CELL_SIZE - PATH_SIZE) // 2, \
        CELL_SIZE * 2 // 3))

    pos = cell.x * CELL_SIZE, cell.y * CELL_SIZE
    screen.blit(cell_surface, pos)


def draw_player(screen, player):
    # player is a cell
    player_surface = pygame.Surface((CELL_SIZE - WALL_SIZE, CELL_SIZE - WALL_SIZE))
    player_surface.fill((255, 0, 0))

    pos = player.x * CELL_SIZE, player.y * CELL_SIZE
    screen.blit(player_surface, pos)


def draw_layer(screen, layer):
    # layer is a set of cells at a z-coord
    for cell in layer:
        draw_cell(screen, cell)
