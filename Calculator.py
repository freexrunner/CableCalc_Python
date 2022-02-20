import math

from LineResultData import LineResultData
from PillResultData import PillResultData

class Calculator:
    def __init__(self, massa, diam, sech, modul, tklr, mdrn, temp, height, land, vet, gol):
        # self.lenLeftPole = None
        self.massa = massa
        self.diam = diam
        self.sech = sech
        self.modul = modul
        self.tklr = tklr
        self.mdrn = mdrn
        self.temp = temp
        self.height = height
        self.land = land
        self.vet = vet
        self.gol = gol



    def koef(self):
        # self.ki   #ki - коэффициент изменения ощины стенки гололеда по высоте (2.5.4. ПУЭ)
        # self.kw   #kw - коэффициент изменения ветрового давления по высоте в зависимости от типа местности и высоты (табл. 2.5.2 ПУЭ)
        # self.kd   #kd - коэффициент зменения толщины стенки гололеда в зависимости от диаметра провода
        # self.kf   #kf - коэффициент надежности по гололедной нагрузке (1.3 - 1 и 2 район, 1.6 - 3 и выше)

        if self.height <= 15.0:  # 15
            self.ki = 1.0
            hI = [1.0, 0.65, 0.4]
        if 15.0 < self.height <= 30.0:  # 20
            self.ki = 1.0
            hI = [1.25, 0.85, 0.55]
        if 30.0 < self.height <= 50.0:  # 40
            self.ki = 1.4
            hI = [1.5, 1.1, 0.8]
        if 50.0 < self.height <= 70.0:  # 60
            self.ki = 1.6
            hI = [1.7, 1.3, 1.0]
        if 70.0 < self.height <= 90.0:  # 80
            self.ki = 1.8
            hI = [1.85, 1.45, 1.15]
        if 90.0 < self.height <= 125.0:  # 100
            self.ki = 2.0
            hI = [2.0, 1.6, 1.25]
        if 125.0 < self.height <= 175.0:  # 150
            self.ki = 2.0
            hI = [2.25, 1.9, 1.55]
        if 175.0 < self.height <= 225.0:  # 200
            self.ki = 2.0
            hI = [2.45, 2.1, 1.8]
        if 225.0 < self.height <= 275.0:  # 250
            self.ki = 2.0
            hI = [2.65, 2.3, 2.0]
        if 275.0 < self.height <= 350.0:  # 300
            self.ki = 2.0
            hI = [2.75, 2.5, 2.2]
        if self.height > 350.0:  # 350+
            self.ki = 2.0
            hI = [2.75, 2.75, 2.35]

        self.kw = hI[self.land]

        if self.diam <= 15.0:
            self.kd = 1.0
        if 15.0 < self.diam <= 25.0:
            self.kd = 0.9
        if 25.0 < self.diam <= 35.0:
            self.kd = 0.8
        if 35.0 < self.diam <= 55.0:
            self.kd = 0.7
        if self.diam > 55.0:
            self.kd = 0.6

        if self.gol <= 2:
            self.kf = 1.3
        if self.gol > 2:
            self.kf = 1.6

    def land_str(self):

        if self.land == 0:
            land_r = "A - открытые пространства"
        if self.land == 1:
            land_r = "B - с препятствиями ниже опор"
        if self.land == 3:
            land_r = "С - с препятствиями выше опор"
        return land_r

    def lineCalc(self, lenth, strela, angle):

        # коэффициенты
        self.koef()

        line_warning = False

        # Вес кабеля, площадь сечения
        wCab = (self.massa * 9.8) / 1000

        # Начальная нагрузка
        hnul = ((wCab * (lenth ** 2)) / (8 * strela)) / 1000

        # Фактическая длина кабеля
        lenCab = lenth + ((8 * (strela ** 2)) / (3 * lenth))

        # Длина кабеля в ненагруженном состоянии
        lenNon = lenCab / (1 + (hnul / (self.modul * self.sech)))

        # Расчет монтажной таблицы
        tf = [-30, -20, -10, 0.0, 10, 20, 30, 40, 50, 60, 70]
        sf = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        hf = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for i in range(len(tf)):
            # Длина кабеля с учетом температуры
            lnk = lenNon * (1 + self.tklr * (tf[i] - self.temp))
            # Члены уравнения
            a = 3 * (lenth ** 2 - lenth * lnk) / 8
            b = (-3 * wCab * (lenth ** 3) * lnk) / (64 * self.modul * 1000 * self.sech)
            dis = ((a / 3) ** 3) + ((-b / 2) ** 2)
            if dis >= 0:
                X = (-b / 2) + (math.sqrt(dis))
                Y = (-b / 2) - (math.sqrt(dis))
                if X >= 0:
                    xcub = X ** (1.0 / 3)
                else:
                    xcub = (-1) * ((math.fabs(X)) ** (1.0 / 3))
                if Y >= 0:
                    ycub = Y ** (1.0 / 3)
                else:
                    ycub = (-1) * ((math.fabs(Y)) ** (1.0 / 3))
                sf[i] = xcub + ycub
            else:
                sf[i] = 2 * (math.sqrt(-a / 3)) * (
                    math.cos((1.0 / 3) * (math.acos((-b / 2) / ((-a / 3) ** (3.0 / 2.0))))))
            hf[i] = ((wCab * (lenth ** 2)) / (8 * sf[i])) / 1000
            if hf[i] > self.mdrn:
                line_warning = True

            sf[i] = round(sf[i], 2)
            hf[i] = round(hf[i], 2)

        # for k in range(len(hf)):
        #     if hf[k] > self.mdrn:
        #         line_w

        # Расчет климатических нагрузок
        cg = [10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0]  # Толщина стенки гололеда
        vd = [400.0, 500.0, 650.0, 800.0, 1000.0, 1250.0, 1500.0]  # Ветровое давление
        wGolnorm = (0.9e-3) * 9.8 * self.ki * self.kd * math.pi * (cg[self.gol - 1] * (
                    self.diam + self.ki * self.kd * cg[self.gol - 1]))  # нормативная гололедная нагрузка на 1 м кабеля
        wGolol = wGolnorm * self.kf * 0.5  # расчетная голоедная нагрузка на 1 м кабеля
        wGol = wCab + wGolol  # Вес кабеля, покрытого гололедом
        av = [0.76, 0.71, 0.7, 0.7, 0.7, 0.7, 0.7]  # Коэффициент неравномерности ветрового давления
        avg = [1.0, 1.0, 1.0, 1.0, 0.9, 0.84, 0.72]
        skl = [0, 0, 0, 0]
        hkl = [0, 0, 0, 0]
        kl = 0.0

        if lenth <= 50.0:  # Коэф. влияния длины пролета на ветровую нагрузку
            kl = 1.2
        if 50.0 < lenth <= 100.0:
            kl = 1.1
        if 100.0 < lenth <= 150.0:
            kl = 1.05
        elif lenth > 150.0:
            kl = 1.0

        angkoef = math.sin((angle * math.pi) / 180) * math.sin((angle * math.pi) / 180)

        # ветровое давление при гололеде
        vg = vd[self.vet - 1] * 0.25
        if vg < 200.0:
            vg = 200.0

        # норм. ветр. нагр. при гололеде пролет
        wwgp = avg[self.vet - 1] * kl * self.kw * 1.2 * vg * (self.diam + 2 * cg[self.gol - 1]) * 1e-3 * angkoef * lenth

        # //расч. ветр. нагр. при гололеде
        wvgr = wwgp * 1.1

        wvg = wvgr / lenth  # Ветровая нагрузка при гололеде 1 m

        wmax = math.sqrt(wGol ** 2 + wvg ** 2)  # Суммарная нагрузка гололед и ветер

        if self.diam >= 20:  # Коэффициент лобового сопротивления в зависимости от диаметра кабеля
            cx = 1.1
        else:
            cx = 1.2

        wvnp = av[self.vet - 1] * kl * self.kw * cx * vd[
            self.vet - 1] * self.diam * 1e-3 * angkoef * lenth  # норм. ветр. нагрузка на кабель без гололеда
        wvr = wvnp * 1.1  # расч. ветр. нагрузка на кабель без гололеда
        wv = wvr / lenth  # расч. ветр. нагрузка на 1 m кабель без гололеда
        wvet = math.sqrt(wCab ** 2 + wv ** 2)  # Суммарная нагрузка, ветер без гололеда
        wkl = [wCab, wGol, wmax, wvet]
        tkl = [10.0, -5.0, -5.0, -5.0]
        aa = [0.0, 0.0, 0.0, 0.0]
        bb = [0.0, 0.0, 0.0, 0.0]
        disa = [0.0, 0.0, 0.0, 0.0]
        lnka = [0.0, 0.0, 0.0, 0.0]

        for k in range(len(wkl)):
            # Длина кабеля с учетом температуры
            lnka[k] = lenNon * (1 + self.tklr * (tkl[k] - self.temp))
            aa[k] = 3 * (lenth ** 2 - lenth * lnka[k]) / 8
            bb[k] = (-3 * wkl[k] * (lenth ** 3) * lnka[k]) / (64 * self.modul * 1000 * self.sech)
            disa[k] = ((aa[k] / 3) ** 3) + ((-bb[k] / 2) ** 2)
            if disa[k] >= 0:
                xa = (-bb[k] / 2) + (math.sqrt(disa[k]))
                ya = (-bb[k] / 2) - (math.sqrt(disa[k]))
                if xa >= 0:
                    xacub = xa ** (1.0 / 3)
                else:
                    xacub = (-1) * ((math.fabs(xa)) ** (1.0 / 3))
                if ya >= 0:
                    yacub = ya ** (1.0 / 3)
                else:
                    yacub = (-1) * ((math.fabs(ya)) ** (1.0 / 3))
                skl[k] = xacub + yacub
            else:
                skl[k] = 2 * (math.sqrt(-aa[k] / 3)) * (
                    math.cos((1.0 / 3) * (math.acos((-bb[k] / 2) / ((-aa[k] / 3) ** (3.0 / 2.0))))))
            hkl[k] = ((wkl[k] * (lenth ** 2)) / (8 * skl[k])) / 1000
            if hkl[k] > self.mdrn:
                line_warning = True

            skl[k] = round(skl[k], 2)
            hkl[k] = round(hkl[k], 2)


        lineResult = LineResultData(self.vet,
                                    self.gol,
                                    vd[self.vet - 1],
                                    cg[self.gol - 1],
                                    self.land_str(),
                                    #self.land,
                                    lenth,
                                    strela,
                                    "cable_name",
                                    self.massa,
                                    self.diam,
                                    self.sech,
                                    self.modul,
                                    str(round(self.tklr * 1000000, 2)),
                                    #self.tklr,
                                    skl[0],
                                    hkl[0],
                                    skl[1],
                                    hkl[1],
                                    skl[3],
                                    hkl[3],
                                    skl[2],
                                    hkl[2],
                                    sf[0],
                                    sf[1],
                                    sf[2],
                                    sf[3],
                                    sf[4],
                                    sf[5],
                                    sf[6],
                                    sf[7],
                                    sf[8],
                                    sf[9],
                                    sf[10],
                                    hf[0],
                                    hf[1],
                                    hf[2],
                                    hf[3],
                                    hf[4],
                                    hf[5],
                                    hf[6],
                                    hf[7],
                                    hf[8],
                                    hf[9],
                                    hf[10],
                                    round(wCab, 2),
                                    round(hnul, 2),
                                    round(lenCab, 2),
                                    round(lenNon, 2),
                                    self.temp,
                                    round(lnka[0], 2),
                                    round(aa[0], 2),
                                    round(bb[0], 2),
                                    round(disa[0], 2),
                                    round(lnka[1], 2),
                                    round(wGolnorm, 2),
                                    self.ki,
                                    self.kd,
                                    self.kf,
                                    round(wGolol, 2),
                                    round(wGol, 2),
                                    round(aa[1], 2),
                                    round(bb[1], 2),
                                    round(disa[1], 2),
                                    av[self.vet - 1],
                                    kl,
                                    self.kw,
                                    cx,
                                    round(wvnp, 2),
                                    round(wvr, 2),
                                    round(wv, 2),
                                    round(wvet, 2),
                                    round(aa[3], 2),
                                    round(bb[3], 2),
                                    round(disa[3], 2),
                                    avg[self.vet - 1],
                                    round(wwgp, 2),
                                    round(wvgr, 2),
                                    round(wvg, 2),
                                    round(wmax, 2),
                                    round(aa[2], 2),
                                    round(bb[2], 2),
                                    round(disa[2], 2),
                                    vg,
                                    line_warning)

        return lineResult

    def pillarCalc(self, lenLeft, strLeft, lenRight, strRight, angle):

        self.koef()

        # сбор нагрузок
        wCab = (self.massa * 9.8) / 1000  # Вес 1 м кабеля
        cg = [10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0]  # Толщина стенки гололеда
        vd = [400.0, 500.0, 650.0, 800.0, 1000.0, 1250.0, 1500.0]  # Ветровое давление
        # нормативная гололедная нагрузка на 1 м кабеля
        wGolnorm = 0.0009 * 9.8 * self.ki * self.kd * math.pi * cg[self.gol - 1] * (
                self.diam + self.ki * self.kd * cg[self.gol - 1])
        wGolol_1 = wGolnorm * self.kf * 1  # расчетная гололедная нагрузка на 1 м кабеля 1ГПС
        wGolol_2 = wGolnorm * self.kf * 0.5  # расчетная гололедная нагрузка на 1 м кабеля 2ГПС

        wTGol = wCab + wGolnorm  # нормативная нагрузка на 1 м кабеля (вес кабеля + вес гололеда)

        wGol_1 = wCab + wGolol_1  # расчетная нагрузка на 1 м кабеля (вес кабеля + вес гололеда) 1ГПС
        wGol_2 = wCab + wGolol_2  # расчетная нагрузка на 1 м кабеля (вес кабеля + вес гололеда) 2ГПС

        av = [0.76, 0.71, 0.7, 0.7, 0.7, 0.7, 0.7]  # Коэффициент неравномерности ветрового давления
        avg = [1.0, 1.0, 1.0, 1.0, 0.9, 0.84, 0.72]  # Коэффициент неравномерности ветрового давления при гололеде

        # Коэф. влияния длины пролета на ветровую нагрузку
        if lenLeft <= 50.0:  # левый пролет
            klLeft = 1.2
        if 50.0 < lenLeft <= 100.0:
            klLeft = 1.1
        if 100.0 < lenLeft <= 150.0:
            klLeft = 1.05
        elif lenLeft > 150.0:
            klLeft = 1.0

        if lenRight <= 50.0:  # правый пролет
            klRight = 1.2
        if 50.0 < lenRight <= 100.0:
            klRight = 1.1
        if 100.0 < lenRight <= 150.0:
            klRight = 1.05
        elif lenRight > 150.0:
            klRight = 1.0

        # коэффициент влияния угла направления ветра
        angkoef = math.sin((angle * math.pi) / 180) * math.sin((angle * math.pi) / 180)
        # нормативная ветровая нагрузка при гололеде левый пролет
        wgn_L = avg[self.vet - 1] * klLeft * self.kw * 1.2 * (vd[self.vet - 1] * 0.25) * (
                self.diam + 2 * cg[self.gol - 1]) * 0.001 * lenLeft * angkoef
        # нормативная ветровая нагрузка при гололеде правый пролет
        wgn_r = avg[self.vet - 1] * klRight * self.kw * 1.2 * (vd[self.vet - 1] * 0.25) * (
                self.diam + 2 * cg[self.gol - 1]) * 0.001 * lenRight * angkoef

        wG1_L = wgn_L * 1.3  # расчетная ветровая нагрузка при гололеде левый пролет 1ГПС
        wG2_L = wgn_L * 1.1  # расчетная ветровая нагрузка при гололеде левый пролет 2ГПС
        wG1_R = wgn_r * 1.3  # расчетная ветровая нагрузка при гололеде правый пролет 1ГПС
        wG2_R = wgn_r * 1.1  # расчетная ветровая нагрузка при гололеде правый пролет 2ГПС

        # нормативная нагрузка кабель + ветер + гололед на 1 м левый пролет
        wmax_1 = math.sqrt((wCab + wGolnorm) ** 2 + (wgn_L / lenLeft) ** 2)
        # нормативная нагрузка кабель + ветер + гололед на 1 м правый пролет
        wmaxR_1 = math.sqrt((wCab + wGolnorm) ** 2 + (wgn_r / lenRight) ** 2)

        if self.diam >= 20:  # Коэффициент лобового сопротивления в зависимости от диаметра кабеля
            cx = 1.1
        else:
            cx = 1.2

        # Нормативная ветровая нагрузка левый пролет
        wlnormL = av[self.vet - 1] * klLeft * self.kw * cx * vd[self.vet - 1] * self.diam * 0.001 * lenLeft * angkoef
        # Нормативная ветровая нагрузка правый пролет
        wlnormR = av[self.vet - 1] * klRight * self.kw * cx * vd[self.vet - 1] * self.diam * 0.001 * lenRight * angkoef

        wL_1 = wlnormL * 1.3  # расчетная ветровая нагрузка левый пролет 1ГПС
        wR_1 = wlnormR * 1.3  # расчетная ветровая нагрузка правый пролет 1ГПС
        wL_2 = wlnormL * 1.1  # расчетная ветровая нагрузка левый пролет 2ГПС
        wR_2 = wlnormR * 1.1  # расчетная ветровая нагрузка правый пролет 2ГПС

        # нормативная нагрузка кабель + ветер на 1 м правый пролет
        wvetR_1 = math.sqrt(wCab ** 2 + (wlnormR / lenRight) ** 2)
        # нормативная нагрузка кабель + ветер на 1 м левый пролет
        wvet_1 = math.sqrt(wCab ** 2 + (wlnormL / lenLeft) ** 2)

        # вес кабеля левый пролет
        wCabLeft = round((wCab * lenLeft), 2)

        # вес кабеля правый пролет
        wCabRight = round((wCab * lenRight), 2)

        # уравнение состояния провода ветер + гололед, левый пролет
        line_max1_left = self.wireCalc(lenLeft, strLeft, -5.0, self.temp, self.modul, self.tklr, self.sech, wCab,
                                       wmax_1)

        # уравнение состояния провода ветер + гололед, правый пролет
        line_max1_right = self.wireCalc(lenRight, strRight, -5.0, self.temp, self.modul, self.tklr, self.sech, wCab,
                                        wmaxR_1)

        # уравнение состояния провода ветер, левый пролет
        line_vet1_left = self.wireCalc(lenLeft, strLeft, -5.0, self.temp, self.modul, self.tklr, self.sech, wCab,
                                       wvet_1)

        # уравнение состояния провода ветер, правый пролет
        line_vet1_right = self.wireCalc(lenRight, strRight, -5.0, self.temp, self.modul, self.tklr, self.sech, wCab,
                                        wvetR_1)

        # уравнение состояния провода гололед, левый пролет
        line_gol1_left = self.wireCalc(lenLeft, strLeft, -5.0, self.temp, self.modul, self.tklr, self.sech, wCab, wTGol)

        # уравнение состояния провода гололед, правый пролет
        line_gol1_right = self.wireCalc(lenRight, strRight, -5.0, self.temp, self.modul, self.tklr, self.sech, wCab,
                                        wTGol)

        # сохранение результатов в экземпляр датакласса

        pillresult = PillResultData(round(wCab, 2),
                                    round(wGolnorm, 2),
                                    round(wGolol_1, 2),
                                    round(wGolol_2, 2),
                                    round(wTGol, 2),
                                    round(wGol_1, 2),
                                    round(wGol_2, 2),
                                    klLeft,
                                    klRight,
                                    angkoef,
                                    round(wgn_L, 2),
                                    round(wgn_r, 2),
                                    round(wG1_L, 2),
                                    round(wG2_L, 2),
                                    round(wG1_R, 2),
                                    round(wG2_R, 2),
                                    round(wmax_1, 2),
                                    round(wmaxR_1, 2),
                                    cx,
                                    round(wlnormL, 2),
                                    round(wlnormR, 2),
                                    round(wL_1, 2),
                                    round(wR_1, 2),
                                    round(wL_2, 2),
                                    round(wR_2, 2),
                                    round(wvetR_1, 2),
                                    round(wvet_1, 2),
                                    round(wCabLeft, 2),
                                    round(wCabRight, 2),
                                    line_max1_left,
                                    line_max1_right,
                                    line_vet1_left,
                                    line_vet1_right,
                                    line_gol1_left,
                                    line_gol1_right,
                                    self.ki,
                                    self.kd,
                                    cg[self.gol - 1],
                                    self.kf,
                                    av[self.vet - 1],
                                    self.kw,
                                    vd[self.vet - 1],
                                    avg[self.vet - 1],
                                    round((line_max1_left[1] * 1.3), 2),  # t1_2L
                                    round((line_max1_right[1] * 1.3), 2),  # t1_2R
                                    round((line_vet1_left[1] * 1.3), 2),  # t1_1L
                                    round((line_vet1_right[1] * 1.3), 2),  # t1_1R
                                    round((line_gol1_left[1] * 1.3), 2),  # t1_3L
                                    round((line_gol1_right[1] * 1.3), 2),  # t1_3R
                                    round((line_gol1_right[1] * 1.3), 2),  # t1_4R
                                    round(((wCab * lenLeft + wCab * lenRight) / 2), 2),  # g1_1
                                    round(((wGol_1 * lenLeft + wGol_1 * lenRight) / 2), 2),  # g1_2
                                    round(((wCab * lenLeft + wCab * lenRight) / 2), 2),  # g2_1
                                    round(((wGol_2 * lenLeft + wGol_2 * lenRight) / 2), 2),  # g2_2
                                    round(((wL_1 + wR_1) / 2), 2),  # p1_1
                                    round(((wL_2 + wR_2) / 2), 2),  # p2_1
                                    round(((wG1_L + wG1_R) / 2), 2),  # p1_2
                                    round(((wG2_L + wG2_R) / 2), 2),  # p2_2
                                    round(((wGol_1 * lenRight) / 2), 2),  # g1_4
                                    self.diam,
                                    lenLeft,
                                    lenRight,
                                    strLeft,
                                    strRight,
                                    self.massa,
                                    self.sech,
                                    self.modul,
                                    self.tklr,
                                    self.temp,
                                    self.vet,
                                    self.gol,
                                    self.land
                                    )

        return pillresult

    def wireCalc(self, lenth, strela, temp_fact, temp_nach, modul, tklr, scab, wCab, wnagr):
        # Начальная нагрузка
        hnul = ((wCab * (lenth ** 2)) / (8 * strela)) / 1000

        # Фактическая длина кабеля
        lcab = lenth + ((8 * (strela ** 2)) / (3 * lenth))

        # Длина кабеля в ненагруженном состоянии
        ln = lcab / (1 + (hnul / (modul * scab)))

        # длина кабеля в ненагруженном состоянии с учетом температуры
        lnk = ln * (1 + tklr * (temp_fact - temp_nach))

        # коэффициенты уравнения состояния провода
        aa = 3 * (lenth ** 2 - lenth * lnk) / 8
        bb = (-3 * wnagr * (lenth ** 3) * lnk) / (64 * modul * 1000 * scab)

        # дискриминант
        disa = ((aa / 3) ** 3) + ((-bb / 2) ** 2)
        if disa >= 0:
            xa = (-bb / 2) + (math.sqrt(disa))
            ya = (-bb / 2) - (math.sqrt(disa))
            if xa >= 0:
                xacub = xa ** (1.0 / 3)
            else:
                xacub = (-1) * ((math.fabs(xa)) ** (1.0 / 3))
            if ya >= 0:
                yacub = ya ** (1.0 / 3)
            else:
                yacub = (-1) * ((math.fabs(ya)) ** (1.0 / 3))
            str_Calc = xacub + yacub  # расчетная стрела провеса
        else:
            str_Calc = 2 * (math.sqrt(-aa / 3)) * (
                math.cos((1.0 / 3) * (math.acos((-bb / 2) / ((-aa / 3) ** (3.0 / 2.0))))))  # расчетная стрела провеса
        h_Calc = ((wnagr * (lenth ** 2)) / (8 * str_Calc))  # расчетное тяжение

        str_Res = round(str_Calc, 2)
        h_Res = round(h_Calc, 2)
        a_Res = round(aa, 3)
        b_Res = round(bb, 3)
        d_Res = round(disa, 3)
        hnul_Res = round(hnul, 3)
        lenFact_Res = round(lcab, 3)
        lenStart_Res = round(ln, 3)
        lenTemp_Res = round(lnk, 3)

        return str_Res, h_Res, a_Res, b_Res, d_Res, hnul_Res, lenFact_Res, lenStart_Res, lenTemp_Res
