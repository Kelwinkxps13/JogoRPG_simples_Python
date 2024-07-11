class Espada:
    def __init__(self, name, atk_base, taxa, dano):
        self.name = name
        self.atk_base = atk_base
        self.taxa = taxa
        self.dano = dano

        self.afetado = ""
        self.quantidade = 0
        self.tempo = 0
        self.quantidade_de_vezes_que_pode_usar = 0
        self.descricao_efeito = ""

    def set_afetado (self, afetado):
            self.afetado = afetado

    def set_quantidade (self, quantidade):
            self.quantidade = quantidade

    def set_tempo (self, tempo):
            self.tempo = tempo

    def set_descricao_efeito (self, descricao_efeito):
            self.descricao_efeito = descricao_efeito

    def set_quantidade_de_vezes_que_pode_usar (self, quantidade_de_vezes_que_pode_usar):
            self.quantidade_de_vezes_que_pode_usar = quantidade_de_vezes_que_pode_usar

    def ativar_efeito(self):
            if(self.afetado == "taxa critica"):
                self.taxa += self.quantidade
            elif(self.afetado == "dano critico"):
                self.dano += self.quantidade
            elif(self.afetado == "ataque base"):
                self.atk_base += self.quantidade

    def desativar_efeito(self):
            if(self.afetado == "taxa critica"):
                self.taxa -= self.quantidade
            elif(self.afetado == "dano critico"):
                self.dano -= self.quantidade
            elif(self.afetado == "ataque base"):
                self.atk_base -= self.quantidade
        # aumenta ... em ... durante ... rodadas

class Lanca:
    def __init__(self, name, atk_base, taxa, dano):
        self.name = name
        self.atk_base = atk_base
        self.taxa = taxa
        self.dano = dano

class Arco:
    def __init__(self, name, atk_base, taxa, dano):
        self.name = name
        self.atk_base = atk_base
        self.taxa = taxa
        self.dano = dano
