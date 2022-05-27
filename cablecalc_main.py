#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 19:33:19 2018

@author: freexrunner
"""

import sys

from cabui import *
from Calculator import *
from PyQt5.QtWidgets import QFileDialog
from dataclasses import asdict

class CableCalcMain(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.rg = QtWidgets.QButtonGroup()
        self.rg.addButton(self.ui.radioButton_A, 0)
        self.rg.addButton(self.ui.radioButton_B, 1)
        self.rg.addButton(self.ui.radioButton_C, 2)  # self.rg.checkedId()
        land = self.rg.checkedId()

        if land == 0:
            self.land_r = "A - открытые пространства"
        if land == 1:
            self.land_r = "B - с препятствиями ниже опор"
        if land == 2:
            self.land_r = "С - с препятствиями выше опор"

        self.ui.sechCalcBtn.clicked.connect(self.onSech)
        self.ui.btnLine.clicked.connect(self.lineStart)
        self.ui.btnSupp.clicked.connect(self.pillarStart)
        self.ui.btnFileSupp.clicked.connect(self.pillFile)
        self.ui.btnFileLine_2.clicked.connect(self.lineFile)

        self.fPillStart = False
        self.fLineStart = False


    def main_empty(self):
        massa_txt = self.ui.massaEdit.text().replace(',', '.')
        diam_txt = self.ui.diamEdit.text().replace(',', '.')
        sech_txt = self.ui.sechEdit.text().replace(',', '.')
        modul_txt = self.ui.modulEdit.text().replace(',', '.')
        tklr_txt = self.ui.tklrEdit.text().replace(',', '.')
        mdrn_txt = self.ui.mdrnEdit.text().replace(',', '.')
        temp_txt = self.ui.tempEdit.text().replace(',', '.')
        height_txt = self.ui.heightEdit.text().replace(',', '.')

        if (len(massa_txt) == 0 or len(diam_txt) == 0 or len(sech_txt) == 0 or len(modul_txt) == 0 or len(tklr_txt) == 0
                or len(mdrn_txt) == 0 or len(temp_txt) == 0 or len(height_txt) == 0):
            msg_mainEmpty = QtWidgets.QMessageBox()
            msg_mainEmpty.setWindowTitle('Ошибка ввода данных!')
            msg_mainEmpty.setText('Укажате все исходные данные')
            msg_mainEmpty.setIcon(msg_mainEmpty.Warning)
            msg_mainEmpty.exec()
            mStart = False

        else:
            self.massa = float(massa_txt)
            self.diam = float(diam_txt)
            self.sech = float(sech_txt)
            self.tklr = 1e-6 * float(tklr_txt)
            self.mdrn = float(mdrn_txt)
            self.temp = float(temp_txt)
            self.height = float(height_txt)
            self.modul = float(modul_txt)
            mStart = True

        return mStart

    def onSech(self):
        diam_txt = self.ui.diamEdit.text().replace(',', '.')
        if (len(diam_txt) == 0):
            msg_diam = QtWidgets.QMessageBox()
            msg_diam.setWindowTitle('Ошибка ввода данных!')
            msg_diam.setText('Укажите диаметр')
            msg_diam.setIcon(msg_diam.Warning)
            msg_diam.exec()
        else:
            diam = float(diam_txt)
            sech_temp = math.pi * ((diam / 2) ** 2)
            sech_temp = round(sech_temp, 2)
            sech_temp = str(sech_temp)
            self.ui.sechEdit.setText(sech_temp)

    def line_empty(self):
        lenLine_txt = self.ui.lenEditLine.text().replace(',', '.')
        strLine_txt = self.ui.strEditLine.text().replace(',', '.')
        angleLine_txt = self.ui.anglEditLine.text().replace(',', '.')
        if (len(lenLine_txt) == 0 or len(strLine_txt) == 0 or len(angleLine_txt) == 0):
            msg_line = QtWidgets.QMessageBox()
            msg_line.setWindowTitle('Ошибка ввода данных!')
            msg_line.setText('Укажите длину пролета/стрелу провеса/угол направления ветра')
            msg_line.setIcon(msg_line.Warning)
            msg_line.exec()
            lStart = False
        else:
            self.lenLine = float(lenLine_txt)
            self.strLine = float(strLine_txt)
            self.angleLine = float(angleLine_txt)
            # self.lStart = 1
            lStart = True

        return lStart

    def pillar_empty(self):
        lenLeftSupp_txt = self.ui.lenLeftEditSupp.text().replace(',', '.')
        strLeftSupp_txt = self.ui.strLeftEditSupp.text().replace(',', '.')
        lenRightSupp_txt = self.ui.lenRightEditSupp.text().replace(',', '.')
        strRightSupp_txt = self.ui.strRightEditSupp.text().replace(',', '.')
        angleSupp_txt = self.ui.angEditSupp.text().replace(',', '.')
        if (len(lenLeftSupp_txt) == 0 or len(strLeftSupp_txt) == 0 or len(lenRightSupp_txt) == 0
                or len(strRightSupp_txt) == 0 or len(angleSupp_txt) == 0):
            msg_supp = QtWidgets.QMessageBox()
            msg_supp.setWindowTitle('Ошибка ввода данных!')
            msg_supp.setText('Укажите длины пролета/стрелы провеса/угол направления ветра')
            msg_supp.setIcon(msg_supp.Warning)
            msg_supp.exec()
            pStart = False
        else:
            self.lenLeftpillar = float(lenLeftSupp_txt)
            self.strLeftpillar = float(strLeftSupp_txt)
            self.lenRightpillar = float(lenRightSupp_txt)
            self.strRightpillar = float(strRightSupp_txt)
            self.anglepillar = float(angleSupp_txt)
            pStart = True

        return pStart

    def lineStart(self):
        if self.main_empty() and self.line_empty():
            try:
                # pass
                calc = Calculator(self.massa,
                                  self.diam,
                                  self.sech,
                                  self.modul,
                                  self.tklr,
                                  self.mdrn,
                                  self.temp,
                                  self.height,
                                  self.rg.checkedId(), #land - тип местности
                                  int(self.ui.spinVet.text()), #vet - район по ветру
                                  int(self.ui.spinGol.text())) #gol - район по гололеду
                self.lineResult = calc.lineCalc(self.lenLine, self.strLine, self.angleLine)

                if self.lineResult.line_warning:
                    msg_supp = QtWidgets.QMessageBox()
                    msg_supp.setWindowTitle('Превышена максимально - допустимая нагрузка')
                    msg_supp.setText('Для данного пролета требуется кабель с большей максимально - допустимой нагрузкой')
                    msg_supp.setIcon(msg_supp.Warning)
                    msg_supp.exec()

                # self.updateLineUI(Hf, Hkl, Sf, Skl)
                self.updateLineUI()

            except:
                msg_ls = QtWidgets.QMessageBox()
                msg_ls.setWindowTitle('Некорректные данные для расчета!')
                msg_ls.setText('Проверьте корректность исходных данных')
                msg_ls.setIcon(msg_ls.Warning)
                msg_ls.exec()

    def updateLineUI(self):
        self.ui.strNorm.setText(str(self.lineResult.str_norm))
        self.ui.nagrNorm.setText(str(self.lineResult.nagr_norm))
        self.ui.strGol.setText(str(self.lineResult.str_gol))
        self.ui.nagrGol.setText(str(self.lineResult.nagr_gol))
        self.ui.strVet.setText(str(self.lineResult.str_vet))
        self.ui.nagrVet.setText(str(self.lineResult.nagr_vet))
        self.ui.strVetGol.setText(str(self.lineResult.strvetgol))
        self.ui.nagrVetGol.setText(str(self.lineResult.nagrvetgol))
        self.ui.strmin30.setText(str(self.lineResult.str_min_30))
        self.ui.nagrmin30.setText(str(self.lineResult.nagr_min_30))
        self.ui.strmin20.setText(str(self.lineResult.str_min_20))
        self.ui.nagrmin20.setText(str(self.lineResult.nagr_min_20))
        self.ui.strmin10.setText(str(self.lineResult.str_min_10))
        self.ui.nagrmin10.setText(str(self.lineResult.nagr_min_10))
        self.ui.str0.setText(str(self.lineResult.str_0))
        self.ui.nagr0.setText(str(self.lineResult.nagr_0))
        self.ui.str10.setText(str(self.lineResult.str_10))
        self.ui.nagr10.setText(str(self.lineResult.nagr_10))
        self.ui.str20.setText(str(self.lineResult.str_20))
        self.ui.nagr20.setText(str(self.lineResult.nagr_20))
        self.ui.str30.setText(str(self.lineResult.str_30))
        self.ui.nagr30.setText(str(self.lineResult.nagr_30))
        self.ui.str40.setText(str(self.lineResult.str_40))
        self.ui.nagr40.setText(str(self.lineResult.nagr_40))
        self.ui.str50.setText(str(self.lineResult.str_50))
        self.ui.nagr50.setText(str(self.lineResult.nagr_50))
        self.ui.str60.setText(str(self.lineResult.str_60))
        self.ui.nagr60.setText(str(self.lineResult.nagr_60))
        self.ui.str70.setText(str(self.lineResult.str_70))
        self.ui.nagr70.setText(str(self.lineResult.nagr_70))

        self.fLineStart = True


    def pillarStart(self):
        if self.main_empty() and self.pillar_empty():
            try:
                # pass
                calc = Calculator(self.massa,
                                  self.diam,
                                  self.sech,
                                  self.modul,
                                  self.tklr,
                                  self.mdrn,
                                  self.temp,
                                  self.height,
                                  self.rg.checkedId(),  # land - тип местности
                                  int(self.ui.spinVet.text()),  # vet - район по ветру
                                  int(self.ui.spinGol.text()))  # gol - район по гололеду

                # результат в экземпляре класса
                self.pillResult = calc.pillarCalc(self.lenLeftpillar, self.strLeftpillar, self.lenRightpillar,
                                                  self.strRightpillar, self.anglepillar)
                self.updatePillarUI()

            except:
                msg_ls = QtWidgets.QMessageBox()
                msg_ls.setWindowTitle('Некорректные данные для расчета!')
                msg_ls.setText('Проверьте корректность исходных данных')
                msg_ls.setIcon(msg_ls.Warning)


    def updatePillarUI(self):

        # self.ui.T1_2_left.setText(str(self.pillResult.t1_2L))
        # self.ui.T1_2_right.setText(str(self.pillResult.t1_2R))
        # self.ui.a2_left.setText(str(self.pillResult.a2_left))
        # self.ui.b2_left.setText(str(self.pillResult.b2_left))
        # self.ui.d2_left.setText(str(self.pillResult.d2_left))
        # self.ui.a2_right.setText(str(self.pillResult.a2_right))
        # self.ui.b2_right.setText(str(self.pillResult.b2_right))
        # self.ui.d2_right.setText(str(self.pillResult.d2_right))
        # self.ui.t2_left.setText(str(self.pillResult.t2_left))
        # self.ui.s2_left.setText(str(self.pillResult.s2_left))
        # self.ui.t2_right.setText(str(self.pillResult.t2_right))
        # self.ui.s2_right.setText(str(self.pillResult.s2_right))
        #
        # self.ui.startH_left.setText(str(self.pillResult.startH_left))
        # self.ui.startH_right.setText(str(self.pillResult.startH_right))
        # self.ui.fact_length_left.setText(str(self.pillResult.fact_length_left))
        # self.ui.fact_length_right.setText(str(self.pillResult.fact_length_right))
        # self.ui.start_length_left.setText(str(self.pillResult.start_length_left))
        # self.ui.start_length_right.setText(str(self.pillResult.start_length_right))
        # self.ui.temp_length_left.setText(str(self.pillResult.Tem_length_left))
        # self.ui.temp_length_right.setText(str(self.pillResult.Tem_length_right))
        #
        # self.ui.T1_1_left.setText(str(self.pillResult.t1_1L))
        # self.ui.T1_1_right.setText(str(self.pillResult.t1_1R))
        # self.ui.a1_left.setText(str(self.pillResult.a1_left))
        # self.ui.b1_left.setText(str(self.pillResult.b1_left))
        # self.ui.d1_left.setText(str(self.pillResult.d1_left))
        # self.ui.a1_right.setText(str(self.pillResult.a1_right))
        # self.ui.b1_right.setText(str(self.pillResult.b1_right))
        # self.ui.d1_right.setText(str(self.pillResult.d1_right))
        # self.ui.t1_left.setText(str(self.pillResult.t1_left))
        # self.ui.s1_left.setText(str(self.pillResult.s1_left))
        # self.ui.t1_right.setText(str(self.pillResult.t1_right))
        # self.ui.s1_right.setText(str(self.pillResult.s1_right))
        #
        # self.ui.T1_4_left.setText('Обрыв')
        # self.ui.P1_4.setText('0')
        #
        # self.ui.T1_3_left.setText(str(self.pillResult.t1_3L))
        # self.ui.T1_3_right.setText(str(self.pillResult.t1_3R))
        # self.ui.T1_4_right.setText(str(self.pillResult.t1_4R))
        # self.ui.a3_left.setText(str(self.pillResult.a3_left))
        # self.ui.b3_left.setText(str(self.pillResult.b3_left))
        # self.ui.d3_left.setText(str(self.pillResult.d3_left))
        # self.ui.a3_right.setText(str(self.pillResult.a3_right))
        # self.ui.b3_right.setText(str(self.pillResult.b3_right))
        # self.ui.d3_right.setText(str(self.pillResult.d3_right))
        #
        # self.ui.t3_left.setText(str(self.pillResult.t3_left))
        # self.ui.s3_left.setText(str(self.pillResult.s3_left))
        # self.ui.t3_right.setText(str(self.pillResult.t3_right))
        # self.ui.s3_right.setText(str(self.pillResult.s3_right))
        #
        # self.ui.T2_1_left.setText(str(self.pillResult.t1_left))
        # self.ui.T2_1_right.setText(str(self.pillResult.t1_right))
        #
        # self.ui.T2_2_left.setText(str(self.pillResult.t2_left))
        # self.ui.T2_2_right.setText(str(self.pillResult.t2_right))
        #
        # self.ui.T2_3_left.setText(str(self.pillResult.t3_left))
        # self.ui.T2_3_right.setText(str(self.pillResult.t3_right))
######################################################################################################
        self.ui.T1_2_left.setText(str(self.pillResult.t1_2L))
        self.ui.T1_2_right.setText(str(self.pillResult.t1_2R))
        self.ui.a2_left.setText(str(self.pillResult.line_max1_left[2]))
        self.ui.b2_left.setText(str(self.pillResult.line_max1_left[3]))
        self.ui.d2_left.setText(str(self.pillResult.line_max1_left[4]))
        self.ui.a2_right.setText(str(self.pillResult.line_max1_right[2]))
        self.ui.b2_right.setText(str(self.pillResult.line_max1_right[3]))
        self.ui.d2_right.setText(str(self.pillResult.line_max1_right[4]))
        self.ui.t2_left.setText(str(self.pillResult.line_max1_left[1]))
        self.ui.s2_left.setText(str(self.pillResult.line_max1_left[0]))
        self.ui.t2_right.setText(str(self.pillResult.line_max1_right[1]))
        self.ui.s2_right.setText(str(self.pillResult.line_max1_right[0]))

        self.ui.startH_left.setText(str(self.pillResult.line_max1_left[5]))
        self.ui.startH_right.setText(str(self.pillResult.line_max1_right[5]))
        self.ui.fact_length_left.setText(str(self.pillResult.line_max1_left[6]))
        self.ui.fact_length_right.setText(str(self.pillResult.line_max1_right[6]))
        self.ui.start_length_left.setText(str(self.pillResult.line_max1_left[7]))
        self.ui.start_length_right.setText(str(self.pillResult.line_max1_right[7]))
        self.ui.temp_length_left.setText(str(self.pillResult.line_max1_left[8]))
        self.ui.temp_length_right.setText(str(self.pillResult.line_max1_right[8]))

        self.ui.T1_1_left.setText(str(self.pillResult.t1_1L))
        self.ui.T1_1_right.setText(str(self.pillResult.t1_1R))
        self.ui.a1_left.setText(str(self.pillResult.line_vet1_left[2]))
        self.ui.b1_left.setText(str(self.pillResult.line_vet1_left[3]))
        self.ui.d1_left.setText(str(self.pillResult.line_vet1_left[4]))
        self.ui.a1_right.setText(str(self.pillResult.line_vet1_right[2]))
        self.ui.b1_right.setText(str(self.pillResult.line_vet1_right[3]))
        self.ui.d1_right.setText(str(self.pillResult.line_vet1_right[4]))
        self.ui.t1_left.setText(str(self.pillResult.line_vet1_left[1]))
        self.ui.s1_left.setText(str(self.pillResult.line_vet1_left[0]))
        self.ui.t1_right.setText(str(self.pillResult.line_vet1_right[1]))
        self.ui.s1_right.setText(str(self.pillResult.line_vet1_right[0]))

        self.ui.T1_4_left.setText('Обрыв')
        self.ui.P1_4.setText('0')

        self.ui.T1_3_left.setText(str(self.pillResult.t1_3L))
        self.ui.T1_3_right.setText(str(self.pillResult.t1_3R))
        self.ui.T1_4_right.setText(str(self.pillResult.t1_4R))
        self.ui.a3_left.setText(str(self.pillResult.line_gol1_left[2]))
        self.ui.b3_left.setText(str(self.pillResult.line_gol1_left[3]))
        self.ui.d3_left.setText(str(self.pillResult.line_gol1_left[4]))
        self.ui.a3_right.setText(str(self.pillResult.line_gol1_right[2]))
        self.ui.b3_right.setText(str(self.pillResult.line_gol1_right[3]))
        self.ui.d3_right.setText(str(self.pillResult.line_gol1_right[4]))

        self.ui.t3_left.setText(str(self.pillResult.line_gol1_left[1]))
        self.ui.s3_left.setText(str(self.pillResult.line_gol1_left[0]))
        self.ui.t3_right.setText(str(self.pillResult.line_gol1_right[1]))
        self.ui.s3_right.setText(str(self.pillResult.line_gol1_right[0]))

        self.ui.T2_1_left.setText(str(self.pillResult.line_vet1_left[1]))
        self.ui.T2_1_right.setText(str(self.pillResult.line_vet1_right[1]))

        self.ui.T2_2_left.setText(str(self.pillResult.line_max1_left[1]))
        self.ui.T2_2_right.setText(str(self.pillResult.line_max1_right[1]))

        self.ui.T2_3_left.setText(str(self.pillResult.line_gol1_left[1]))
        self.ui.T2_3_right.setText(str(self.pillResult.line_gol1_right[1]))

####################################################################

        self.ui.G1_1.setText(str(self.pillResult.g1_1))
        self.ui.G1_2.setText(str(self.pillResult.g1_2))
        self.ui.G2_1.setText(str(self.pillResult.g2_1))
        self.ui.G2_2.setText(str(self.pillResult.g2_2))
        self.ui.P1_1.setText(str(self.pillResult.p1_1))
        self.ui.P2_1.setText(str(self.pillResult.p2_1))
        self.ui.P1_2.setText(str(self.pillResult.p1_2))
        self.ui.P2_2.setText(str(self.pillResult.p2_2))
        self.ui.G1_4.setText(str(self.pillResult.g1_4))
        self.ui.G1_3.setText(str(self.pillResult.g1_2))
        self.ui.P1_3.setText('0')
        self.ui.G2_3.setText(str(self.pillResult.g2_2))
        self.ui.P2_3.setText('0')

        wcabLeft = round((self.pillResult.wCab * self.lenLeftpillar), 2)
        wcabRight = round((self.pillResult.wCab * self.lenRightpillar), 2)

        self.ui.left_Self.setText(str(wcabLeft))
        self.ui.right_Self.setText(str(wcabRight))

        self.ui.gol_Norm.setText(str(self.pillResult.wGolNorm))
        self.ui.gol_1.setText(str(self.pillResult.wGolol_1))
        self.ui.gol_2.setText(str(self.pillResult.wGolol_2))
        self.ui.vet_left_Norm.setText(str(self.pillResult.wLNormL))
        self.ui.vet_right_Norm.setText(str(self.pillResult.wLNormR))
        self.ui.vet_left_1.setText(str(self.pillResult.wL_1))
        self.ui.vet_right_1.setText(str(self.pillResult.wR_1))
        self.ui.vet_left_2.setText(str(self.pillResult.wL_2))
        self.ui.vet_right_2.setText(str(self.pillResult.wR_2))
        self.ui.vetgol_left_Norm.setText(str(self.pillResult.wGN_L))
        self.ui.vetgol_right_Norm.setText(str(self.pillResult.wGN_R))
        self.ui.vetgol_left_1.setText(str(self.pillResult.wG1_L))
        self.ui.vetgol_right_1.setText(str(self.pillResult.wG1_R))
        self.ui.vetgol_left_2.setText(str(self.pillResult.wG2_L))
        self.ui.vetgol_right_2.setText(str(self.pillResult.wG2_R))
        self.ui.cabWeight.setText(str(self.pillResult.wCab))
        self.ui.nagrVet_left.setText(str(self.pillResult.wvet_1))
        self.ui.nagrVet_right.setText(str(self.pillResult.wvetR_1))
        self.ui.nagrVetGol_left.setText(str(self.pillResult.wmax_1))
        self.ui.nagrVetGol_right.setText(str(self.pillResult.wmaxR_1))

        self.fPillStart = True

    def pillFile(self):

        if not self.fPillStart:
            msg_file = QtWidgets.QMessageBox()
            msg_file.setWindowTitle('Ошибка записи!')
            msg_file.setText('Не выполнен расчет нагрузок')
            msg_file.setIcon(msg_file.Warning)
            msg_file.exec()

        else:
            try:
                inputfile = "pill_blank.txt"
                # inputfile = "pill_blank_format1.txt"
                # inputfile = "pill_blank_new.txt"
                outputfile = QFileDialog.getSaveFileName(self, 'Save file', 'Расчет нагрузок на опору', "TXT (*.txt)")[
                    0]

                # форматирование строк ключами и значениями из словаря

                # results = asdict(self.pillResult)
                #
                # key = list(results.keys())
                # values = list(results.values())
                #
                # with open(inputfile, 'r') as infile, open(outputfile, 'w') as outfile:
                #     for line in infile:
                #         for f in range(len(key)):
                #             if key[f] in line:
                #                 line = line.replace(key[f], str(values[f]))
                #         outfile.write(line)


                # форматирование строк значениями полей датакласса

                # values = self.pillResult
                #
                # with open(inputfile, 'r') as infile, open(outputfile, 'w') as outfile:
                #     for line in infile:
                #         linerepl = line.format(val = values)
                #         outfile.write(linerepl)



                # старый вариант
                keys = self.pillResult.getKeys()

                key = keys[0]
                key_r = keys[1]

                infile = open(inputfile, mode='r', encoding='utf-8')
                outfile = open(outputfile, mode='w', encoding='utf-8')

                for line in infile:
                    for f in range(len(key)):
                        if key[f] in line:
                            line = line.replace(key[f], key_r[f])
                    outfile.write(line)
                infile.close()
                outfile.close()
            except:
                msg_ls = QtWidgets.QMessageBox()
                msg_ls.setWindowTitle('Сохранение результатов расчета в файл')
                msg_ls.setText('Запись в файл не выполнена!')
                msg_ls.setIcon(msg_ls.Warning)

    def lineFile(self):

        if not self.fLineStart:
            msg_file = QtWidgets.QMessageBox()
            msg_file.setWindowTitle('Ошибка записи!')
            msg_file.setText('Не выполнен расчет нагрузок')
            msg_file.setIcon(msg_file.Warning)
            msg_file.exec()
        else:
            try:
                inputfile = "line_blank_new.txt"
                outputfile = QFileDialog.getSaveFileName(self, 'Save file', 'Расчет пролета', "TXT (*.txt)")[0]

                results = asdict(self.lineResult)

                key = list(results.keys())
                values = list(results.values())

                with open(inputfile, 'r') as infile, open(outputfile, 'w') as outfile:
                    for line in infile:
                        for f in range(len(key)):
                            if key[f] in line:
                                line = line.replace(key[f], str(values[f]))
                        outfile.write(line)

                # старый вариант
                # keys = self.lineResult.getKeys()
                #
                # key = keys[0]
                # key_r = keys[1]
                #
                # infile = open(inputfile, mode='r', encoding='utf-8')
                # outfile = open(outputfile, mode='w', encoding='utf-8')
                #
                # for line in infile:
                #     for f in range(len(key)):
                #         if key[f] in line:
                #             line = line.replace(key[f], key_r[f])
                #     outfile.write(line)
                # infile.close()
                # outfile.close()
            except:
                msg_ls = QtWidgets.QMessageBox()
                msg_ls.setWindowTitle('Сохранение результатов расчета в файл')
                msg_ls.setText('Запись в файл не выполнена!')
                msg_ls.setIcon(msg_ls.Warning)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = CableCalcMain()
    myapp.show()
    sys.exit(app.exec_())
