import os 

class Combate:

    # def __init__(self):
    #     self._player = []
    #     self._enemy = []

    # @property
    # def player(self):    
    #     return self._player

    # @player.setter
    # def player(self, player):
    #     self._player = player

    # @property
    # def enemy(self):    
    #     return self._enemy

    # @enemy.setter
    # def enemy(self, enemy):
    #     self._enemy = enemy


    def acao(player, enemy):
        
        
        rodadas_efeito_arma = 0
        count_rodadas = 1
        efeito_arma = False
        quantidade_de_vezes_que_pode_usar_o_efeito = player.arma.quantidade_de_vezes_que_pode_usar

        while player.hp_atual > 0 and enemy.hp_atual > 0:

            if rodadas_efeito_arma == 0 and efeito_arma == True:
                print(f'o efeito da arma {player.arma.name} acabou!')
                player.desativar_efeito_arma()
                efeito_arma = False

            print("")
            print("#########################################################")
            print("")

            if efeito_arma:
                print(f'rodadas restantes do efeito da arma: {rodadas_efeito_arma}')

            print(f'rodada: {count_rodadas}')
            print("")
            print(f'nv{player.level.atual_level}')
            print(f'xp: {player.level.atual_xp}/{player.level.xp_next_level}')
            print("")
            print(f'arma atual: {player.arma.name}')
            print(f'taxa critica: {player.arma.taxa}%')
            print(f'dano critico: {player.arma.dano}%')
            print(f'ataque base: {player.arma.atk_base}')
            print("")
            print(f'hp {player.name}: {player.hp_atual}/{player.hp_base}')
            print(f'hp {enemy.name}: {enemy.hp_atual}/{enemy.hp_base}')

            print("")
            print("#########################################################")
            print("")
            
            print("[1] atacar")
            print("[2] efeito de arma")
            choice = (input("> "))

            


            if choice == "1":
                os.system('cls')
                player.fight(enemy)

                if rodadas_efeito_arma >0 and efeito_arma:
                    rodadas_efeito_arma -=1

                count_rodadas += 1

                if enemy.hp_atual <=0:
                    print("voce ganhou!")
                    print(f'total de rodadas:{count_rodadas}')
                    return False

                else:
                    enemy.fight(player)
                    if player.hp_atual <=0:
                        print("voce perdeu!")
                        print(f'total de rodadas:{count_rodadas}')
                        return True

            elif choice == "2":

                os.system('cls')

                while True:
                    

                    print("")
                    print("#########################################################")
                    print("")

                    print(f'descrição: {player.arma.descricao_efeito}')
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
                            rodadas_efeito_arma = player.arma.tempo
                            efeito_arma = True
                            quantidade_de_vezes_que_pode_usar_o_efeito -= 1
                            player.ativar_efeito_arma()
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
            
            else:
                os.system('cls')