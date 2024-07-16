from Assets.combate import Combate
import os
import sys
class Mapa_teste:
    def __init__(self):
        self._player = None
        self._array_enemies = [None] *2
    
    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, player):
        self._player = player
    @property
    def array_enemies(self):
        return self._array_enemies
    @array_enemies.setter
    def array_enemies(self, array_enemies):
        self._array_enemies = array_enemies
    
    def mapa_aberto(self):
        while True:
            print("")
            print("#########################################################")
            print("")
            print('[1] ir para o local 1')
            print('[2] encerrar Programa')
            c = input('> ')
            if c == "1":
                os.system('cls')
                self.local1()
            elif c == "2":
                sys.exit()
            else:
                os.system('cls')

    def reiniciar_hp(self, personagem):
        # Reinitialize the enemy's health or any other required attributes for a new battle
        personagem.hp_atual = personagem.hp_base
        # Add more reinitialization if needed

    def local1(self):
        while True:
            print("")
            print("#########################################################")
            print("")
            print('Você chega em um ambiente com alguns inimigos. Escolha quem enfrentar:')
            print(f'[1] {self._array_enemies[0].name} lv{self._array_enemies[0].level.atual_level}')
            print(f'[2] {self._array_enemies[1].name} lv{self._array_enemies[1].level.atual_level}')
            print("[3] voltar")
            c = input('> ')
            if c == "1":
                os.system('cls')
                print(f"Iniciando batalha contra {self._array_enemies[0].name}...")
                x = Combate.acao(self._player, self._array_enemies[0])
                print(f"Resultado da batalha: {x}")
                if x == False:
                    print(f"Batalha vencida! Ganhando XP...")
                    self._player.ganhar_xp_while(10)
                    self.reiniciar_hp(self._array_enemies[0])
                    self.reiniciar_hp(self._player)
                else:
                    print(f"Batalha perdida.")
                input("Pressione Enter para continuar...")  # Para pausar antes de limpar a tela
                os.system('cls')
            elif c == "2":
                os.system('cls')
                print(f"Iniciando batalha contra {self._array_enemies[1].name}...")
                x = Combate.acao(self._player, self._array_enemies[1])
                print(f"Resultado da batalha: {x}")
                if x == False:
                    print(f"Batalha vencida! Ganhando XP...")
                    self._player.ganhar_xp_while(20)
                    self.reiniciar_hp(self._array_enemies[1])
                    self.reiniciar_hp(self._player)
                else:
                    print(f"Batalha perdida.")
                input("Pressione Enter para continuar...")  # Para pausar antes de limpar a tela
                os.system('cls')
            elif c == "3":
                os.system('cls')
                break
            else:
                os.system('cls')