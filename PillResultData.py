# датакласс для результатов расчетов нагрузок на опору
from dataclasses import dataclass

# @dataclass
# class PillResultData:
#     wCab: float
#     wGolNorm: float
#     wGolol_1: float
#     wGolol_2: float
#     wTGol: float
#     wgol_1: float
#     wgol_2: float
#     klLeft: float
#     klRight: float
#     angkoef: float
#     wGN_L: float
#     wGN_R: float
#     wG1_L: float
#     wG2_L: float
#     wG1_R: float
#     wG2_R: float
#     wmax_1: float
#     wmaxR_1: float
#     cx: float
#     wLNormL: float
#     wLNormR: float
#     wL_1: float
#     wR_1: float
#     wL_2: float
#     wR_2: float
#     wvetR_1: float
#     wvet_1: float
#     wCabLeft: float
#     wCabRight: float
#     s2_left: float
#     t2_left: float
#     a2_left: float
#     b2_left: float
#     d2_left: float
#     startH_left: float
#     fact_length_left: float
#     start_length_left: float
#     Tem_length_left: float
#     s2_right: float
#     t2_right: float
#     a2_right: float
#     b2_right: float
#     d2_right: float
#     startH_right: float
#     fact_length_right: float
#     start_length_right: float
#     Tem_length_right: float
#     s1_left: float
#     t1_left: float
#     a1_left: float
#     b1_left: float
#     d1_left: float
#     s1_right: float
#     t1_right: float
#     a1_right: float
#     b1_right: float
#     d1_right: float
#     s3_left: float
#     t3_left: float
#     a3_left: float
#     b3_left: float
#     d3_left: float
#     s3_right: float
#     t3_right: float
#     a3_right: float
#     b3_right: float
#     d3_right: float
#     ki: float
#     kd: float
#     cg: float
#     kf: float
#     av: float
#     kw: float
#     vd: float
#     avg: float
#     t1_2L: float
#     t1_2R: float
#     t1_1L: float
#     t1_1R: float
#     t1_3L: float
#     t1_3R: float
#     t1_4R: float
#     g1_1: float
#     g1_2: float
#     g2_1: float
#     g2_2: float
#     p1_1: float
#     p2_1: float
#     p1_2: float
#     p2_2: float
#     g1_4: float
#     diam: float
#     len_left: float
#     len_right: float
#     str_left: float
#     str_right: float
#     massa: float
#     sech: float
#     modul: float
#     tklr: float
#     temp: float
#     vet_area: int
#     vet_area: int
#     land: str

# старый вариант
@dataclass
class PillResultData:
    wCab: float
    wGolNorm: float
    wGolol_1: float
    wGolol_2: float
    wTGol: float
    wgol_1: float
    wgol_2: float
    klLeft: float
    klRight: float
    angkoef: float
    wGN_L: float
    wGN_R: float
    wG1_L: float
    wG2_L: float
    wG1_R: float
    wG2_R: float
    wmax_1: float
    wmaxR_1: float
    cx: float
    wLNormL: float
    wLNormR: float
    wL_1: float
    wR_1: float
    wL_2: float
    wR_2: float
    wvetR_1: float
    wvet_1: float
    wCabLeft: float
    wCabRight: float
    line_max1_left: tuple
    line_max1_right: tuple
    line_vet1_left: tuple
    line_vet1_right: tuple
    line_gol1_left: tuple
    line_gol1_right: tuple
    ki: float
    kd: float
    cg: float
    kf: float
    av: float
    kw: float
    vd: float
    avg: float
    t1_2L: float
    t1_2R: float
    t1_1L: float
    t1_1R: float
    t1_3L: float
    t1_3R: float
    t1_4R: float
    g1_1: float
    g1_2: float
    g2_1: float
    g2_2: float
    p1_1: float
    p2_1: float
    p1_2: float
    p2_2: float
    g1_4: float
    diam: float
    len_left: float
    len_right: float
    str_left: float
    str_right: float
    massa: float
    sech: float
    modul: float
    tklr: float
    temp: float
    vet: int
    gol: int
    land: str

    def getKeys(self):

        if self.land == 0:
            land_r = "A - открытые пространства"
        if self.land == 1:
            land_r = "B - с препятствиями ниже опор"
        if self.land == 3:
            land_r = "С - с препятствиями выше опор"

        pill_key = {}
        pill_key_r = {}

        pill_key[0] = "#G1_1"
        pill_key_r[0] = str(self.g1_1)
        pill_key[1] = "#right_Self"
        pill_key_r[1] = str(self.wCabLeft)
        pill_key[2] = "#left_Self"
        pill_key_r[2] = str(self.wCabRight)
        pill_key[3] = "#Ki"
        pill_key_r[3] = str(self.ki)
        pill_key[4] = "#Kd"
        pill_key_r[4] = str(self.kd)
        pill_key[5] = "#cg"
        pill_key_r[5] = str(self.cg)  # проверить!!!
        pill_key[6] = "#diam"
        pill_key_r[6] = str(self.diam)
        pill_key[7] = "#gol_Norm"
        pill_key_r[7] = str(self.wGolNorm)
        pill_key[8] = "#Kf"
        pill_key_r[8] = str(self.kf)
        pill_key[9] = "#gol_1"
        pill_key_r[9] = str(self.wGolol_1)
        pill_key[10] = "#gol_2"
        pill_key_r[10] = str(self.wGolol_2)
        pill_key[11] = "#len_Left"
        pill_key_r[11] = str(self.len_left)
        pill_key[12] = "#len_Right"
        pill_key_r[12] = str(self.len_right)
        pill_key[13] = "#G1_2"
        pill_key_r[13] = str(self.g1_2)
        pill_key[14] = "#G2_2"
        pill_key_r[14] = str(self.g2_2)
        pill_key[15] = "#av"
        pill_key_r[15] = str(self.av)
        pill_key[16] = "#KlR"
        pill_key_r[16] = str(self.klRight)
        pill_key[17] = "#Kw"
        pill_key_r[17] = str(self.kw)
        pill_key[18] = "#Cx"
        pill_key_r[18] = str(self.cx)
        pill_key[19] = "#vd"
        pill_key_r[19] = str(self.vd)
        pill_key[20] = "#Kl"
        pill_key_r[20] = str(self.klLeft)
        pill_key[21] = "#vet_right_Norm"
        pill_key_r[21] = str(self.wLNormR)
        pill_key[22] = "#vet_left_Norm"
        pill_key_r[22] = str(self.wLNormL)
        pill_key[23] = "#vet_right_1"
        pill_key_r[23] = str(self.wR_1)
        pill_key[24] = "#vet_left_1"
        pill_key_r[24] = str(self.wL_1)
        pill_key[25] = "#vet_right_2"
        pill_key_r[25] = str(self.wR_2)
        pill_key[26] = "#vet_left_2"
        pill_key_r[26] = str(self.wL_2)
        pill_key[27] = "#P1_1"
        pill_key_r[27] = str(self.p1_1)
        pill_key[28] = "#P2_1"
        pill_key_r[28] = str(self.p2_1)
        pill_key[29] = "#agol"
        pill_key_r[29] = str(self.avg)
        pill_key[30] = "#vetgol_right_Norm"
        pill_key_r[30] = str(self.wGN_R)
        pill_key[31] = "#vetgol_left_Norm"
        pill_key_r[31] = str(self.wGN_L)
        pill_key[32] = "#vetgol_right_1"
        pill_key_r[32] = str(self.wG1_R)
        pill_key[33] = "#vetgol_left_1"
        pill_key_r[33] = str(self.wG1_L)
        pill_key[34] = "#vetgol_right_2"
        pill_key_r[34] = str(self.wG2_R)
        pill_key[35] = "#vetgol_left_2"
        pill_key_r[35] = str(self.wG2_L)
        pill_key[36] = "#P1_2"
        pill_key_r[36] = str(self.p1_2)
        pill_key[37] = "#P2_2"
        pill_key_r[37] = str(self.p2_2)
        pill_key[38] = "#strLeftSupp"
        pill_key_r[38] = str(self.str_left)
        pill_key[39] = "#strRightSupp"
        pill_key_r[39] = str(self.str_right)
        pill_key[40] = "#massa"
        pill_key_r[40] = str(self.massa)
        pill_key[41] = "#sech"
        pill_key_r[41] = str(self.sech)
        pill_key[42] = "#modul"
        pill_key_r[42] = str(self.modul)
        pill_key[43] = "#tklr"
        pill_key_r[43] = str(self.tklr * 1000000)
        pill_key[44] = "#cabWeight"
        pill_key_r[44] = str(self.wCab)
        pill_key[45] = "#startH_left"
        pill_key_r[45] = str(self.line_max1_left[5])
        pill_key[46] = "#startH_right"
        pill_key_r[46] = str(self.line_max1_right[5])
        pill_key[47] = "#fact_length_left"
        pill_key_r[47] = str(self.line_max1_left[6])
        pill_key[48] = "#fact_length_right"
        pill_key_r[48] = str(self.line_max1_right[6])
        pill_key[49] = "#start_length_left"
        pill_key_r[49] = str(self.line_max1_left[7])
        pill_key[50] = "#start_length_right"
        pill_key_r[50] = str(self.line_max1_right[7])
        pill_key[51] = "#temp"
        pill_key_r[51] = str(self.temp)
        pill_key[52] = "#Tem_length_left"
        pill_key_r[52] = str(self.line_max1_left[8])
        pill_key[53] = "#Tem_length_right"
        pill_key_r[53] = str(self.line_max1_right[8])
        pill_key[54] = "#nagrVet_left"
        pill_key_r[54] = str(self.wvet_1)
        pill_key[55] = "#nagrVet_right"
        pill_key_r[55] = str(self.wvetR_1)
        pill_key[56] = "#a1_left"
        pill_key_r[56] = str(self.line_vet1_left[2])
        pill_key[57] = "#b1_left"
        pill_key_r[57] = str(self.line_vet1_left[3])
        pill_key[58] = "#d1_left"
        pill_key_r[58] = str(self.line_vet1_left[4])
        pill_key[59] = "#s1_left"
        pill_key_r[59] = str(self.line_vet1_left[0])
        pill_key[60] = "#a1_right"
        pill_key_r[60] = str(self.line_vet1_right[2])
        pill_key[61] = "#b1_right"
        pill_key_r[61] = str(self.line_vet1_right[3])
        pill_key[62] = "#d1_right"
        pill_key_r[62] = str(self.line_vet1_right[4])
        pill_key[63] = "#s1_right"
        pill_key_r[63] = str(self.line_vet1_right[0])
        pill_key[64] = "#t1_left"
        pill_key_r[64] = str(self.line_vet1_left[1])
        pill_key[65] = "#t1_right"
        pill_key_r[65] = str(self.line_vet1_right[1])
        pill_key[66] = "#T1_1_left"
        pill_key_r[66] = str(self.t1_1L)
        pill_key[67] = "#T1_1_right"
        pill_key_r[67] = str(self.t1_1R)
        pill_key[68] = "#nagrVetGol_left"
        pill_key_r[68] = str(self.wmax_1)
        pill_key[69] = "#nagrVetGol_right"
        pill_key_r[69] = str(self.wmaxR_1)
        pill_key[70] = "#a2_left"
        pill_key_r[70] = str(self.line_max1_left[2])
        pill_key[71] = "#b2_left"
        pill_key_r[71] = str(self.line_max1_left[3])
        pill_key[72] = "#d2_left"
        pill_key_r[72] = str(self.line_max1_left[4])
        pill_key[73] = "#s2_left"
        pill_key_r[73] = str(self.line_max1_left[0])
        pill_key[74] = "#a2_right"
        pill_key_r[74] = str(self.line_max1_right[2])
        pill_key[75] = "#b2_right"
        pill_key_r[75] = str(self.line_max1_right[3])
        pill_key[76] = "#d2_right"
        pill_key_r[76] = str(self.line_max1_right[4])
        pill_key[77] = "#s2_right"
        pill_key_r[77] = str(self.line_max1_right[0])
        pill_key[78] = "#t2_left"
        pill_key_r[78] = str(self.line_max1_left[1])
        pill_key[79] = "#t2_right"
        pill_key_r[79] = str(self.line_max1_right[1])
        pill_key[80] = "#T1_2_left"
        pill_key_r[80] = str(self.t1_2L)
        pill_key[81] = "#T1_2_right"
        pill_key_r[81] = str(self.t1_2R)
        pill_key[82] = "#G1_4"
        pill_key_r[82] = str(self.g1_4)
        pill_key[83] = "#t3_left"
        pill_key_r[83] = str(self.line_gol1_left[1])
        pill_key[84] = "#t3_right"
        pill_key_r[84] = str(self.line_gol1_right[1])
        pill_key[85] = "#G1_3"
        pill_key_r[85] = str(self.g1_2)
        pill_key[86] = "#T1_3_left"
        pill_key_r[86] = str(self.t1_3L)
        pill_key[87] = "#T1_3_right"
        pill_key_r[87] = str(self.t1_3R)
        pill_key[88] = "#vet_area"
        pill_key_r[88] = str(self.vet)
        pill_key[89] = "#gol_area"
        pill_key_r[89] = str(self.gol)
        pill_key[90] = "#land"
        pill_key_r[90] = self.land
        pill_key[91] = "#WTGol"
        pill_key_r[91] = str(self.wTGol)
        pill_key[92] = "#a3_left"
        pill_key_r[92] = str(self.line_gol1_left[2])
        pill_key[93] = "#a3_right"
        pill_key_r[93] = str(self.line_gol1_right[2])
        pill_key[94] = "#b3_left"
        pill_key_r[94] = str(self.line_gol1_left[3])
        pill_key[95] = "#b3_right"
        pill_key_r[95] = str(self.line_gol1_right[3])
        pill_key[96] = "#d3_left"
        pill_key_r[96] = str(self.line_gol1_left[4])
        pill_key[97] = "#d3_right"
        pill_key_r[97] = str(self.line_gol1_right[4])
        pill_key[98] = "#s3_left"
        pill_key_r[98] = str(self.line_gol1_left[0])
        pill_key[99] = "#s3_right"
        pill_key_r[99] = str(self.line_gol1_right[0])

        return pill_key, pill_key_r

