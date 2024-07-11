from characthers import Player, Enemy
from espadas import *
from combate import Combate
import os

os.system('cls')

player1 = Player("Kelwin", 100, espada_de_madeira)
enemy1 = Enemy("Goblin", 100, espada_de_madeira)

primeiro_combate = Combate(player1, enemy1)

primeiro_combate.acao()

print("fim do combate")