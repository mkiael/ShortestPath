class KeyManager(object):
    def __init__(self):
        self._key_dict = dict()
        self._callback_reg = dict()

    def register_callback(self, key_id, function):
        self._callback_reg[key_id] = function

    def on_key_down(self, key_id):
        self._key_dict[key_id] = True
        if key_id in self._callback_reg:
            self._callback_reg[key_id](True)

    def on_key_up(self, key_id):
        self._key_dict[key_id] = False
        if key_id in self._callback_reg:
            self._callback_reg[key_id](False)

    def is_key_pressed(self, key_id):
        if key_id in self._key_dict:
            return self._key_dict[key_id]
        else:
            return False