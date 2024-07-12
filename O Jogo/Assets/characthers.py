from .finaldamage import Critico
from .characthrers_level import *

class Personagem:
    def __init__(self, name, hp_base, arma, level):
        self.name = name
        self.element = "fogo"
        self.hp_base = hp_base
        self.hp_atual = hp_base
        self.arma = arma

        self.level = level

    def fight(self, enemy):
        crit = Critico(self.arma.atk_base, self.arma.taxa, self.arma.dano)
        if crit.critical():
            enemy.hp_atual -= crit.dano_multiplicado()
            print(f'um critico!!! {self.name} ataca {enemy.name} e causa {crit.dano_multiplicado()} de dano!!')
        else:
            enemy.hp_atual -= self.arma.atk_base
            print(f'{self.name} ataca {enemy.name} e causa {self.arma.atk_base} de dano!!')

    def ganhar_xp(self, win): 

        #supunhetemos que estamamos no lv2 com 15/30
        # win = 20
        # teoricamente ele ficaria com 5/40 -- 35/30 se der errado

        x = 0
        x = self.level.atual_xp # xp atual = 15
        x += win # 15+20 = 35

        print(f'voce ganhou {win} de xp!')

        if(x >= self.level.xp_next_level): # x >= 30 -- 35 >= 30
            self.level.atual_xp = x - self.level.xp_next_level # 35 - 30 = 5
            self.level.xp_next_level = self.level.max_level[self.level.atual_level+1][1] # 40
            self.level.atual_level = self.level.max_level[self.level.atual_level+1][0] # lv3
            print(f'voce subiu para o nivel {self.level.atual_level}! continue assim!')