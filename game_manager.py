import pygame
from maze import Maze
from display import *
from components import Menu
from solver import Solver

# Move player in the 6 directions
MOVE_KEYS = {pygame.K_w: (0, -1, 0), pygame.K_s: (0, 1, 0),
             pygame.K_a: (-1, 0, 0), pygame.K_d: (1, 0, 0),
             pygame.K_q: (0, 0, -1), pygame.K_e: (0, 0, 1)}

# Peek through each layer without moving player
PEEK_KEYS = {pygame.K_UP: 1, pygame.K_DOWN: -1}

# Show hint
HINT_KEY = pygame.K_p

# Controls speed of maze generation
# Lower = Faster
GEN_CONST = 300


class GameManager:
    def __init__(self):
        self.width = 20
        self.length = 20
        self.height = 3

        self.disp = None
        self.menu = None

        self.maze = None
        self.layer = None
        self.genLoops = 1
        self.generated = False
        self.wonGame = False
        self.solver = None
        self.timer = pygame.time.Clock()
        self.reset()

        print('Controls: WASD/QE to move. Up/Dn to peek. P for solution.')

    def reset(self):
        self.disp = pygame.display.set_mode((max(self.width * CELL_SIZE, 560),
                                             self.length * CELL_SIZE + 30))
        self.menu = Menu(self)
        self.menu.draw(self.disp)

        self.maze = Maze(self.width, self.length, self.height)

        self.layer = self.get_player().z  # currently-viewed layer
        self.menu.update_layer(self.disp, self.layer)

        # Scale maze generation speed linearly with volume
        self.genLoops = max(1, self.width * self.length * self.height // GEN_CONST)
        self.generated = False
        self.wonGame = False

        self.timer.tick()


    def generate_maze(self):
        """
        In each loop, generates a single cell of the maze
        - If the cell is on the currently-viewed layer, it will be drawn
        - If all cells have been generated, the player will be drawn
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

                # Solve maze
                self.solver = Solver(self.maze)
                return

        return

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN \
           and self.maze.generated and not self.wonGame:
            self.get_input(event.key) # player movement or layer peek or hint

        self.menu.handle_event(event)

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
        elif eventKey == HINT_KEY:
            self.show_hint()
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
            self.menu.update_layer(self.disp, self.layer)
        else:
            # Update last cell
            # Less expensive
            draw_cell(self.disp, c1)

        draw_player(self.disp, self.get_player())

        if c2.get_pos() == self.maze.end_cell.get_pos():
            draw_win(self.disp, self.timer.tick() // 1000)
            self.wonGame = True

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
            self.menu.update_layer(self.disp, self.layer)

    def show_hint(self):
        """
        Lights up the solution. Cheater.
        """
        self.solver.show_hint()

        for cell in self.solver.path:
            if self.layer == cell.z:
                # only draw cells at currently-viewed layer
                draw_cell(self.disp, cell)

    def get_player(self):
        return self.maze.get_player()
