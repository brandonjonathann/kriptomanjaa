from vigenere import *
from extended_vigenere import *
from playfair import *

def check_alphabet(text):
    checked = []
    for i in range(len(text)):
        for j in range(26):
            if (text[i] == chr(j + 65)):
                checked.append(text[i])
    return(checked)

def create_kunci(plaintext, kunci):
    kunci_asli = []
    for i in range(len(plaintext)):
        kunci_asli.append(kunci[i % len(kunci)])
    return(kunci_asli)

cipher = input("Pilih cipher: ")
kunci_awal = input("Masukkan kunci: ")
plaintext_awal = input("Masukkan plaintext: ")

kunci_tmp = [x for x in kunci_awal]
kunci = check_alphabet(kunci_tmp)

plaintext_tmp = [x for x in plaintext_awal]
plaintext = check_alphabet(plaintext_tmp)

if (cipher == "VIGENERE"):
    kunci = create_kunci(plaintext, kunci)
    print(vigenere_encrypt(plaintext, kunci))
    print(vigenere_decrypt(vigenere_encrypt(plaintext, kunci), kunci))
elif (cipher == "EXTENDED VIGENERE"):
    kunci = create_kunci(plaintext_tmp, kunci_tmp)
    print(extended_vigenere_encrypt(plaintext_tmp, kunci))
    print(extended_vigenere_decrypt(extended_vigenere_encrypt(plaintext_tmp, kunci), kunci))
elif (cipher == "PLAYFAIR"):
    kunci = create_kunci_playfair(kunci)
    plaintext = create_plaintext_playfair(plaintext)
    print(playfair_encrypt(plaintext, kunci))
    print(playfair_decrypt(playfair_encrypt(plaintext, kunci), kunci))