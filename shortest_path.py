import pygame
import keymanager
import mousemanager
from graph import Graph
from pygame.locals import *

# States
DRAW_NODES = 0
DRAW_EDGES = 1

class App(object):
    def __init__(self):
        self._key_manager = keymanager.KeyManager()
        self._mouse_manager = mousemanager.MouseManager()
        self._graph = Graph()
        self._running = True
        self._display_surf = None
        self._width, self._height = 800, 600
        self._size = (self._width, self._height)
        self._bg_color = (255, 255, 255)
        self._state = DRAW_NODES

        self._key_manager.register_callback(pygame.K_e, self._on_key_e_cb)
        self._key_manager.register_callback(pygame.K_n, self._on_key_n_cb)

        # Register mouse callbacks
        self._mouse_manager.register_callback(1, self._on_left_button_cb)

    def _on_left_button_cb(self, is_pressed, pos):

        # No action on key up yet
        if not is_pressed: return

        if self._state == DRAW_NODES:
            self._graph.add_node(pos)
        elif self._state == DRAW_EDGES:
            self._graph.select_node(pos)

    def _on_key_e_cb(self, is_pressed):
        self._state = DRAW_EDGES

    def _on_key_n_cb(self, is_pressed):
        self._state = DRAW_NODES

    def _on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self._size)
        pygame.display.set_caption('Shortest path')
        self._running = True

    def _on_event(self, event):
        if event.type == pygame.KEYDOWN:
            self._key_manager.on_key_down(event.key)
        elif event.type == pygame.KEYUP:
            self._key_manager.on_key_up(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self._mouse_manager.on_mouse_button_down(event.button, event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            self._mouse_manager.on_mouse_button_up(event.button, event.pos)
        elif event.type == pygame.QUIT:
            self._running = False

    def _on_update(self):
        pass

    def _on_render(self):
        self._display_surf.fill(self._bg_color)
        self._graph.render(self._display_surf)
        pygame.display.update()

    def _on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self._on_init() == False:
            self._running = False

        while( self._running ):

            # Process all events
            for event in pygame.event.get():
                self._on_event(event)

            # Update state
            self._on_update()

            # Draw everything
            self._on_render()

        # Clean up
        self._on_cleanup()

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()