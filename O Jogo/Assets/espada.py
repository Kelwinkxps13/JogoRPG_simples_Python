class Espada:
    def __init__(self):
        self._name = ""
        self._atk_base = 0
        self._taxa = 0
        self._dano = 0
        self._afetado = ""
        self._quantidade = 0
        self._tempo = 0
        self._quantidade_de_vezes_que_pode_usar = 0
        self._descricao_efeito = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def atk_base(self):
        return self._atk_base

    @atk_base.setter
    def atk_base(self, atk_base):
        self._atk_base = atk_base

    @property
    def taxa(self):
        return self._taxa

    @taxa.setter
    def taxa(self, taxa):
        self._taxa = taxa

    @property
    def dano(self):
        return self._dano

    @dano.setter
    def dano(self, dano):
        self._dano = dano

    @property
    def afetado(self):
        return self._afetado

    @afetado.setter
    def afetado(self, afetado):
        self._afetado = afetado

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade

    @property
    def tempo(self):
        return self._tempo

    @tempo.setter
    def tempo(self, tempo):
        self._tempo = tempo

    @property
    def quantidade_de_vezes_que_pode_usar(self):
        return self._quantidade_de_vezes_que_pode_usar

    @quantidade_de_vezes_que_pode_usar.setter
    def quantidade_de_vezes_que_pode_usar(self, quantidade_de_vezes_que_pode_usar):
        self._quantidade_de_vezes_que_pode_usar = quantidade_de_vezes_que_pode_usar

    @property
    def descricao_efeito(self):
        return self._descricao_efeito

    @descricao_efeito.setter
    def descricao_efeito(self, descricao_efeito):
        self._descricao_efeito = descricao_efeito
        # aumenta ... em ... durante ... rodadas