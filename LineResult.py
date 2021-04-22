# заготовка под dataclass
class LineResult:
    def __init__(self,
                 vetr_str,
                 gol_str,
                 vd,
                 cg,
                 land,
                 length,
                 str_nach,
                 cable_name,
                 massa,
                 diam,
                 sech,
                 modul,
                 tklr,
                 str_norm,
                 nagr_norm,
                 str_gol,
                 nagr_gol,
                 str_vet,
                 nagr_vet,
                 str_vet_gol,
                 nagr_vet_gol,
                 str_min_30,
                 str_min_20,
                 str_min_10,
                 str_0,
                 str_10,
                 str_20,
                 str_30,
                 str_40,
                 str_50,
                 str_60,
                 str_70,
                 nagr_min_30,
                 nagr_min_20,
                 nagr_min_10,
                 nagr_0,
                 nagr_10,
                 nagr_20,
                 nagr_30,
                 nagr_40,
                 nagr_50,
                 nagr_60,
                 nagr_70,
                 cab_weight,
                 start_h,
                 fact_length,
                 start_length,
                 temp,
                 temp_length,
                 a_norm,
                 b_norm,
                 d_norm,
                 calc_length,
                 gol_norm,
                 ki,
                 kd,
                 kf,
                 golol,
                 wt_gol,
                 a_gol,
                 b_gol,
                 d_gol,
                 av,
                 kl,
                 kw,
                 cx,
                 vet_norm,
                 vet_r,
                 vet_metr,
                 w_vet_r,
                 a_vet,
                 b_vet,
                 d_vet,
                 agol,
                 vet_gol_norm,
                 vet_gol_r,
                 vet_gol_metr,
                 w_vet_gol,
                 a_vet_gol,
                 b_vet_gol,
                 d_vet_gol,
                 vg,
                 line_warning):
        self.vetr_str = vetr_str
        self.gol_str = gol_str
        self.vd = vd
        self.cg = cg
        self.land = land
        self.length = length
        self.str_nach = str_nach
        self.cable_name = cable_name
        self.massa = massa
        self.diam = diam
        self.sech = sech
        self.modul = modul
        self.tklr = tklr
        self.str_norm = str_norm
        self.nagr_norm = nagr_norm
        self.str_gol = str_gol
        self.nagr_gol = nagr_gol
        self.str_vet = str_vet
        self.nagr_vet = nagr_vet
        self.str_vet_gol = str_vet_gol
        self.nagr_vet_gol = nagr_vet_gol
        self.str_min_30 = str_min_30
        self.str_min_20 = str_min_20
        self.str_min_10 = str_min_10
        self.str_0 = str_0
        self.str_10 = str_10
        self.str_20 = str_20
        self.str_30 = str_30
        self.str_40 = str_40
        self.str_50 = str_50
        self.str_60 = str_60
        self.str_70 = str_70
        self.nagr_min_30 = nagr_min_30
        self.nagr_min_20 = nagr_min_20
        self.nagr_min_10 = nagr_min_10
        self.nagr_0 = nagr_0
        self.nagr_10 = nagr_10
        self.nagr_20 = nagr_20
        self.nagr_30 = nagr_30
        self.nagr_40 = nagr_40
        self.nagr_50 = nagr_50
        self.nagr_60 = nagr_60
        self.nagr_70 = nagr_70
        self.cab_weight = cab_weight
        self.start_h = start_h
        self.fact_length = fact_length
        self.start_length = start_length
        self.temp = temp
        self.temp_length = temp_length
        self.a_norm = a_norm
        self.b_norm = b_norm
        self.d_norm = d_norm
        self.calc_length = calc_length
        self.gol_norm = gol_norm
        self.ki = ki
        self.kd = kd
        self.kf = kf
        self.golol = golol
        self.wt_gol = wt_gol
        self.a_gol = a_gol
        self.b_gol = b_gol
        self.d_gol = d_gol
        self.av = av
        self.kl = kl
        self.kw = kw
        self.cx = cx
        self.vet_norm = vet_norm
        self.vet_r = vet_r
        self.vet_metr = vet_metr
        self.w_vet_r = w_vet_r
        self.a_vet = a_vet
        self.b_vet = b_vet
        self.d_vet = d_vet
        self.agol = agol
        self.vet_gol_norm = vet_gol_norm
        self.vet_gol_r = vet_gol_r
        self.vet_gol_metr = vet_gol_metr
        self.w_vet_gol = w_vet_gol
        self.a_vet_gol = a_vet_gol
        self.b_vet_gol = b_vet_gol
        self.d_vet_gol = d_vet_gol
        self.vg = vg
        self.line_warning = line_warning

    def getKeys(self):

        if self.land == 0:
            land_r = "A - открытые пространства"
        if self.land == 1:
            land_r = "B - с препятствиями ниже опор"
        if self.land == 3:
            land_r = "С - с препятствиями выше опор"

        key = {}
        key_r = {}

        key[0] = "#vet_area"
        key_r[0] = str(self.vetr_str)
        key[1] = "#gol_area"
        key_r[1] = str(self.gol_str)
        key[2] = "#vd"
        key_r[2] = str(self.vd)
        key[3] = "#cg"
        key_r[3] = str(self.cg)
        key[4] = "#land"
        key_r[4] = land_r
        key[5] = "#len_Line"
        key_r[5] = str(self.length)
        key[6] = "#str_Line"
        key_r[6] = str(self.str_nach)
        key[7] = "xxxx"
        key_r[7] = self.cable_name
        key[8] = "#massa"
        key_r[8] = str(self.massa)
        key[9] = "#diam"
        key_r[9] = str(self.diam)
        key[10] = "#sech"
        key_r[10] = str(self.sech)
        key[11] = "#modul"
        key_r[11] = str(self.modul)
        key[12] = "#tklr"
        key_r[12] = str(self.tklr * 1000000)
        key[13] = "#strNorm"
        key_r[13] = str(self.str_norm)
        key[14] = "#nagrNorm"
        key_r[14] = str(self.nagr_norm)
        key[15] = "#strGol"
        key_r[15] = str(self.str_gol)
        key[16] = "#nagrGol"
        key_r[16] = str(self.nagr_gol)
        key[17] = "#strVet"
        key_r[17] = str(self.str_vet)
        key[18] = "#nagrVet"
        key_r[18] = str(self.nagr_vet)
        key[19] = "#str_Vet_Gol"
        key_r[19] = str(self.str_vet_gol)
        key[20] = "#nagr_Vet_Gol"
        key_r[20] = str(self.nagr_vet_gol)
        key[21] = "#strmin30"
        key_r[21] = str(self.str_min_30)
        key[22] = "#strmin20"
        key_r[22] = str(self.str_min_20)
        key[23] = "#strmin10"
        key_r[23] = str(self.str_min_10)
        key[24] = "#str0"
        key_r[24] = str(self.str_0)
        key[25] = "#str10"
        key_r[25] = str(self.str_10)
        key[26] = "#str20"
        key_r[26] = str(self.str_20)
        key[27] = "#str30"
        key_r[27] = str(self.str_30)
        key[28] = "#str40"
        key_r[28] = str(self.str_40)
        key[29] = "#str50"
        key_r[29] = str(self.str_50)
        key[30] = "#str60"
        key_r[30] = str(self.str_60)
        key[31] = "#str70"
        key_r[31] = str(self.str_70)
        key[32] = "#nagrmin30"
        key_r[32] = str(self.nagr_min_30)
        key[33] = "#nagrmin20"
        key_r[33] = str(self.nagr_min_20)
        key[34] = "#nagrmin10"
        key_r[34] = str(self.nagr_min_10)
        key[35] = "#nagr0"
        key_r[35] = str(self.nagr_0)
        key[36] = "#nagr10"
        key_r[36] = str(self.nagr_10)
        key[37] = "#nagr20"
        key_r[37] = str(self.nagr_20)
        key[38] = "#nagr30"
        key_r[38] = str(self.nagr_30)
        key[39] = "#nagr40"
        key_r[39] = str(self.nagr_40)
        key[40] = "#nagr50"
        key_r[40] = str(self.nagr_50)
        key[41] = "#nagr60"
        key_r[41] = str(self.nagr_60)
        key[42] = "#nagr70"
        key_r[42] = str(self.nagr_70)
        key[43] = "#cabWeight"
        key_r[43] = str(self.cab_weight)
        key[44] = "#startH"
        key_r[44] = str(self.start_h)
        key[45] = "#fact_length"
        key_r[45] = str(self.fact_length)
        key[46] = "#start_length"
        key_r[46] = str(self.start_length)
        key[47] = "#temp"
        key_r[47] = str(self.temp)
        key[48] = "#Tem_length"
        key_r[48] = str(self.temp_length)
        key[49] = "#a_Norm"
        key_r[49] = str(self.a_norm)
        key[50] = "#b_Norm"
        key_r[50] = str(self.b_norm)
        key[51] = "#d_Norm"
        key_r[51] = str(self.d_norm)
        key[52] = "#calc_length"
        key_r[52] = str(self.calc_length)
        key[53] = "#golNorm"
        key_r[53] = str(self.gol_norm)
        key[54] = "#Ki"
        key_r[54] = str(self.ki)
        key[55] = "#Kd"
        key_r[55] = str(self.kd)
        key[56] = "#Kf"
        key_r[56] = str(self.kf)
        key[57] = "#golol"
        key_r[57] = str(self.golol)
        key[58] = "#WTGol"
        key_r[58] = str(self.wt_gol)
        key[59] = "#a_Gol"
        key_r[59] = str(self.a_gol)
        key[60] = "#b_Gol"
        key_r[60] = str(self.b_gol)
        key[61] = "#d_Gol"
        key_r[61] = str(self.d_gol)
        key[62] = "#av"
        key_r[62] = str(self.av)
        key[63] = "#Kl"
        key_r[63] = str(self.kl)
        key[64] = "#Kw"
        key_r[64] = str(self.kw)
        key[65] = "#Cx"
        key_r[65] = str(self.cx)
        key[66] = "#vetNorm"
        key_r[66] = str(self.vet_norm)
        key[67] = "#vetR"
        key_r[67] = str(self.vet_r)
        key[68] = "#vetMetr"
        key_r[68] = str(self.vet_metr)
        key[69] = "#WvetR"
        key_r[69] = str(self.w_vet_r)
        key[70] = "#a_vet"
        key_r[70] = str(self.a_vet)
        key[71] = "#b_vet"
        key_r[71] = str(self.b_vet)
        key[72] = "#d_vet"
        key_r[72] = str(self.d_vet)
        key[73] = "#agol"
        key_r[73] = str(self.agol)
        key[74] = "#vetgolNorm"
        key_r[74] = str(self.vet_gol_norm)
        key[75] = "#vetgolR"
        key_r[75] = str(self.vet_gol_r)
        key[76] = "#vetgolMetr"
        key_r[76] = str(self.vet_gol_metr)
        key[77] = "#Wvetgol"
        key_r[77] = str(self.w_vet_gol)
        key[78] = "#aa_vetgol"
        key_r[78] = str(self.a_vet_gol)
        key[79] = "#bb_vetgol"
        key_r[79] = str(self.b_vet_gol)
        key[80] = "#dd_vetgol"
        key_r[80] = str(self.d_vet_gol)
        key[81] = "#vg"
        key_r[81] = str(self.vg)

        return key, key_r

