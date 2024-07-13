# multiplicadores de dano final
from random import randint

class Critico:

    def __init__(self):
        self._dano_final = 0
        self._taxa = 0
        self._dano = 0

    @property
    def dano_final(self):
        return self._dano_final

    @dano_final.setter
    def dano_final(self, dano_final):
        self._dano_final = dano_final

    @property
    def taxa(self):
        return self._taxa

    @taxa.setter
    def taxa(self, taxa):
        self._taxa = taxa

    @property
    def dano(self):
        return self._dano

    @dano.setter
    def dano(self, dano):
        self._dano = dano

    def critical(self):
        crit = randint(1, 1000)
        if crit <= self._taxa*10:
            return True
        else:
            return False
    
    def dano_multiplicado(self):
        multiplicador_final = self._dano_final * self._dano / 100 # 10 * 120/100 = 10 * 1,2 = 12
        return self._dano_final + multiplicador_final