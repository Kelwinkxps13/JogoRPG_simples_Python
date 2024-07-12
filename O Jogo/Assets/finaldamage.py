# multiplicadores de dano final
from random import randint

class Critico:

    def __init__(self, dano_final, taxa, dano):
        self.dano_final = dano_final
        self.taxa = taxa
        self.dano = dano

    def critical(self):
        crit = randint(1, 1000)
        if crit <= self.taxa*10:
            return True
        else:
            return False
    
    def dano_multiplicado(self):
        multiplicador_final = self.dano_final * self.dano / 100 # 10 * 120/100 = 10 * 1,2 = 12
        return self.dano_final + multiplicador_final