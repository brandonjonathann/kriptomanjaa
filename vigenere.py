def vigenere_encrypt(plaintext, kunci_asli):
    result = []
    for i in range(len(plaintext)):
        x = ord(plaintext[i]) - 65
        y = ord(kunci_asli[i]) - 65
        result.append(chr((x + y) % 26 + 65))
    return(''.join(result))

def vigenere_decrypt(ciphertext, kunci_asli):
    result = []
    for i in range(len(ciphertext)):
        x = ord(ciphertext[i]) - 65
        y = ord(kunci_asli[i]) - 65
        result.append(chr((x - y) % 26 + 65))
    return(''.join(result))