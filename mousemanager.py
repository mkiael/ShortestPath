class MouseManager(object):
    def __init__(self):
        self._left_button = False
        self._right_button = False
        self._callback_reg = dict()

    def register_callback(self, button_id, function):
        self._callback_reg[button_id] = function

    def on_mouse_button_down(self, button_id, pos):
        if button_id == 1:
            self._left_button = True
        elif button_id == 3:
            self._right_button = True

        if button_id in self._callback_reg:
            self._callback_reg[button_id](True, pos)

    def on_mouse_button_up(self, button_id, pos):
        if button_id == 1:
            self._left_button = False
        elif button_id == 3:
            self._right_button = False

        if button_id in self._callback_reg:
            self._callback_reg[button_id](False, pos)

    def is_left_button_pressed(self):
        return self._left_button

    def is_right_button_pressed(self):
        return self._right_button

