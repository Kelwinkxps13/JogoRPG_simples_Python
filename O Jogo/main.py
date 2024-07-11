from characthers import Player, Enemy
from espadas import *
from combate import Combate

player1 = Player("Kelwin", espada_de_madeira)
enemy1 = Enemy("Goblin", espada_de_madeira)

primeiro_combate = Combate(player1, enemy1)

primeiro_combate.acao()

print("fim do combate")