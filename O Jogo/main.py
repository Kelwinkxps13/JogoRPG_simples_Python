from Assets.personagem import *
from Instances.espadas import *
from Maps.mapa_teste import Mapa_teste
from Assets.level import Level
import os
import sys

def debug_and_die():
    print("isso é um debug")
    sys.exit()

os.system('cls')

player1 = Personagem()
player1.name = "Kelwin"
player1.arma = espada_de_madeira
level_player = Level()
level_player.atual_level = 7   ## mude aqui o level do player durante o teste
# level_player.atual_xp = 99999999999999991
player1.hp_atual = level_player.max_level[level_player.atual_level][2]
player1.hp_base = player1.hp_atual
player1.level = level_player

enemy1 = Personagem()
enemy1.name = "Leandro 1"
enemy1.arma = espada_de_madeira
level_enemy1 = Level()
level_enemy1.atual_level = 2
enemy1.hp_atual = level_enemy1.max_level[level_enemy1.atual_level][2]
enemy1.hp_base = enemy1.hp_atual
enemy1.level = level_enemy1

enemy2 = Personagem()
enemy2.name = "Leandro 2"
enemy2.arma = espada_de_madeira
level_enemy2 = Level()
level_enemy2.atual_level = 3
enemy2.hp_atual = level_enemy2.max_level[level_enemy2.atual_level][2]
enemy2.hp_base = enemy2.hp_atual
enemy2.level = level_enemy2

enemy3 = Personagem()
enemy3.name = "Leandro 3"
enemy3.arma = espada_de_madeira
level_enemy3 = Level()
level_enemy3.atual_level = 5
enemy3.hp_atual = level_enemy3.max_level[level_enemy3.atual_level][2]
enemy3.hp_base = enemy3.hp_atual
enemy3.level = level_enemy3

# tire o comentario dessa parte para testar a funcao de ganhar xp

# player1.ganhar_xp_while(100000000)



# tire o comentario dessa parte para testar a funcao de combate

# Combate.acao(player1, enemy1


t = Mapa_teste()
t.player = player1
t.array_enemies[0] = enemy1
t.array_enemies[1] = enemy2
t.array_enemies[2] = enemy3
t.mapa_aberto()
print('end')