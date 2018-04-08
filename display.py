import pygame
import os

pygame.font.init()

CELL_SIZE = 30
MENU_SIZE = CELL_SIZE
WALL_SIZE = 2
PATH_SIZE = CELL_SIZE // 4
PLAYER_SIZE = CELL_SIZE * 2 // 3
BACKGROUND_COLOR = (0, 0, 0)  # Black

WALL_COLOR = (255, 255, 255)  # White
UP_COLOUR = (0, 255, 0) # Green
DOWN_COLOUR = (255, 0, 0) # Red
VISIT_COLOUR = (0, 255, 255) # Cyan
PLAYER_COLOUR = (0, 0, 255) # Blue
vert_wall = pygame.Surface((WALL_SIZE, CELL_SIZE))
vert_wall.fill(WALL_COLOR)

hor_wall = pygame.Surface((CELL_SIZE, WALL_SIZE))
hor_wall.fill(WALL_COLOR)

up_path = pygame.Surface((PATH_SIZE, WALL_SIZE))
up_path.fill(UP_COLOUR)

down_path = pygame.Surface((PATH_SIZE, WALL_SIZE))
down_path.fill(DOWN_COLOUR)

visit_icon = pygame.Surface((WALL_SIZE, WALL_SIZE))
visit_icon.fill(VISIT_COLOUR)

door_icon = pygame.image.load(os.path.join('assets', 'door.jpg'))
door_rect = door_icon.get_rect()
door_offset = (CELL_SIZE - door_rect.width) // 2, (CELL_SIZE - door_rect.height) // 2

player_icon = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
player_icon.fill(PLAYER_COLOUR)


def draw_walls(screen, cell, surface):
    if cell.north is None:
        surface.blit(hor_wall, (0, 0))
    if cell.south is None:
        surface.blit(hor_wall, (0, CELL_SIZE - WALL_SIZE))
    if cell.west is None:
        surface.blit(vert_wall, (0, 0))
    if cell.east is None:
        surface.blit(vert_wall, (CELL_SIZE - WALL_SIZE, 0))
    if cell.above is not None:
        surface.blit(up_path, ((CELL_SIZE - PATH_SIZE) // 2,
                               CELL_SIZE // 3))
    if cell.below is not None:
        surface.blit(down_path, ((CELL_SIZE - PATH_SIZE) // 2,
                                 CELL_SIZE * 2 // 3))


def draw_cell(screen, cell):
    cell_surface = pygame.Surface((CELL_SIZE, CELL_SIZE))

    if cell.visited:
        cell_surface.blit(visit_icon, ((CELL_SIZE - WALL_SIZE) // 2,
                                       (CELL_SIZE - WALL_SIZE) // 2))

    draw_walls(screen, cell, cell_surface)
    if cell.is_end:
        cell_surface.blit(door_icon, door_offset)

    pos = cell.x * CELL_SIZE, cell.y * CELL_SIZE + MENU_SIZE

    screen.blit(cell_surface, pos)


def draw_player(screen, player):
    # player is a cell
    cell_surface = pygame.Surface((CELL_SIZE, CELL_SIZE))

    cell_surface.blit(player_icon, ((CELL_SIZE - PLAYER_SIZE) // 2,
                                    (CELL_SIZE - PLAYER_SIZE) // 2))

    draw_walls(screen, player, cell_surface)

    pos = player.x * CELL_SIZE, player.y * CELL_SIZE + MENU_SIZE

    screen.blit(cell_surface, pos)


def draw_layer(screen, layer):
    # layer is a set of cells at a z-coord
    for cell in layer:
        draw_cell(screen, cell)


class Caption:
    def __init__(self, text, size=50, color=(200, 000, 000)):
        self.text = str(text)
        self.x = 0
        self.y = 0
        self.centered = True
        self.color = color
        self.size = size
        self.font_type = pygame.font.get_default_font()


def draw_text(screen, caption):
    try:
        font = pygame.font.Font(caption.font_type, caption.size)
        text = font.render(caption.text, True, caption.color)
        text_width, text_height = text.get_size()

        if caption.centered:
            x = caption.x + (screen.get_width() - text_width) // 2
            y = caption.y + (screen.get_height() - text_height) // 2
        else:
            x = caption.x
            y = caption.y

        screen.blit(text, (x, y))

    except Exception as e:
        print('Font error')
        raise e


def draw_win(screen):
    win_caption = Caption('YOU WIN!!!', color=(255, 255, 51))
    draw_text(screen, win_caption)
