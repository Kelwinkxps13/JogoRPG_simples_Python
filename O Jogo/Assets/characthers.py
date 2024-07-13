from .finaldamage import Critico
from .characthrers_level import *

class Personagem:
    def __init__(self):
        self._name = ""
        self._element = ""
        self._hp_base = 0
        self._hp_atual = 0
        self._arma = []
        self._level = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def element(self):
        return self._element

    @element.setter
    def element(self, element):
        self._element = element

    @property
    def hp_base(self):
        return self._hp_base

    @hp_base.setter
    def hp_base(self, hp_base):
        self._hp_base = hp_base

    @property
    def hp_atual(self):
        return self._hp_atual

    @hp_atual.setter
    def hp_atual(self, hp_atual):
        self._hp_atual = hp_atual

    @property
    def arma(self):
        return self._arma

    @arma.setter
    def arma(self, arma):
        self._arma = arma

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        self._level = level

    def fight(self, enemy):
        crit = Critico()
        crit.dano_final = self._arma.atk_base
        crit.taxa = self._arma.taxa
        crit.dano = self._arma.dano
        if crit.critical():
            enemy.hp_atual -= crit.dano_multiplicado()
            print(f'um critico!!! {self._name} ataca {enemy.name} e causa {crit.dano_multiplicado()} de dano!!')
        else:
            enemy.hp_atual -= self._arma.atk_base
            print(f'{self._name} ataca {enemy.name} e causa {self._arma.atk_base} de dano!!')

    def ganhar_xp(self, win): 

        #supunhetemos que estamamos no lv2 com 15/30
        # win = 20
        # teoricamente ele ficaria com 5/40 -- 35/30 se der errado

        x = 0
        x = self._level.atual_xp # xp atual = 15
        x += win # 15+20 = 35

        print(f'voce ganhou {win} de xp!')

        if(x >= self._level.xp_next_level): # x >= 30 -- 35 >= 30
            self._level.atual_xp = x - self._level.xp_next_level # 35 - 30 = 5
            self._level.xp_next_level = self._level.max_level[self._level.atual_level+1][1] # 40
            self._level.atual_level = self._level.max_level[self._level.atual_level+1][0] # lv3
            print(f'voce subiu para o nivel {self._level.atual_level}! continue assim!')