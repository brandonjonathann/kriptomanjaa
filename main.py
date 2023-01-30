from vigenere import *
from extended_vigenere import *

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

kunci_awal = input("Masukkan kunci: ")
plaintext_awal = input("Masukkan plaintext: ")

kunci_tmp = [x for x in kunci_awal]
kunci = check_alphabet(kunci_tmp)

plaintext_tmp = [x for x in plaintext_awal]
plaintext = check_alphabet(plaintext_tmp)

kunci_asli = create_kunci(plaintext, kunci)
kunci_extended = create_kunci(plaintext_tmp, kunci_tmp)

# Vigenere Cipher
print(vigenere_encrypt(plaintext, kunci_asli))
print(vigenere_decrypt(vigenere_encrypt(plaintext, kunci_asli), kunci_asli))

# Extended Vigenere Cipher
print(extended_vigenere_encrypt(plaintext_tmp, kunci_extended))
print(extended_vigenere_decrypt(extended_vigenere_encrypt(plaintext_tmp, kunci_extended), kunci_extended))