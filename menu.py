import pygame
import types
from display import *

COLOR_WHITE = (255, 255, 255)

MOUSE_LEFT = 1
MOUSE_RIGHT = 3


class DisplayObject:
    """
    Base class for display object
    """

    def __init__(self, rect):
        self.rect = rect
        self.surface = pygame.Surface((rect.width, rect.height))
        self.children = []

    def add_child(self, child):
        """
        Add DisplayObject as child of this one
        """
        self.children.append(child)

    def handle_event(self, event):
        """
        Event distribution handler
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self._on_click(event.pos, event.button)

    def _on_click(self, pos, button):
        """
        Handle click event. Returns True if handled and False if not
        This structure is meant to click on the shallowest child in
        the tree (the most elevated)
        """
        for child in self.children:
            if child.rect.collidepoint(pos) and child._on_click(pos, button):
                return True

        return self.on_click(pos, button)

    def on_click(self, pos, button):
        """
        Empty on click callback
        """
        return True

    def draw(self, screen):
        # Draw ourselves first (bottom)
        screen.blit(self.surface, (self.rect.x, self.rect.y))

        for child in self.children:
            child.draw(screen)


class Button(DisplayObject):

    def __init__(self, rect, caption):
        super().__init__(rect)

        draw_text(self.surface, caption)
        self.on_click = super().on_click

    def set_on_click(self, click_cb):
        self.on_click = click_cb


class Menu(DisplayObject):

    def __init__(self, gm):
        super().__init__(pygame.Rect(0, 0, gm.disp.get_width(), 30))

        def restart(pos, button):
            if button == MOUSE_LEFT:
                gm.disp.fill((0, 0, 0))
                gm.reset()
                self.draw(gm.disp)
                return True

            return False

        restart_caption = Caption('Restart', size=15, color=(255, 255, 255))
        restart_button = Button(pygame.Rect(gm.disp.get_width() - 100, 0, 100, 30), restart_caption)
        restart_button.set_on_click(restart)
        self.add_child(restart_button)



