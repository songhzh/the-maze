import pygame
import types
from display import *

'''
Constants
'''

COLOR_WHITE = (255, 255, 255)
COLOR_INACTIVE = COLOR_WHITE
COLOR_ACTIVE = (255, 255, 51)
FONT = pygame.font.get_default_font()

MOUSE_LEFT = 1
MOUSE_RIGHT = 3


class DisplayObject:
    """
    Base class for display object
    """

    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.surface = pygame.Surface((self.rect.width, self.rect.height))
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
        for child in self.children:
            child.handle_event(event)

    def draw(self, screen):
        # Draw ourselves first (bottom)
        screen.blit(self.surface, (self.rect.x, self.rect.y))

        for child in self.children:
            child.draw(screen)


class Label(DisplayObject):
    """
    Represents a text label
    """
    def __init__(self, x, y, w, h, text, size=15):
        self.caption = Caption(text, size, COLOR_WHITE)
        super().__init__(x, y, w, h)

        draw_text(self.surface, self.caption)

    def update_text(self, text):
        self.caption.text = text
        self.surface.fill(BACKGROUND_COLOR)
        draw_text(self.surface, self.caption)


class Button(DisplayObject):
    """
    Represents a clickable button, with text on top
    """
    def __init__(self, x, y, w, h, text, size=15):
        super().__init__(x, y, w, h)

        caption = Caption(text, size, COLOR_WHITE)
        draw_text(self.surface, caption)
        self.on_click = None

    def handle_event(self, event):
        super().handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(*event.pos) and self.on_click is not None:
                self.on_click(event.pos, event.button)

    def set_on_click(self, click_cb):
        """
        click_cb is of type function(pos, button)
        """
        self.on_click = click_cb


class InputBox(DisplayObject):
    # Adapted from code posted by user 'skrx' on stack overflow
    # Source: https://stackoverflow.com/questions/46390231/how-to-create-a-text-input-box-with-pygame
    def __init__(self, x, y, w, h, text='', max_length=2):
        super().__init__(x, y, w, h)
        self.caption = Caption(text, size=15, color=COLOR_INACTIVE)
        self.caption.y = 2
        self.text = text
        self.max_length = max_length
        
        draw_text(self.surface, self.caption)
        self.active = False

    def handle_event(self, event):
        """
        Focus / unfocus the input box on click and accepts key input
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(*event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.caption.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.unicode.isdigit():
                    if len(self.text) < self.max_length:
                        self.text += event.unicode
                    # Overwrite the string with the new character
                    else:
                        self.text = event.unicode

        # Re-render the text.
        self.caption.text = self.text
        self.surface.fill(BACKGROUND_COLOR)
        draw_text(self.surface, self.caption)

    def update(self, screen):
        """
        To properly react to user input, we have to redraw the
        input box at every cycle
        """
        self.draw(screen)
        pygame.draw.rect(screen, self.caption.color, self.rect, 2)

    def get_value(self):
        return self.text


class Menu(DisplayObject):
    """
    Represents the menu bar at the top of the screen
    """
    def __init__(self, gm):
        super().__init__(0, 0, gm.disp.get_width(), 30)

        # Layer label
        layer_text = 'Layer 1/{}'.format(gm.height)
        self.layer_label = Label(0, 0, 100, 30, layer_text)
        self.total_layers = gm.height
        self.add_child(self.layer_label)

        # Dimension input boxes
        self.width_label = Label(100, 0, 60, 30, 'Width: ')
        self.width_box = InputBox(160, 2, 40, 25, str(gm.width))
        self.length_label = Label(210, 0, 80, 30, 'Length: ')
        self.length_box = InputBox(290, 2, 40, 25, str(gm.length))
        self.height_label = Label(340, 0, 80, 30, 'Height: ')
        self.height_box = InputBox(420, 2, 40, 25, str(gm.height), max_length=1)

        self.input_boxes = [self.width_box, self.length_box, self.height_box]

        self.add_child(self.width_label)
        self.add_child(self.width_box)
        self.add_child(self.length_label)
        self.add_child(self.length_box)
        self.add_child(self.height_label)
        self.add_child(self.height_box)

        # The restart button
        def restart(pos, button):
            if button == MOUSE_LEFT:
                gm.disp.fill(BACKGROUND_COLOR)

                gm.width = self._check_dim(self.width_box.get_value(), 20, 60)
                gm.length = self._check_dim(self.length_box.get_value(), 10, 40)
                gm.height = self._check_dim(self.height_box.get_value(), 1, 10)

                gm.reset()

        restart_button = Button(gm.disp.get_width() - 100, 0, 100, 30, 'Restart')
        restart_button.set_on_click(restart)
        self.add_child(restart_button)

    def update(self, screen):
        """
        We need to check for updates to the input boxes at every cycle
        """
        for box in self.input_boxes:
            box.update(screen)

    def update_layer(self, screen, layer):
        self.layer_label.update_text('Layer: {}/{}'.format(layer + 1, self.total_layers))
        self.layer_label.draw(screen)

    def _check_dim(self, dim, minimum=10, maximum=40):
        """
        Returns a valid dimension
        """

        try:
            dim = int(dim)
        except ValueError:
            print('Invalid dimension \'{}\', defaulting to {}'.format(dim, minimum))
            dim = minimum

        # Clamp to range
        dim = max(minimum, dim)
        dim = min(maximum, dim)

        return dim
