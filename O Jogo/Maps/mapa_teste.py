from Assets.combate import Combate
import os
import sys
import time

def dialogo(frase, speed):
    for caractere in frase:
        print(caractere, end='', flush=True)
        time.sleep(speed)
    print()
def pausa():
    dialogo("pressione enter para continuar...", 0.001)
    return input()
class Mapa_teste:
    def __init__(self):
        self._player = None
        self._array_enemies = [None] * 3
        self._info_local = None
        self._taverna_info = True
    
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
    @property
    def info_local(self):
        return self._info_local
    @info_local.setter
    def info_local(self, info_local):
        self._info_local = info_local
    
    def mapa_aberto(self):
        while True:
            texto = """
#########################################################
MAPA ABERTO
#########################################################
"""
            dialogo(texto, 0.001)
            print('[1] ir para o local 1')
            print('[2] encerrar Programa')
            print('[3] Taverna Teste')
            if self.info_local:
                print("[4] local secreto")
            c = input('> ')
            if c == "1":
                os.system('cls')
                self.local1()
            elif c == "2":
                sys.exit()
            elif c == "3":
                os.system('cls')
                self.taverna()
            elif c == "4" and self.info_local:
                os.system('cls')
                self.local_secreto()
            else:
                os.system('cls')

    def reiniciar_hp(self, personagem):
        # Reinitialize the enemy's health or any other required attributes for a new battle
        personagem.hp_atual = personagem.hp_base
        # Add more reinitialization if needed



    def local1(self):
        while True:
            texto = """
#########################################################
LOCAL 1
#########################################################
Você chega em um ambiente com alguns inimigos. Escolha quem enfrentar:
"""

            dialogo(texto, 0.001)
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
                input("Pressione Enter para continuar...")
                self.reiniciar_hp(self._array_enemies[0])
                self.reiniciar_hp(self._player)
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
                input("Pressione Enter para continuar...")
                self.reiniciar_hp(self._array_enemies[0])
                self.reiniciar_hp(self._player)
                os.system('cls')
            elif c == "3":
                os.system('cls')
                break
            else:
                os.system('cls')
    def taverna(self):
        while True:
            texto = """
#########################################################
TAVERNA TESTE
#########################################################
"""

            dialogo(texto, 0.001)
            print("[1] voltar")
            if self._taverna_info:
                print("[2] pedir informaçao sobre um local com inimigos")
            
            c = input('> ')
            if c == "1":
                os.system('cls')
                break
            
            elif c == "2" and self._taverna_info:
                os.system('cls')
                self.conversa1_taverna()
            elif c == "2" and self._taverna_info == False:
                os.system('cls')
            else:
                os.system('cls')
    def conversa1_taverna(self):
        loop_externo = True
        while loop_externo:
            texto = """
#########################################################
CONVERSA COM BARMAN
#########################################################

Barman: você quer saber sobre um local com inimigos mais interessantes né
"""

            dialogo(texto, 0.001)
            print("[1] concordar")
            print("[2] voltar")
            c = input('> ')
            if c == "1":
                os.system('cls')
                while True:
                    print("")
                    print("#########################################################")
                    print("")
                    dialogo("Barman: bom meu amigo você veio ao local certo, conheco um otimo lugar...", 0.05)
                    pausa()
                    os.system("cls")
                    dialogo("Barman: fica perto do lago a esquerda da praça central...", 0.05)
                    pausa()
                    os.system("cls")
                    dialogo(f'{self._player.name}: Tem alguma rota daqui pra chegar la rapido?', 0.05)
                    pausa()
                    os.system("cls")
                    dialogo("Barman: infelizmente nao, mas voce vai saber rapidamente onde fica o local...", 0.05)
                    pausa()
                    os.system("cls")
                    dialogo("Barman: assim que sair dessa taverna", 0.05)
                    pausa()
                    os.system("cls")
                    dialogo(f'{self._player.name}: Certo entao, valeu pela informaçao.', 0.05)
                    pausa()
                    os.system("cls")
                    loop_externo = False
                    self._info_local = True
                    self._taverna_info = False
                    os.system("cls")
                    break
            elif c == "2":
                os.system('cls')
                break
            else:
                os.system('cls')
    def local_secreto(self):
        print("batalha contra um mini chefe!!")
        x = Combate.acao(self._player, self._array_enemies[2])
        if x == False:
            print(f"Batalha vencida! Ganhando XP...")
            self._player.ganhar_xp_while(70)
            self.reiniciar_hp(self._array_enemies[2])
            self.reiniciar_hp(self._player)
        else:
            print(f"Batalha perdida.")
            self.reiniciar_hp(self._array_enemies[2])
            self.reiniciar_hp(self._player)
        input("Pressione Enter para continuar...")
        os.system('cls')