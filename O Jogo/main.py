from Assets.personagem import *
from Instances.espadas import *
from Assets.combate import Combate
import os

os.system('cls')

player1 = Personagem()
player1.name = "Kelwin"
player1.hp_atual = 150
player1.hp_base = 150
player1.arma = espada_de_madeira
level_player = Level()
level_player.atual_level = 1
player1.level = level_player

enemy1 = Personagem()
enemy1.name = "Leandro"
enemy1.hp_atual = 150
enemy1.hp_base = 150
enemy1.arma = espada_de_madeira
level_enemy = Level()
level_enemy.atual_level = 3
enemy1.level = level_enemy

# player1.ganhar_xp(100)
primeiro_combate = Combate()
primeiro_combate.player = player1
primeiro_combate.enemy = enemy1

primeiro_combate.acao()

print("fim do combate")