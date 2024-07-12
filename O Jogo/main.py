from Assets.characthers import *
from Instances.espadas import *
from Assets.combate import Combate
import os

os.system('cls')

player1 = Personagem("Kelwin", 100, espada_de_madeira, Level(1, 0, "humano"))
enemy1 = Personagem("Goblin", 100, espada_de_madeira, Level(1, 0, "humano"))

primeiro_combate = Combate(player1, enemy1)

primeiro_combate.acao()

print("fim do combate")