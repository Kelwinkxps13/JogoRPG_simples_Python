from finaldamage import Critico

class Player:
    def __init__(self, name, arma):
        self.name = name
        self.element = "fogo"
        self.hp_base = 100
        self.hp_atual = 100

        self.arma = arma

    def fight(self, enemy):
        crit = Critico(self.arma.atk_base, self.arma.taxa, self.arma.dano)
        if crit.critical():
            enemy.hp_atual -= crit.dano_multiplicado()
            print(f'um critico!!! {self.name} ataca {enemy.name} e causa {crit.dano_multiplicado()} de dano!!')
        else:
            enemy.hp_atual -= self.arma.atk_base
            print(f'{self.name} ataca {enemy.name} e causa {self.arma.atk_base} de dano!!')
            

class Enemy:
    def __init__(self, name, arma):
        self.name = name
        self.element = "agua"
        self.hp_base = 100
        self.hp_atual = 100

        self.arma = arma

    def fight(self, player):
        crit = Critico(self.arma.atk_base, self.arma.taxa, self.arma.dano)
        if crit.critical():
            player.hp_atual -= crit.dano_multiplicado()
            print(f'um critico!!! {self.name} ataca {player.name} e causa {crit.dano_multiplicado()} de dano!!')
        else:
            player.hp_atual -= self.arma.atk_base
            print(f'{self.name} ataca {player.name} e causa {self.arma.atk_base} de dano!!')
    