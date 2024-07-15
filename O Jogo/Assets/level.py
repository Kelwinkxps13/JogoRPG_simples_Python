# cada raça tem um level e xp diferente

class Level:
    def __init__(self):

        self._max_level = [None] * (100+1)
        self._raca = "humano"

        if(self.raca == "humano"):

            self._max_level[0] = [0, 0, 0]

            ilevel = 1
            count_dezena = 1
            ixp = 10 * count_dezena

            while ilevel <101:

                if ilevel >9:

                    if count_dezena == 10:
                        ixp *=10
                    self._max_level[ilevel] = [ilevel, ixp*count_dezena-1, ilevel*100]

                    if count_dezena == 19:
                        count_dezena = 9

                else:

                    self._max_level[ilevel] = [ilevel, ixp*count_dezena-1, ilevel*100]

                count_dezena += 1
                ilevel += 1

        self._atual_level = 0
        self._atual_xp = 0
        self._xp_next_level = ""

    @property
    def max_level(self):
        return self._max_level

    @property
    def raca(self):
        return self._raca

    @property
    def atual_level(self):
        return self._atual_level

    @atual_level.setter
    def atual_level(self, atual_level):
        self._atual_level = atual_level
        if self._atual_level < 100:
            self._xp_next_level = self._max_level[self._atual_level+1][1]
        else:
            self._xp_next_level = "--"

    @property
    def atual_xp(self):
        return self._atual_xp

    @atual_xp.setter
    def atual_xp(self, atual_xp):
        self._atual_xp = atual_xp

    @property
    def xp_next_level(self):
        return self._xp_next_level
    
    @xp_next_level.setter
    def xp_next_level(self, xp_next_level):
        self._xp_next_level = xp_next_level



# lv1 - 10xp - 100hp
# lv2 - 20xp - 200hp
# lv3 - 30xp - 300hp
# lv4 - 40xp - 400hp
# lv5 - 50xp - 500hp
# lv6 - 60xp - 600hp
# lv7 - 70xp - 700hp
# lv8 - 80xp - 800hp
# lv9 - 90xp - 900hp
# lv10 - 1000xp - 1000hp
# lv11 - 1100xp - 1100hp
# lv12 - 1200xp - 1200hp
# lv13 - 1300xp - 1300hp
# lv14 - 1400xp - 1400hp
# lv15 - 1500xp - 1500hp
# lv16 - 1600xp - 1600hp
# lv17 - 1700xp - 1700hp
# lv18 - 1800xp - hp
# lv19 - 1900xp - hp
# lv20 - 10000xp - hp
# lv21 - 11000xp - hp
# lv22 - 12000xp - hp
# lv23 - 13000xp - hp
# lv24 - 14000xp - hp
# lv25 - 15000xp - hp
# lv26 - 16000xp - hp
# lv27 - 17000xp - hp
# lv28 - 18000xp - hp
# lv29 - 19000xp - hp
# lv30 - 100000xp - hp
# lv31 - 110000xp - hp
# lv32 - 120000xp - hp
# lv33 - 130000xp - hp
# lv34 - 140000xp - hp
# lv35 - 150000xp - hp
# lv36 - 160000xp - hp
# lv37 - 170000xp - hp
# lv38 - 180000xp - hp
# lv39 - 190000xp - hp
# lv40 - 1000000xp - hp

# ...

# lv100 =  ???