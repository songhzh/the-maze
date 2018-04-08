import pygame
from maze import Maze
from display import *
from menu import DisplayObject, Button


# Move player in the 6 directions
MOVE_KEYS = {pygame.K_w: (0, -1, 0), pygame.K_s: (0, 1, 0),
             pygame.K_a: (-1, 0, 0), pygame.K_d: (1, 0, 0),
             pygame.K_q: (0, 0, -1), pygame.K_e: (0, 0, 1)}

# Peek through each layer without moving player
PEEK_KEYS = {pygame.K_UP: 1, pygame.K_DOWN: -1}

# Controls speed of maze generation
# Lower = Faster
GEN_CONST = 300


class GameManager:
    def __init__(self):
        self.width = 20
        self.length = 20
        self.height = 2

        self.disp = pygame.display.set_mode((self.width * CELL_SIZE,
                                             self.length * CELL_SIZE + 30))

        self.maze = None
        self.layer = None
        self.genLoops = 1
        self.generated = False

        self.reset()

    def reset(self):
        self.maze = Maze(self.width, self.length, self.height)

        self.layer = self.get_player().z  # currently-viewed layer

        # Scale maze generation speed linearly with volume
        self.genLoops = max(1, self.width * self.length * self.height // GEN_CONST)
        self.generated = False

    def generate_maze(self):
        """
        In each loop, generates a single cell of the maze
        - If the cell is on the currently-viewed layer, it will be drawn
        - If all cells have been generated, the player will be drawn

        Returns: If maze has been entirely generated
        """
        for i in range(self.genLoops):
            changed_cells = self.maze.generate()

            if changed_cells is not None:
                c1, c2 = changed_cells
                # only draw cells in current layer
                if c1.z == self.layer:
                    draw_cell(self.disp, c1)
                if c2.z == self.layer:
                    draw_cell(self.disp, c2)
            else:
                # end generation, draw player
                draw_player(self.disp, self.get_player())
                self.generated = True
                return

        return

    def get_input(self, eventKey):
        """
        Determines player input and redirects to appropriate function
        Also refreshes player render

        eventKey: pygame key code of pressed key
        """
        if eventKey in MOVE_KEYS:
            self.move_player(MOVE_KEYS[eventKey])
        elif eventKey in PEEK_KEYS:
            self.peek_layer(PEEK_KEYS[eventKey])
        else:
            return

        if self.layer == self.get_player().z:
            draw_player(self.disp, self.get_player())

    def move_player(self, delta):
        """
        Move player in 6 directions
        Overrides layer peeking; Will always jump back to player's level

        delta: tuple (dx, dy, dz); change +/- 1 in one direction
        """
        # c1, c2 are the previous and current cells that represent the player
        c1, c2 = self.maze.player_move(*delta)

        if self.layer != c2.z:
            # Change layers
            self.layer = c2.z
            draw_layer(self.disp, self.maze.get_layer(c2.z))
        else:
            # Update last cell
            # Less expensive
            draw_cell(self.disp, c1)

        draw_player(self.disp, self.get_player())

        if c2.get_pos() == self.maze.end_cell.get_pos():
            draw_win(self.disp)

    def peek_layer(self, delta):
        """
        Move currently-viewed layer up or down without moving the player

        delta: change +/- 1 for the layer
        """
        new_layer = self.layer + delta

        if self.layer != self.maze.check_layer(new_layer):
            # Not at bottom of top of layers
            self.layer = new_layer
            draw_layer(self.disp, self.maze.get_layer(new_layer))

    def get_player(self):
        return self.maze.get_player()
