from vigenere import *
from extended_vigenere import *
from playfair import *
from one_time_pad import *

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
plaintext_awal = input("Masukkan plaintext: ")
plaintext_tmp = [x for x in plaintext_awal]
plaintext = check_alphabet(plaintext_tmp)

if (cipher == "ONE TIME PAD"):
    kunci = generate_kunci(plaintext)
    print(one_time_pad_encrypt(plaintext, kunci))
    print(one_time_pad_decrypt(one_time_pad_encrypt(plaintext, kunci), kunci))

else: 
    kunci_awal = input("Masukkan kunci: ")
    kunci_tmp = [x for x in kunci_awal]
    kunci = check_alphabet(kunci_tmp)

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