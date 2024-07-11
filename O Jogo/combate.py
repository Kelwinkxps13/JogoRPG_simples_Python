class Combate:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def acao(self):
        while self.player.hp_atual > 0 and self.enemy.hp_atual > 0:
            print("Menu combate")
            print(f'arma atual: {self.player.arma.name}')
            print(f'hp {self.player.name}: {self.player.hp_atual}/{self.player.hp_base}')
            print(f'hp {self.enemy.name}: {self.enemy.hp_atual}/{self.player.hp_base}')
            print("[1] atacar")
            choice = (input("> "))

            if choice == "1":
                self.player.fight(self.enemy)
                if self.enemy.hp_atual <=0:
                    print("voce ganhou!")
                else:
                    self.enemy.fight(self.player)
                    if self.player.hp_atual <=0:
                        print("voce perdeu!")