import os 

class Combate:
    def __init__(self):
        self._player = []
        self._enemy = []

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        self._player = player

    @property
    def enemy(self):
        return self._enemy

    @enemy.setter
    def enemy(self, enemy):
        self._enemy = enemy


    def acao(self):
        
        
        rodadas_efeito_arma = 0
        count_rodadas = 1
        efeito_arma = False
        quantidade_de_vezes_que_pode_usar_o_efeito = self._player.arma.quantidade_de_vezes_que_pode_usar

        while self._player.hp_atual > 0 and self._enemy.hp_atual > 0:

            if rodadas_efeito_arma == 0 and efeito_arma == True:
                print(f'o efeito da arma {self._player.arma.name} acabou!')
                self._player.arma.desativar_efeito()
                efeito_arma = False

            print("")
            print("#########################################################")
            print("")

            if efeito_arma:
                print(f'rodadas restantes do efeito da arma: {rodadas_efeito_arma}')

            print(f'rodada: {count_rodadas}')
            print("")
            print(f'nv{self._player.level.atual_level}')
            print(f'xp: {self._player.level.atual_xp}/{self._player.level.xp_next_level}')
            print("")
            print(f'arma atual: {self._player.arma.name}')
            print(f'taxa critica: {self._player.arma.taxa}%')
            print(f'dano critico: {self._player.arma.dano}%')
            print(f'ataque base: {self._player.arma.atk_base}')
            print("")
            print(f'hp {self._player.name}: {self._player.hp_atual}/{self._player.hp_base}')
            print(f'hp {self._enemy.name}: {self._enemy.hp_atual}/{self._player.hp_base}')

            print("")
            print("#########################################################")
            print("")
            
            print("[1] atacar")
            print("[2] efeito de arma")
            choice = (input("> "))

            


            if choice == "1":
                os.system('cls')

                print("")
                print("#########################################################")
                print("")

                self._player.fight(self._enemy)

                if rodadas_efeito_arma >0 and efeito_arma:
                    rodadas_efeito_arma -=1

                count_rodadas += 1

                if self._enemy.hp_atual <=0:
                    print("voce ganhou!")
                    print(f'total de rodadas:{count_rodadas}')

                else:
                    self._enemy.fight(self._player)
                    if self._player.hp_atual <=0:
                        print("voce perdeu!")
                        print(f'total de rodadas:{count_rodadas}')

            elif choice == "2":

                os.system('cls')

                while True:
                    

                    print("")
                    print("#########################################################")
                    print("")

                    print(f'descrição: {self._player.arma.descricao_efeito}')
                    print(f'pode usar esse efeito {quantidade_de_vezes_que_pode_usar_o_efeito} vezes')
                    print("[1] ativar")
                    print("[2] voltar")
                    choice = (input("> "))

                    if choice == "1" and quantidade_de_vezes_que_pode_usar_o_efeito > 0:

                        if rodadas_efeito_arma > 0:
                            os.system('cls')
                            print("o efeito já está ativo!")
                        else:    
                            os.system('cls')
                            rodadas_efeito_arma = self._player.arma.tempo
                            efeito_arma = True
                            quantidade_de_vezes_que_pode_usar_o_efeito -= 1
                            self._player.arma.ativar_efeito()
                            print("efeito foi ativado!!")
                            break
                        # efeito de arma estara ativado
                        
                    elif choice == "1" and quantidade_de_vezes_que_pode_usar_o_efeito == 0:
                        os.system('cls')
                        print("nao pode mais usar esse efeito!")
                    elif choice == "2":
                        os.system('cls')
                        break
                    else:
                        os.system('cls')
