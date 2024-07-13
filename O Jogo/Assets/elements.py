class Elementos:
    def __init__ (self):
        self._name = ""
        self._superior_a = ""
        self._inferior_a = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def superior_a(self):
        return self._superior_a

    @superior_a.setter
    def superior_a(self, superior_a):
        self._superior_a = superior_a

    @property
    def inferior_a(self):
        return self._inferior_a

    @inferior_a.setter
    def inferior_a(self, inferior_a):
        self._inferior_a = inferior_a