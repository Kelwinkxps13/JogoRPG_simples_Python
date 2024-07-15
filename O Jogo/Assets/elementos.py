# Elementos

# "fogo",   forte:vento ,fraco: agua
# "vento",  forte:raio  ,fraco: fogo
# "raio" ,  forte:terra ,fraco: vento
# "terra"   forte:agua  ,fraco: raio
# "agua"    forte:fogo  ,fraco: terra

# "luz"
# "trevas"

# esses 5 sao os elementos base da terra.
# qualquer ser vivo pode conjurar feitiços com esses 5 elementos,
# nao ha restricao para qual usuario use cada tipo de elemento.


# reacoes elementais

# - reacao:(fogo-vento), nome_reacao: propagaçao,
# - reacao:(vento-fogo), nome_reacao: propagaçao,
# - reacao:(fogo-raio), nome_reacao: eletrofogo,
# - reacao:(raio-fogo), nome_reacao: eletrofogo,
# - reacao:(fogo-terra), nome_reacao: Calcinação,
# - reacao:(terra-fogo), nome_reacao: Calcinação,
# - reacao:(fogo-agua), nome_reacao: vaporizaçao,
# - reacao:(agua-fogo), nome_reacao: vaporizaçao,
# - reacao:(vento-raio), nome_reacao: Tempestade,
# - reacao:(raio-vento), nome_reacao: Tempestade,
# - reacao:(vento-terra), nome_reacao: Erosão,
# - reacao:(terra-vento), nome_reacao: Erosão,
# - reacao:(vento-agua), nome_reacao: Tempestade Marítima,
# - reacao:(agua-vento), nome_reacao: Tempestade Marítima,
# - reacao:(raio-terra), nome_reacao: Petrificação,
# - reacao:(terra-raio), nome_reacao: Petrificação,
# - reacao:(raio-agua), nome_reacao: condutividade,
# - reacao:(agua-raio), nome_reacao: condutividade,
# - reacao:(terra-agua), nome_reacao: Lama,
# - reacao:(agua-terra), nome_reacao: Lama,

class Elementos:
    def __init__ (self):
        self._name = ""
        self._superior_a = ""
        self._inferior_a = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def superior_a(self):
        return self._superior_a

    @superior_a.setter
    def superior_a(self, superior_a):
        self._superior_a = superior_a

    @property
    def inferior_a(self):
        return self._inferior_a

    @inferior_a.setter
    def inferior_a(self, inferior_a):
        self._inferior_a = inferior_a