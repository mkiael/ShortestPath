from node import Node

class Graph(object):
    def __init__(self):
        self._node_list = []
        self._edge_list = []
        self._selected_node = None
        self._node_id_counter = -1

    def _create_node_id(self):
        self._node_id_counter += 1
        return self._node_id_counter


    def add_node(self, pos):
        self._node_list.append(Node(self._create_node_id(), pos))

    def select_node(self, pos):
        for node in self._node_list:
            if node.is_inside(pos):
                if self._selected_node != None:
                    self._selected_node.add_neighbour(node)
                    self._selected_node.deselect()
                    self._selected_node = None
                else:
                    node.select()
                    self._selected_node = node

    def render(self, display_surf):
        for node in self._node_list:
            node.render_edges(display_surf)

        for node in self._node_list:
            node.render_node(display_surf)
