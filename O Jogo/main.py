from characthers import Player, Enemy
from espadas import *

player1 = Player("Kelwin", espada_de_madeira)
enemy1 = Enemy("Goblin", espada_de_madeira)

while player1.hp_atual > 0 and enemy1.hp_atual > 0:
    print("Menu combate")
    print(f'arma atual: {player1.arma.name}')
    print(f'hp {player1.name}: {player1.hp_atual}/{player1.hp_base}')
    print(f'hp {enemy1.name}: {enemy1.hp_atual}/{player1.hp_base}')
    print("[1] atacar")
    choice = (input("> "))

    if choice == "1":
        player1.fight(enemy1)
        if enemy1.hp_atual <=0:
            print("voce ganhou!")
        else:
            enemy1.fight(player1)
            if player1.hp_atual <=0:
                print("voce perdeu!")
        
print("fim do combate")