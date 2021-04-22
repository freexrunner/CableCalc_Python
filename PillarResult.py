# заготовка под dataclass
class PillarResult:
    def __init__(self,
                 Wcab,
                 WgolNorm,
                 Wgolol_1,
                 Wgolol_2,
                 WTGol,
                 Wgol_1,
                 Wgol_2,
                 KlLeft,
                 KlRight,
                 angkoef,
                 WGN_L,
                 WGN_R,
                 WG1_L,
                 WG2_L,
                 WG1_R,
                 WG2_R,
                 Wmax_1,
                 WmaxR_1,
                 Cx,
                 WLNormL,
                 WLNormR,
                 WL_1,
                 WR_1,
                 WL_2,
                 WR_2,
                 WvetR_1,
                 Wvet_1,
                 WcabLeft,
                 WcabRight,
                 line_max1_left,
                 line_max1_right,
                 line_vet1_left,
                 line_vet1_right,
                 line_gol1_left,
                 line_gol1_right,
                 Ki,
                 Kd,
                 Cg,
                 Kf,
                 av,
                 Kw,
                 vd,
                 avg,
                 t1_2L,
                 t1_2R,
                 t1_1L,
                 t1_1R,
                 t1_3L,
                 t1_3R,
                 t1_4R,
                 g1_1,
                 g1_2,
                 g2_1,
                 g2_2,
                 p1_1,
                 p2_1,
                 p1_2,
                 p2_2,
                 g1_4,
                 diam,
                 len_left,
                 len_right,
                 str_left,
                 str_right,
                 massa,
                 sech,
                 modul,
                 tklr,
                 temp,
                 vet,
                 gol,
                 land):
        self.Wcab = Wcab
        self.WgolNorm = WgolNorm
        self.Wgolol_1 = Wgolol_1
        self.Wgolol_2 = Wgolol_2
        self.WTGol = WTGol
        self.Wgol_1 = Wgol_1
        self.Wgol_2 = Wgol_2
        self.KlLeft = KlLeft
        self.KlRight = KlRight
        self.angkoef = angkoef
        self.WGN_L = WGN_L
        self.WGN_R = WGN_R
        self.WG1_L = WG1_L
        self.WG2_L = WG2_L
        self.WG1_R = WG1_R
        self.WG2_R = WG2_R
        self.Wmax_1 = Wmax_1
        self.WmaxR_1 = WmaxR_1
        self.Cx = Cx
        self.WLNormL = WLNormL
        self.WLNormR = WLNormR
        self.WL_1 = WL_1
        self.WR_1 = WR_1
        self.WL_2 = WL_2
        self.WR_2 = WR_2
        self.WvetR_1 = WvetR_1
        self.Wvet_1 = Wvet_1
        self.WcabLeft = WcabLeft
        self.WcabRight = WcabRight
        self.line_max1_left = line_max1_left
        self.line_max1_right = line_max1_right
        self.line_vet1_left = line_vet1_left
        self.line_vet1_right = line_vet1_right
        self.line_gol1_left = line_gol1_left
        self.line_gol1_right = line_gol1_right
        self.Ki = Ki
        self.Kd = Kd
        self.Cg = Cg
        self.Kf = Kf
        self.av = av
        self.Kw = Kw
        self.vd = vd
        self.avg = avg
        self.t1_2L = t1_2L
        self.t1_2R = t1_2R
        self.t1_1L = t1_1L
        self.t1_1R = t1_1R
        self.t1_3L = t1_3L
        self.t1_3R = t1_3R
        self.t1_4R = t1_4R
        self.g1_1 = g1_1
        self.g1_2 = g1_2
        self.g2_1 = g2_1
        self.g2_2 = g2_2
        self.p1_1 = p1_1
        self.p2_1 = p2_1
        self.p1_2 = p1_2
        self.p2_2 = p2_2
        self.g1_4 = g1_4
        self.diam = diam
        self.len_left = len_left
        self.len_right = len_right
        self.str_left = str_left
        self.str_right = str_right
        self.massa = massa
        self.sech = sech
        self.modul = modul
        self.tklr = tklr
        self.temp = temp
        self.vet = vet
        self.gol = gol
        self.land = land
        
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
        pill_key_r[1] = str(self.WcabLeft)
        pill_key[2] = "#left_Self"
        pill_key_r[2] = str(self.WcabRight)
        pill_key[3] = "#Ki"
        pill_key_r[3] = str(self.Ki)
        pill_key[4] = "#Kd"
        pill_key_r[4] = str(self.Kd)
        pill_key[5] = "#cg"
        pill_key_r[5] = str(self.Cg)  # проверить!!!
        pill_key[6] = "#diam"
        pill_key_r[6] = str(self.diam)
        pill_key[7] = "#gol_Norm"
        pill_key_r[7] = str(self.WgolNorm)
        pill_key[8] = "#Kf"
        pill_key_r[8] = str(self.Kf)
        pill_key[9] = "#gol_1"
        pill_key_r[9] = str(self.Wgolol_1)
        pill_key[10] = "#gol_2"
        pill_key_r[10] = str(self.Wgolol_2)
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
        pill_key_r[16] = str(self.KlRight)
        pill_key[17] = "#Kw"
        pill_key_r[17] = str(self.Kw)
        pill_key[18] = "#Cx"
        pill_key_r[18] = str(self.Cx)
        pill_key[19] = "#vd"
        pill_key_r[19] = str(self.vd)
        pill_key[20] = "#Kl"
        pill_key_r[20] = str(self.KlLeft)
        pill_key[21] = "#vet_right_Norm"
        pill_key_r[21] = str(self.WLNormR)
        pill_key[22] = "#vet_left_Norm"
        pill_key_r[22] = str(self.WLNormL)
        pill_key[23] = "#vet_right_1"
        pill_key_r[23] = str(self.WR_1)
        pill_key[24] = "#vet_left_1"
        pill_key_r[24] = str(self.WL_1)
        pill_key[25] = "#vet_right_2"
        pill_key_r[25] = str(self.WR_2)
        pill_key[26] = "#vet_left_2"
        pill_key_r[26] = str(self.WL_2)
        pill_key[27] = "#P1_1"
        pill_key_r[27] = str(self.p1_1)
        pill_key[28] = "#P2_1"
        pill_key_r[28] = str(self.p2_1)
        pill_key[29] = "#agol"
        pill_key_r[29] = str(self.avg)
        pill_key[30] = "#vetgol_right_Norm"
        pill_key_r[30] = str(self.WGN_R)
        pill_key[31] = "#vetgol_left_Norm"
        pill_key_r[31] = str(self.WGN_L)
        pill_key[32] = "#vetgol_right_1"
        pill_key_r[32] = str(self.WG1_R)
        pill_key[33] = "#vetgol_left_1"
        pill_key_r[33] = str(self.WG1_L)
        pill_key[34] = "#vetgol_right_2"
        pill_key_r[34] = str(self.WG2_R)
        pill_key[35] = "#vetgol_left_2"
        pill_key_r[35] = str(self.WG2_L)
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
        pill_key_r[44] = str(self.Wcab)
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
        pill_key_r[54] = str(self.Wvet_1)
        pill_key[55] = "#nagrVet_right"
        pill_key_r[55] = str(self.WvetR_1)
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
        pill_key_r[68] = str(self.Wmax_1)
        pill_key[69] = "#nagrVetGol_right"
        pill_key_r[69] = str(self.WmaxR_1)
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
        pill_key_r[90] = land_r

        return pill_key, pill_key_r
