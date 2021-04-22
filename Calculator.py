import math

from PillarResult import PillarResult
from LineResult import LineResult

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

        # self.Ki   #Ki - коэффициент изменения ощины стенки гололеда по высоте (2.5.4. ПУЭ)
        # self.Kw   #Kw - коэффициент изменения ветрового давления по высоте в зависимости от типа местности и высоты (табл. 2.5.2 ПУЭ)
        # self.Kd   #Kd - коэффициент зменения толщины стенки гололеда в зависимости от диаметра провода
        # self.Kf   #Kf - коэффициент надежности по гололедной нагрузке (1.3 - 1 и 2 район, 1.6 - 3 и выше

    def koef(self):
        if self.height <= 15.0:  # 15
            self.Ki = 1.0
            hI = [1.0, 0.65, 0.4]
        if 15.01 <= self.height <= 30.0:  # 20
            self.Ki = 1.0
            hI = [1.25, 0.85, 0.55]
        if 30.01 <= self.height <= 50.0:  # 40
            self.Ki = 1.4
            hI = [1.5, 1.1, 0.8]
        if 50.01 <= self.height <= 70.0:  # 60
            self.Ki = 1.6
            hI = [1.7, 1.3, 1.0]
        if 70.01 <= self.height <= 90.0:  # 80
            self.Ki = 1.8
            hI = [1.85, 1.45, 1.15]
        if 90.01 <= self.height <= 125.0:  # 100
            self.Ki = 2.0
            hI = [2.0, 1.6, 1.25]
        if 125.01 <= self.height <= 175.0:  # 150
            self.Ki = 2.0
            hI = [2.25, 1.9, 1.55]
        if 175.01 <= self.height <= 225.0:  # 200
            self.Ki = 2.0
            hI = [2.45, 2.1, 1.8]
        if 225.01 <= self.height <= 275.0:  # 250
            self.Ki = 2.0
            hI = [2.65, 2.3, 2.0]
        if 275.01 <= self.height <= 350.0:  # 300
            self.Ki = 2.0
            hI = [2.75, 2.5, 2.2]
        if self.height > 350.01:  # 350+
            self.Ki = 2.0
            hI = [2.75, 2.75, 2.35]

        self.Kw = hI[self.land]

        if self.diam <= 15.0:
            self.Kd = 1.0
        if 15.0 < self.diam <= 25.0:
            self.Kd = 0.9
        if 25.0 < self.diam <= 35.0:
            self.Kd = 0.8
        if 35.0 < self.diam <= 55.0:
            self.Kd = 0.7
        if self.diam > 55.0:
            self.Kd = 0.6

        if self.gol <= 2:
            self.Kf = 1.3
        if self.gol > 2:
            self.Kf = 1.6

    def lineCalc(self, lenth, strela, angle):

        # коэффициенты
        self.koef()

        line_warning = False

        # Вес кабеля, площадь сечения
        wCab = (self.massa * 9.8) / 1000

        # Начальная нагрузка
        hNul = ((wCab * (lenth ** 2)) / (8 * strela)) / 1000

        # Фактическая длина кабеля
        lenCab = lenth + ((8 * (strela ** 2)) / (3 * lenth))

        # Длина кабеля в ненагруженном состоянии
        lenNon = lenCab / (1 + (hNul / (self.modul * self.sech)))

        # Расчет монтажной таблицы
        Tf = [-30, -20, -10, 0.0, 10, 20, 30, 40, 50, 60, 70]
        Sf = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        Hf = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for i in range(len(Tf)):
            # Длина кабеля с учетом температуры
            Lnk = lenNon * (1 + self.tklr * (Tf[i] - self.temp))
            # Члены уравнения
            a = 3 * (lenth ** 2 - lenth * Lnk) / 8
            b = (-3 * wCab * (lenth ** 3) * Lnk) / (64 * self.modul * 1000 * self.sech)
            dis = ((a / 3) ** 3) + ((-b / 2) ** 2)
            if dis >= 0:
                X = (-b / 2) + (math.sqrt(dis))
                Y = (-b / 2) - (math.sqrt(dis))
                if X >= 0:
                    Xcub = X ** (1.0 / 3)
                else:
                    Xcub = (-1) * ((math.fabs(X)) ** (1.0 / 3))
                if Y >= 0:
                    Ycub = Y ** (1.0 / 3)
                else:
                    Ycub = (-1) * ((math.fabs(Y)) ** (1.0 / 3))
                Sf[i] = Xcub + Ycub
            else:
                Sf[i] = 2 * (math.sqrt(-a / 3)) * (math.cos((1.0 / 3) * (math.acos((-b / 2) / ((-a / 3) ** (3.0 / 2.0))))))
            Hf[i] = ((wCab * (lenth ** 2)) / (8 * Sf[i])) / 1000
            if Hf[i] > self.mdrn:
                line_warning = True

            Sf[i] = round(Sf[i], 2)
            Hf[i] = round(Hf[i], 2)

        # for k in range(len(Hf)):
        #     if Hf[k] > self.mdrn:
        #         line_w

        # Расчет климатических нагрузок
        cg = [10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0]  # Толщина стенки гололеда
        vd = [400.0, 500.0, 650.0, 800.0, 1000.0, 1250.0, 1500.0]  # Ветровое давление
        WgolNorm = (0.9e-3) * 9.8 * self.Ki * self.Kd * math.pi * (cg[self.gol - 1] * (self.diam + self.Ki * self.Kd * cg[self.gol - 1]))  #  нормативная гололедная нагрузка на 1 м кабеля
        Wgolol = WgolNorm * self.Kf * 0.5  # расчетная голоедная нагрузка на 1 м кабеля
        Wgol = wCab + Wgolol   # Вес кабеля, покрытого гололедом
        av = [0.76, 0.71, 0.7, 0.7, 0.7, 0.7, 0.7]  # Коэффициент неравномерности ветрового давления
        avg = [1.0, 1.0, 1.0, 1.0, 0.9, 0.84, 0.72]
        Skl = [0, 0, 0, 0]
        Hkl = [0, 0, 0, 0]
        Kl = 0.0

        if lenth <= 50.0:  # Коэф. влияния длины пролета на ветровую нагрузку
            Kl = 1.2
        if 50.0 < lenth <= 100.0:
            Kl = 1.1
        if 100.0 < lenth <= 150.0:
            Kl = 1.05
        elif lenth > 150.0:
            Kl = 1.0

        angkoef = math.sin((angle * math.pi) / 180) * math.sin((angle * math.pi) / 180)

        # ветровое давление при гололеде
        vg = vd[self.vet - 1] * 0.25
        if vg < 200.0:
            vg = 200.0

        # норм. ветр. нагр. при гололеде пролет
        Wvgp = avg[self.vet - 1] * Kl * self.Kw * 1.2 * vg * (self.diam + 2 * cg[self.gol - 1]) * 1e-3 * angkoef * lenth

        # //расч. ветр. нагр. при гололеде
        Wvgr = Wvgp * 1.1

        Wvg = Wvgr / lenth   # Ветровая нагрузка при гололеде 1 m

        Wmax = math.sqrt(Wgol ** 2 + Wvg ** 2)  # Суммарная нагрузка гололед и ветер

        if self.diam >= 20:  # Коэффициент лобового сопротивления в зависимости от диаметра кабеля
            Cx = 1.1
        else:
            Cx = 1.2

        Wvnp = av[self.vet - 1] * Kl * self.Kw * Cx * vd[self.vet - 1] * self.diam * 1e-3 * angkoef * lenth  # норм. ветр. нагрузка на кабель без гололеда
        Wvr = Wvnp * 1.1  # расч. ветр. нагрузка на кабель без гололеда
        Wv = Wvr / lenth  # расч. ветр. нагрузка на 1 m кабель без гололеда
        Wvet = math.sqrt(wCab ** 2 + Wv ** 2)  # Суммарная нагрузка, ветер без гололеда
        Wkl = [wCab, Wgol, Wmax, Wvet]
        Tkl = [10.0, -5.0, -5.0, -5.0]
        aa = [0.0, 0.0, 0.0, 0.0]
        bb = [0.0, 0.0, 0.0, 0.0]
        disa = [0.0, 0.0, 0.0, 0.0]
        lnka = [0.0, 0.0, 0.0, 0.0]

        for k in range(len(Wkl)):
            # Длина кабеля с учетом температуры
            lnka[k] = lenNon * (1 + self.tklr * (Tkl[k] - self.temp))
            aa[k] = 3 * (lenth ** 2 - lenth * lnka[k]) / 8
            bb[k] = (-3 * Wkl[k] * (lenth ** 3) * lnka[k]) / (64 * self.modul * 1000 * self.sech)
            disa[k] = ((aa[k] / 3) ** 3) + ((-bb[k] / 2) ** 2)
            if disa[k] >= 0:
                Xa = (-bb[k] / 2) + (math.sqrt(disa[k]))
                Ya = (-bb[k] / 2) - (math.sqrt(disa[k]))
                if Xa >= 0:
                    Xacub = Xa ** (1.0 / 3)
                else:
                    Xacub = (-1) * ((math.fabs(Xa)) ** (1.0 / 3))
                if Ya >= 0:
                    Yacub = Ya ** (1.0 / 3)
                else:
                    Yacub = (-1) * ((math.fabs(Ya)) ** (1.0 / 3))
                Skl[k] = Xacub + Yacub
            else:
                Skl[k] = 2 * (math.sqrt(-aa[k] / 3)) * (
                    math.cos((1.0 / 3) * (math.acos((-bb[k] / 2) / ((-aa[k] / 3) ** (3.0 / 2.0))))))
            Hkl[k] = ((Wkl[k] * (lenth ** 2)) / (8 * Skl[k])) / 1000
            if Hkl[k] > self.mdrn:
                line_warning = True

            Skl[k] = round(Skl[k], 2)
            Hkl[k] = round(Hkl[k], 2)

        lineResult = LineResult(self.vet,
                                self.gol,
                                vd[self.vet - 1],
                                cg[self.gol - 1],
                                self.land,
                                lenth,
                                strela,
                                "cable_name",
                                self.massa,
                                self.diam,
                                self.sech,
                                self.modul,
                                self.tklr,
                                Skl[0],
                                Hkl[0],
                                Skl[1],
                                Hkl[1],
                                Skl[3],
                                Hkl[3],
                                Skl[2],
                                Hkl[2],
                                Sf[0],
                                Sf[1],
                                Sf[2],
                                Sf[3],
                                Sf[4],
                                Sf[5],
                                Sf[6],
                                Sf[7],
                                Sf[8],
                                Sf[9],
                                Sf[10],
                                Hf[0],
                                Hf[1],
                                Hf[2],
                                Hf[3],
                                Hf[4],
                                Hf[5],
                                Hf[6],
                                Hf[7],
                                Hf[8],
                                Hf[9],
                                Hf[10],
                                round(wCab, 2),
                                round(hNul, 2),
                                round(lenCab, 2),
                                round(lenNon, 2),
                                self.temp,
                                round(lnka[0], 2),
                                round(aa[0], 2),
                                round(bb[0], 2),
                                round(disa[0], 2),
                                round(lnka[1], 2),
                                round(WgolNorm, 2),
                                self.Ki,
                                self.Kd,
                                self.Kf,
                                round(Wgolol, 2),
                                round(Wgol, 2),
                                round(aa[1], 2),
                                round(bb[1], 2),
                                round(disa[1], 2),
                                av[self.vet - 1],
                                Kl,
                                self.Kw,
                                Cx,
                                round(Wvnp, 2),
                                round(Wvr, 2),
                                round(Wv, 2),
                                round(Wvet, 2),
                                round(aa[3], 2),
                                round(bb[3], 2),
                                round(disa[3], 2),
                                avg[self.vet - 1],
                                round(Wvgp, 2),
                                round(Wvgr, 2),
                                round(Wvg, 2),
                                round(Wmax, 2),
                                round(aa[2], 2),
                                round(bb[2], 2),
                                round(disa[2], 2),
                                vg,
                                line_warning)

        return lineResult

        # return Hf, Sf, Hkl, Skl

    def pillarCalc(self, lenLeft, strLeft, lenRight, strRight, angle):

        self.koef()

        # сбор нагрузок
        Wcab = (self.massa * 9.8) / 1000  # Вес 1 м кабеля
        cg = [10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0]  # Толщина стенки гололеда
        vd = [400.0, 500.0, 650.0, 800.0, 1000.0, 1250.0, 1500.0]  # Ветровое давление
        # нормативная гололедная нагрузка на 1 м кабеля
        WgolNorm = 0.0009 * 9.8 * self.Ki * self.Kd * math.pi * cg[self.gol - 1] * (
                self.diam + self.Ki * self.Kd * cg[self.gol - 1])
        Wgolol_1 = WgolNorm * self.Kf * 1  # расчетная гололедная нагрузка на 1 м кабеля 1ГПС
        Wgolol_2 = WgolNorm * self.Kf * 0.5  # расчетная гололедная нагрузка на 1 м кабеля 2ГПС

        WTGol = Wcab + WgolNorm  # нормативная нагрузка на 1 м кабеля (вес кабеля + вес гололеда)

        Wgol_1 = Wcab + Wgolol_1  # расчетная нагрузка на 1 м кабеля (вес кабеля + вес гололеда) 1ГПС
        Wgol_2 = Wcab + Wgolol_2  # расчетная нагрузка на 1 м кабеля (вес кабеля + вес гололеда) 2ГПС

        av = [0.76, 0.71, 0.7, 0.7, 0.7, 0.7, 0.7]  # Коэффициент неравномерности ветрового давления
        avg = [1.0, 1.0, 1.0, 1.0, 0.9, 0.84, 0.72]  # Коэффициент неравномерности ветрового давления при гололеде

        # Коэф. влияния длины пролета на ветровую нагрузку
        if lenLeft <= 50.0:  # левый пролет
            KlLeft = 1.2
        if 50.0 < lenLeft <= 100.0:
            KlLeft = 1.1
        if 100.0 < lenLeft <= 150.0:
            KlLeft = 1.05
        elif lenLeft > 150.0:
            KlLeft = 1.0

        if lenRight <= 50.0:  # правый пролет
            KlRight = 1.2
        if 50.0 < lenRight <= 100.0:
            KlRight = 1.1
        if 100.01 < lenRight <= 150.0:
            KlRight = 1.05
        elif lenRight > 150.01:
            KlRight = 1.0

        # коэффициент влияния угла направления ветра
        angkoef = math.sin((angle * math.pi) / 180) * math.sin((angle * math.pi) / 180)
        # нормативная ветровая нагрузка при гололеде левый пролет
        WGN_L = avg[self.vet - 1] * KlLeft * self.Kw * 1.2 * (vd[self.vet - 1] * 0.25) * (
                self.diam + 2 * cg[self.gol - 1]) * 0.001 * lenLeft * angkoef
        # нормативная ветровая нагрузка при гололеде правый пролет
        WGN_R = avg[self.vet - 1] * KlRight * self.Kw * 1.2 * (vd[self.vet - 1] * 0.25) * (
                self.diam + 2 * cg[self.gol - 1]) * 0.001 * lenRight * angkoef

        WG1_L = WGN_L * 1.3  # расчетная ветровая нагрузка при гололеде левый пролет 1ГПС
        WG2_L = WGN_L * 1.1  # расчетная ветровая нагрузка при гололеде левый пролет 2ГПС
        WG1_R = WGN_R * 1.3  # расчетная ветровая нагрузка при гололеде правый пролет 1ГПС
        WG2_R = WGN_R * 1.1  # расчетная ветровая нагрузка при гололеде правый пролет 2ГПС

        # нормативная нагрузка кабель + ветер + гололед на 1 м левый пролет
        Wmax_1 = math.sqrt((Wcab + WgolNorm) ** 2 + (WGN_L / lenLeft) ** 2)
        # нормативная нагрузка кабель + ветер + гололед на 1 м правый пролет
        WmaxR_1 = math.sqrt((Wcab + WgolNorm) ** 2 + (WGN_R / lenRight) ** 2)

        if self.diam >= 20:  # Коэффициент лобового сопротивления в зависимости от диаметра кабеля
            Cx = 1.1
        else:
            Cx = 1.2

        # Нормативная ветровая нагрузка левый пролет
        WLNormL = av[self.vet - 1] * KlLeft * self.Kw * Cx * vd[self.vet - 1] * self.diam * 0.001 * lenLeft * angkoef
        # Нормативная ветровая нагрузка правый пролет
        WLNormR = av[self.vet - 1] * KlRight * self.Kw * Cx * vd[self.vet - 1] * self.diam * 0.001 * lenRight * angkoef

        WL_1 = WLNormL * 1.3  # расчетная ветровая нагрузка левый пролет 1ГПС
        WR_1 = WLNormR * 1.3  # расчетная ветровая нагрузка правый пролет 1ГПС
        WL_2 = WLNormL * 1.1  # расчетная ветровая нагрузка левый пролет 2ГПС
        WR_2 = WLNormR * 1.1  # расчетная ветровая нагрузка правый пролет 2ГПС

        # нормативная нагрузка кабель + ветер на 1 м правый пролет
        WvetR_1 = math.sqrt(Wcab ** 2 + (WLNormR / lenRight) ** 2)
        # нормативная нагрузка кабель + ветер на 1 м левый пролет
        Wvet_1 = math.sqrt(Wcab ** 2 + (WLNormL / lenLeft) ** 2)

        # вес кабеля левый пролет
        WcabLeft = round((Wcab * lenLeft), 2)

        # вес кабеля правый пролет
        WcabRight = round((Wcab * lenRight), 2)

        # уравнение состояния провода ветер + гололед, левый пролет
        line_max1_left = self.wireCalc(lenLeft, strLeft, -5.0, self.temp, self.modul, self.tklr, self.sech, Wcab,
                                       Wmax_1)

        # уравнение состояния провода ветер + гололед, правый пролет
        line_max1_right = self.wireCalc(lenRight, strRight, -5.0, self.temp, self.modul, self.tklr, self.sech, Wcab,
                                        WmaxR_1)

        # уравнение состояния провода ветер, левый пролет
        line_vet1_left = self.wireCalc(lenLeft, strLeft, -5.0, self.temp, self.modul, self.tklr, self.sech, Wcab,
                                       Wvet_1)

        # уравнение состояния провода ветер, правый пролет
        line_vet1_right = self.wireCalc(lenRight, strRight, -5.0, self.temp, self.modul, self.tklr, self.sech, Wcab,
                                        WvetR_1)

        # уравнение состояния провода гололед, левый пролет
        line_gol1_left = self.wireCalc(lenLeft, strLeft, -5.0, self.temp, self.modul, self.tklr, self.sech, Wcab, WTGol)

        # уравнение состояния провода гололед, правый пролет
        line_gol1_right = self.wireCalc(lenRight, strRight, -5.0, self.temp, self.modul, self.tklr, self.sech, Wcab,
                                        WTGol)

        # сохранение результатов в экземпляр класса

        pillresult = PillarResult(round(Wcab, 2),
                                  round(WgolNorm, 2),
                                  round(Wgolol_1, 2),
                                  round(Wgolol_2, 2),
                                  round(WTGol, 2),
                                  round(Wgol_1, 2),
                                  round(Wgol_2, 2),
                                  KlLeft,
                                  KlRight,
                                  angkoef,
                                  round(WGN_L, 2),
                                  round(WGN_R, 2),
                                  round(WG1_L, 2),
                                  round(WG2_L, 2),
                                  round(WG1_R, 2),
                                  round(WG2_R, 2),
                                  round(Wmax_1, 2),
                                  round(WmaxR_1, 2),
                                  Cx,
                                  round(WLNormL, 2),
                                  round(WLNormR, 2),
                                  round(WL_1, 2),
                                  round(WR_1, 2),
                                  round(WL_2, 2),
                                  round(WR_2, 2),
                                  round(WvetR_1, 2),
                                  round(Wvet_1, 2),
                                  round(WcabLeft, 2),
                                  round(WcabRight, 2),
                                  line_max1_left,
                                  line_max1_right,
                                  line_vet1_left,
                                  line_vet1_right,
                                  line_gol1_left,
                                  line_gol1_right,
                                  self.Ki,
                                  self.Kd,
                                  cg[self.gol - 1],
                                  self.Kf,
                                  av[self.vet - 1],
                                  self.Kw,
                                  vd[self.vet - 1],
                                  avg[self.vet - 1],
                                  round((line_max1_left[1] * 1.3), 2),  # t1_2L
                                  round((line_max1_right[1] * 1.3), 2),  # t1_2R
                                  round((line_vet1_left[1] * 1.3), 2),  # t1_1L
                                  round((line_vet1_right[1] * 1.3), 2),  # t1_1R
                                  round((line_gol1_left[1] * 1.3), 2),  # t1_3L
                                  round((line_gol1_right[1] * 1.3), 2),  # t1_3R
                                  round((line_gol1_right[1] * 1.3), 2),  # t1_4R
                                  round(((Wcab * lenLeft + Wcab * lenRight) / 2), 2),  # g1_1
                                  round(((Wgol_1 * lenLeft + Wgol_1 * lenRight) / 2), 2),  # g1_2
                                  round(((Wcab * lenLeft + Wcab * lenRight) / 2), 2),  # g2_1
                                  round(((Wgol_2 * lenLeft + Wgol_2 * lenRight) / 2), 2),  # g2_2
                                  round(((WL_1 + WR_1) / 2), 2),  # p1_1
                                  round(((WL_2 + WR_2) / 2), 2),  # p2_1
                                  round(((WG1_L + WG1_R) / 2), 2),  # p1_2
                                  round(((WG2_L + WG2_R) / 2), 2),  # p2_2
                                  round(((Wgol_1 * lenRight) / 2), 2),  # g1_4
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

    def wireCalc(self, lenth, strela, temp_fact, temp_nach, modul, tklr, scab, Wcab, Wnagr):
        # Начальная нагрузка
        Hnul = ((Wcab * (lenth ** 2)) / (8 * strela)) / 1000

        # Фактическая длина кабеля
        Lcab = lenth + ((8 * (strela ** 2)) / (3 * lenth))

        # Длина кабеля в ненагруженном состоянии
        Ln = Lcab / (1 + (Hnul / (modul * scab)))

        # длина кабеля в ненагруженном состоянии с учетом температуры
        Lnk = Ln * (1 + tklr * (temp_fact - temp_nach))

        # коэффициенты уравнения состояния провода
        aa = 3 * (lenth ** 2 - lenth * Lnk) / 8
        bb = (-3 * Wnagr * (lenth ** 3) * Lnk) / (64 * modul * 1000 * scab)

        # дискриминант
        disa = ((aa / 3) ** 3) + ((-bb / 2) ** 2)
        if disa >= 0:
            Xa = (-bb / 2) + (math.sqrt(disa))
            Ya = (-bb / 2) - (math.sqrt(disa))
            if Xa >= 0:
                Xacub = Xa ** (1.0 / 3)
            else:
                Xacub = (-1) * ((math.fabs(Xa)) ** (1.0 / 3))
            if Ya >= 0:
                Yacub = Ya ** (1.0 / 3)
            else:
                Yacub = (-1) * ((math.fabs(Ya)) ** (1.0 / 3))
            Str_Calc = Xacub + Yacub  # расчетная стрела провеса
        else:
            Str_Calc = 2 * (math.sqrt(-aa / 3)) * (
                math.cos((1.0 / 3) * (math.acos((-bb / 2) / ((-aa / 3) ** (3.0 / 2.0))))))  # расчетная стрела провеса
        H_Calc = ((Wnagr * (lenth ** 2)) / (8 * Str_Calc))  # расчетное тяжение

        Str_Res = round(Str_Calc, 2)
        H_Res = round(H_Calc, 2)
        a_Res = round(aa, 3)
        b_Res = round(bb, 3)
        D_Res = round(disa, 3)
        Hnul_Res = round(Hnul, 3)
        LenFact_Res = round(Lcab, 3)
        LenStart_Res = round(Ln, 3)
        LenTemp_Res = round(Lnk, 3)

        return Str_Res, H_Res, a_Res, b_Res, D_Res, Hnul_Res, LenFact_Res, LenStart_Res, LenTemp_Res
