# cada raça tem um level e xp diferente

class Level:
    def __init__(self, atual_level, atual_xp, raca):

        self.max_level = [None] * (100+1)
        self.raca = raca

        if(self.raca == "humano"):

            self.max_level[0] = [0, 0]

            ilevel = 1
            count_dezena = 1
            ixp = 10 * count_dezena

            while ilevel <101:

                if ilevel >9:

                    if count_dezena == 10:
                        ixp *=10
                    self.max_level[ilevel] = [ilevel, ixp*count_dezena-1]

                    if count_dezena == 19:
                        count_dezena = 9

                else:

                    self.max_level[ilevel] = [ilevel, ixp*count_dezena-1]

                count_dezena += 1
                ilevel += 1

        self.atual_level = atual_level
        self.atual_xp = atual_xp
        self.xp_next_level = self.max_level[self.atual_level+1][1]



# lv1 - 10xp
# lv2 - 20xp
# lv3 - 30xp
# lv4 - 40xp
# lv5 - 50xp
# lv6 - 60xp
# lv7 - 70xp
# lv8 - 80xp
# lv9 - 90xp
# lv10 - 1000xp
# lv11 - 1100xp
# lv12 - 1200xp
# lv13 - 1300xp
# lv14 - 1400xp
# lv15 - 1500xp
# lv16 - 1600xp
# lv17 - 1700xp
# lv18 - 1800xp
# lv19 - 1900xp
# lv20 - 10000xp
# lv21 - 11000xp
# lv22 - 12000xp
# lv23 - 13000xp
# lv24 - 14000xp
# lv25 - 15000xp
# lv26 - 16000xp
# lv27 - 17000xp
# lv28 - 18000xp
# lv29 - 19000xp
# lv30 - 100000xp
# lv31 - 110000xp
# lv32 - 120000xp
# lv33 - 130000xp
# lv34 - 140000xp
# lv35 - 150000xp
# lv36 - 160000xp
# lv37 - 170000xp
# lv38 - 180000xp
# lv39 - 190000xp
# lv40 - 1000000xp

# ...

# lv100 =  ???