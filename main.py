import sys
from tkinter import Widget
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap

from vigenere import *
from extended_vigenere import *
from playfair import *
from one_time_pad import *
from check import *

import sqlite3
import os
import csv
import datetime
import random

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        loadUi("main.ui", self)
        self.label.setText("Welcome To Cipher Program!!!")
        self.pushButton_2.clicked.connect(self.Vigenere)
        self.pushButton_3.clicked.connect(self.ExtendVigenere)
        self.pushButton_4.clicked.connect(self.OneTimePad)
        self.pushButton_5.clicked.connect(self.Playfair)
        self.pushButton_6.clicked.connect(self.Enigma)

    def Vigenere(self):
        vigenere = Vigenere()
        widget.addWidget(vigenere)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def ExtendVigenere(self):
        extendVigenere = ExtendVigenere()
        widget.addWidget(extendVigenere)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def OneTimePad(self):
        oneTimePad = OneTimePad()
        widget.addWidget(oneTimePad)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Playfair(self):
        playfair = Playfair()
        widget.addWidget(playfair)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Enigma(self):
        enigma = Enigma()
        widget.addWidget(enigma)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Vigenere(QMainWindow):
    def __init__(self):
        super(Vigenere, self).__init__()
        loadUi("cipher.ui", self)

        self.label_2.setText("Vigenere Cipher")
        self.pushButton_10.clicked.connect(self.Menu)
        self.pushButton_6.clicked.connect(self.Encrypt)
        self.pushButton_7.clicked.connect(self.Decrypt)
        self.pushButton_11.clicked.connect(self.AddFile)
        self.pushButton_8.clicked.connect(self.Default)
        self.pushButton_9.clicked.connect(self.Grouped)
        self.pushButton_12.clicked.connect(self.Save)

    def Menu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Encrypt(self):
        plaintext_awal = self.textEdit.toPlainText()
        plaintext_tmp = [x for x in plaintext_awal]
        plaintext = check_alphabet(plaintext_tmp)
        key_awal = self.textEdit_2.toPlainText()
        key_tmp = [x for x in key_awal]
        key = check_alphabet(key_tmp)
        keyFinal = create_kunci(plaintext, key)
        result = vigenere_encrypt(plaintext, keyFinal)
        self.textBrowser.setText(result)

    def Decrypt(self):
        ciphertext_awal = self.textEdit.toPlainText()
        ciphertext_tmp = [x for x in ciphertext_awal]
        ciphertext = check_alphabet(ciphertext_tmp)
        key_awal = self.textEdit_2.toPlainText()
        key_tmp = [x for x in key_awal]
        key = check_alphabet(key_tmp)
        keyFinal = create_kunci(ciphertext, key)
        result = vigenere_decrypt(ciphertext, keyFinal)
        self.textBrowser.setText(result)
    
    def AddFile(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File", "E:\Kripto\kriptomanjaa", "All Files (*)")
        with open(fname[0], 'r') as file :
            lines = file.read().rstrip()
        self.textEdit.setPlainText(str(lines))

    def Default(self):
        output = []
        text_awal = self.textBrowser.toPlainText()
        text_tmp = [x for x in text_awal]
        for i in range(len(text_tmp)):
            if (text_tmp[i] != ' '):
                output.append(text_tmp[i])
        self.textBrowser.setText(''.join(output))


    def Grouped(self):
        output_tmp = []
        output = []
        text_awal = self.textBrowser.toPlainText()
        text_tmp = [x for x in text_awal]
        for i in range(len(text_tmp)):
            if (text_tmp[i] != ' '):
                output_tmp.append(text_tmp[i])
        for i in range(len(output_tmp)):
            if i % 5 == 0 and i > 0:
                output.append(' ')
            output.append(output_tmp[i])
        self.textBrowser.setText(''.join(output))

    def Save(self):
        name = QFileDialog.getSaveFileName(self, "Save File")
        file = open(name[0], 'w')
        text = self.textBrowser.toPlainText()
        file.write(text)
        file.close()


class ExtendVigenere(QMainWindow):
    def __init__(self):
        super(ExtendVigenere, self).__init__()
        loadUi("cipher.ui", self)

        self.label_2.setText("Extend Vigenere Cipher")
        self.pushButton_10.clicked.connect(self.Menu)
        self.pushButton_6.clicked.connect(self.Encrypt)
        self.pushButton_7.clicked.connect(self.Decrypt)
        self.pushButton_11.clicked.connect(self.AddFile)
        self.pushButton_8.clicked.connect(self.Default)
        self.pushButton_9.clicked.connect(self.Grouped)
        self.pushButton_12.clicked.connect(self.Save)

    def Menu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Encrypt(self):
        plaintext_awal = self.textEdit.toPlainText()
        plaintext_tmp = [x for x in plaintext_awal]
        key_awal = self.textEdit_2.toPlainText()
        key_tmp = [x for x in key_awal]
        keyFinal = create_kunci(plaintext_tmp, key_tmp)
        result = extended_vigenere_encrypt(plaintext_tmp, keyFinal)
        self.textBrowser.setText(result)

    def Decrypt(self):
        ciphertext_awal = self.textEdit.toPlainText()
        ciphertext_tmp = [x for x in ciphertext_awal]
        key_awal = self.textEdit_2.toPlainText()
        key_tmp = [x for x in key_awal]
        keyFinal = create_kunci(ciphertext_tmp, key_tmp)
        result = extended_vigenere_decrypt(ciphertext_tmp, keyFinal)
        self.textBrowser.setText(result)
    
    def AddFile(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File", "E:\Kripto\kriptomanjaa", "All Files (*)")
        with open(fname[0], 'r') as file :
            lines = file.read().rstrip()
        self.textEdit.setPlainText(str(lines))

    def Default(self):
        output = []
        text_awal = self.textBrowser.toPlainText()
        text_tmp = [x for x in text_awal]
        for i in range(len(text_tmp)):
            if (text_tmp[i] != ' '):
                output.append(text_tmp[i])
        self.textBrowser.setText(''.join(output))


    def Grouped(self):
        output_tmp = []
        output = []
        text_awal = self.textBrowser.toPlainText()
        text_tmp = [x for x in text_awal]
        for i in range(len(text_tmp)):
            if (text_tmp[i] != ' '):
                output_tmp.append(text_tmp[i])
        for i in range(len(output_tmp)):
            if i % 5 == 0 and i > 0:
                output.append(' ')
            output.append(output_tmp[i])
        self.textBrowser.setText(''.join(output))

    def Save(self):
        name = QFileDialog.getSaveFileName(self, "Save File")
        file = open(name[0], 'w')
        text = self.textBrowser.toPlainText()
        file.write(text)
        file.close()

class Playfair(QMainWindow):
    def __init__(self):
        super(Playfair, self).__init__()
        loadUi("cipher.ui", self)

        self.label_2.setText("Playfair Cipher")
        self.pushButton_10.clicked.connect(self.Menu)
        self.pushButton_6.clicked.connect(self.Encrypt)
        self.pushButton_7.clicked.connect(self.Decrypt)
        self.pushButton_11.clicked.connect(self.AddFile)
        self.pushButton_8.clicked.connect(self.Default)
        self.pushButton_9.clicked.connect(self.Grouped)
        self.pushButton_12.clicked.connect(self.Save)

    def Menu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Encrypt(self):
        plaintext_awal = self.textEdit.toPlainText()
        plaintext_tmp = [x for x in plaintext_awal]
        plaintext = check_alphabet(plaintext_tmp)
        key_awal = self.textEdit_2.toPlainText()
        key_tmp = [x for x in key_awal]
        key = check_alphabet(key_tmp)
        keyFinal = create_kunci_playfair(key)
        plaintextFinal = create_plaintext_playfair(plaintext)
        result = playfair_encrypt(plaintextFinal, keyFinal)
        self.textBrowser.setText(result)

    def Decrypt(self):
        ciphertext_awal = self.textEdit.toPlainText()
        ciphertext_tmp = [x for x in ciphertext_awal]
        ciphertext = check_alphabet(ciphertext_tmp)
        key_awal = self.textEdit_2.toPlainText()
        key_tmp = [x for x in key_awal]
        key = check_alphabet(key_tmp)
        keyFinal = create_kunci_playfair(key)
        ciphertextFinal = create_plaintext_playfair(ciphertext)
        result = playfair_decrypt(ciphertext, keyFinal)
        self.textBrowser.setText(result)
    
    def AddFile(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File", "E:\Kripto\kriptomanjaa", "All Files (*)")
        with open(fname[0], 'r') as file :
            lines = file.read().rstrip()
        self.textEdit.setPlainText(str(lines))

    def Default(self):
        output = []
        text_awal = self.textBrowser.toPlainText()
        text_tmp = [x for x in text_awal]
        for i in range(len(text_tmp)):
            if (text_tmp[i] != ' '):
                output.append(text_tmp[i])
        self.textBrowser.setText(''.join(output))

    def Grouped(self):
        output_tmp = []
        output = []
        text_awal = self.textBrowser.toPlainText()
        text_tmp = [x for x in text_awal]
        for i in range(len(text_tmp)):
            if (text_tmp[i] != ' '):
                output_tmp.append(text_tmp[i])
        for i in range(len(output_tmp)):
            if i % 5 == 0 and i > 0:
                output.append(' ')
            output.append(output_tmp[i])
        self.textBrowser.setText(''.join(output))
    
    def Save(self):
        name = QFileDialog.getSaveFileName(self, "Save File")
        file = open(name[0], 'w')
        text = self.textBrowser.toPlainText()
        file.write(text)
        file.close()

class OneTimePad(QMainWindow):
    def __init__(self):
        super(OneTimePad, self).__init__()
        loadUi("cipher.ui", self)

        self.label_2.setText("One Time Pad Cipher")
        self.pushButton_10.clicked.connect(self.Menu)
        self.pushButton_6.clicked.connect(self.Encrypt)
        self.pushButton_7.clicked.connect(self.Decrypt)
        self.pushButton_11.clicked.connect(self.AddFile)
        self.pushButton_8.clicked.connect(self.Default)
        self.pushButton_9.clicked.connect(self.Grouped)
        self.pushButton_12.clicked.connect(self.Save)
        self.pushButton_13.clicked.connect(self.RandKey)

    def Menu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Encrypt(self):
        plaintext_awal = self.textEdit.toPlainText()
        plaintext_tmp = [x for x in plaintext_awal]
        plaintext = check_alphabet(plaintext_tmp)
        key_awal = self.textEdit_2.toPlainText()
        key_tmp = [x for x in key_awal]
        key = check_alphabet(key_tmp)
        keyFinal = create_kunci(plaintext, key)
        result = one_time_pad_encrypt(plaintext, keyFinal)
        self.textBrowser.setText(result)

    def Decrypt(self):
        ciphertext_awal = self.textEdit.toPlainText()
        ciphertext_tmp = [x for x in ciphertext_awal]
        ciphertext = check_alphabet(ciphertext_tmp)
        key_awal = self.textEdit_2.toPlainText()
        key_tmp = [x for x in key_awal]
        key = check_alphabet(key_tmp)
        keyFinal = create_kunci(ciphertext, key)
        result = one_time_pad_decrypt(ciphertext, keyFinal)
        self.textBrowser.setText(result)
    
    def AddFile(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File", "E:\Kripto\kriptomanjaa", "All Files (*)")
        with open(fname[0], 'r') as file :
            lines = file.read().rstrip()
        self.textEdit.setPlainText(str(lines))

    def Default(self):
        output = []
        text_awal = self.textBrowser.toPlainText()
        text_tmp = [x for x in text_awal]
        for i in range(len(text_tmp)):
            if (text_tmp[i] != ' '):
                output.append(text_tmp[i])
        self.textBrowser.setText(''.join(output))

    def Grouped(self):
        output_tmp = []
        output = []
        text_awal = self.textBrowser.toPlainText()
        text_tmp = [x for x in text_awal]
        for i in range(len(text_tmp)):
            if (text_tmp[i] != ' '):
                output_tmp.append(text_tmp[i])
        for i in range(len(output_tmp)):
            if i % 5 == 0 and i > 0:
                output.append(' ')
            output.append(output_tmp[i])
        self.textBrowser.setText(''.join(output))
    
    def Save(self):
        name = QFileDialog.getSaveFileName(self, "Save File")
        file = open(name[0], 'w')
        text = self.textBrowser.toPlainText()
        file.write(text)
        file.close()

    def RandKey(self):
        fname = QFileDialog.getOpenFileName(self, "Choose File", "E:\Kripto\kriptomanjaa", "All Files (*)")
        with open(fname[0], 'r') as file :
            lines = file.read().rstrip()
        tmp = [x for x in lines]
        tmp2 = []
        randomnumber = random.randint(0, 19999)
        plaintextlen = len([x for x in self.textEdit.toPlainText()])
        for i in range(plaintextlen):
            tmp2.append(tmp[(randomnumber + i) % 20000])
        str1 = ""
        tmp3 = str1.join(tmp2)
        self.textEdit_2.setPlainText(str(tmp3))

class Enigma(QMainWindow):
    def __init__(self):
        super(Enigma, self).__init__()
        loadUi("cipher.ui", self)

        self.label_2.setText("Enigma Cipher")
        self.pushButton_10.clicked.connect(self.Menu)
        self.pushButton_6.clicked.connect(self.Encrypt)
        self.pushButton_7.clicked.connect(self.Decrypt)
        self.pushButton_11.clicked.connect(self.AddFile)
        self.pushButton_8.clicked.connect(self.Default)
        self.pushButton_9.clicked.connect(self.Grouped)

    def Menu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Encrypt(self):
        print("")

    def Decrypt(self):
        print("")
    
    def AddFile(self):
        print("")

    def Default(self):
        print("")

    def Grouped(self):
        print("")

# main
app = QApplication(sys.argv)
welcome = Menu()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exit Program")