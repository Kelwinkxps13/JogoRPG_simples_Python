from .critico import Critico
from .level import *
from Instances.espadas import *
import sys

class Personagem:
    def __init__(self):
        self._name = ""
        self._element = ""
        self._hp_base = 0
        self._hp_atual = 0
        self._arma = None
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
        x = Espada()
        x.name = arma.name
        x.atk_base = arma.atk_base
        x.taxa = arma.taxa
        x.dano = arma.dano
        x.afetado = arma.afetado
        x.quantidade = arma.quantidade
        x.tempo = arma.tempo
        x.quantidade_de_vezes_que_pode_usar = arma.quantidade_de_vezes_que_pode_usar
        x.descricao_efeito = arma.descricao_efeito
        self._arma = x

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


    def ganhar_xp_while(self, win):

        x = self._level.atual_xp
        w = x + win
        print(f'voce ganhou {win} de xp!')

        if (self._level.atual_level >= 100):
            self._level.atual_xp += win
        else:
            z = 0
            k = int(self._level.xp_next_level)
            z = k - self._level.atual_xp
            if (self._level.atual_level < 100 and win < z):
                self._level.atual_xp += win
                restam = k - self._level.atual_xp
                print(f'faltam {restam} de xp para o proximo level!')
            else:
                # print(self._level.xp_next_level)
                # sys.exit()
                while (w >= k):

                    self._level.atual_xp = w - (int(self._level.xp_next_level))
                    w = self._level.atual_xp
                    y = 0
                    y = self._level.atual_xp
                    new_level = 0
                    new_level = self._level.max_level[self._level.atual_level+1][0]
                    self._level.atual_level = new_level #lv3
                    if (self._level.atual_level == 100):
                        self._level.xp_next_level = str("--")
                    else:
                        self._level.xp_next_level = str(self._level.max_level[self._level.atual_level+1][1])
                        x = y

                print(f'voce subiu para o nivel {self._level.atual_level}! continue assim!')
                if (self._level.atual_level < 100):
                    restam1 = int(self._level.xp_next_level) - self._level.atual_xp
                    print(f'faltam {restam1} de xp para o proximo level!')


    def ativar_efeito_arma(self):
        if(self._arma.afetado == "taxa critica"):
            self._arma.taxa += self._arma.quantidade
        elif(self._arma.afetado == "dano critico"):
            self._arma.dano += self._arma.quantidade
        elif(self._arma.afetado == "ataque base"):
            self._arma.atk_base += self._arma.quantidade

    def desativar_efeito_arma(self):
        if(self._arma.afetado == "taxa critica"):
            self._arma.taxa -= self._arma.quantidade
        elif(self._arma.afetado == "dano critico"):
            self._arma.dano -= self._arma.quantidade
        elif(self._arma.afetado == "ataque base"):
            self._arma.atk_base -= self._arma.quantidade
    # def ganhar_xp(self, win): 

    #     #supunhetemos que estamamos no lv2 com 15/30
    #     #win = 100
    #     #teoricamente ele ficaria com 5/40 -- 75/30 se der errado

    #     x = 0
    #     x = self._level.atual_xp #xp atual = 15
    #     x += win #15 + 100 = 115

    #     result = False
    #     if (self._level.atual_level == 100):
    #         result = False
    #     elif (x >= int(self._level.xp_next_level) and self._level.atual_level < 100): #115 >= 30
    #         result = True


    #     if(result): #x >= 30 -- 115 >= 30
    #         self._level.atual_xp = x - (int(self._level.xp_next_level)) #115 - 30 = 75

    #         new_level = 0
    #         new_level = self._level.max_level[self._level.atual_level+1][0]
    #         self._level.atual_level = new_level #lv3
    #         print(f'voce subiu para o nivel {self._level.atual_level}! continue assim!')

    #         if (self._level.atual_level == 100):
    #             self._level.xp_next_level = "--"
    #         elif (self._level.atual_level < 100):
    #             self._level.xp_next_level = self._level.max_level[self._level.atual_level+1][1] #40
    #             if (self._level.atual_xp >= int(self._level.xp_next_level)): #75 >= 40
    #                 self.ganhar_xp(self._level.atual_xp)

    #     elif (result == False):
    #         self._level.atual_xp += win

    #     print(f'voce ganhou {win} de xp!')
