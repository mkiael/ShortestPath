import pygame

class Node(object):
    def __init__(self, node_id, pos):
        self._node_id = node_id
        self._pos = pos
        self._radius = 10
        self._node_color = (255, 0, 0)
        self._edge_color = (0, 0, 0)
        self._rect = None
        self._is_selected = False
        self._neighbours = []

    def get_pos(self):
        return self._pos

    def add_neighbour(self, node):
        self._neighbours.append(node)

    def render_edges(self, display_surf):
        for node in self._neighbours:
            pygame.draw.line(display_surf, self._edge_color, self._pos, node.get_pos())

    def render_node(self, display_surf):
        self._rect = pygame.draw.circle(display_surf, self._node_color, self._pos, self._radius)

    def is_inside(self, pos):
        return self._rect.collidepoint(pos)

    def select(self):
        if not self._is_selected:
            self._node_color = (255, 255, 0)
            self._is_selected = True;

    def deselect(self):
        if self._is_selected:
            self._node_color = (255, 0, 0)
            self._is_selected = False;
