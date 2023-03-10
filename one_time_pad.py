def one_time_pad_encrypt(plaintext, kunci):
    result = []
    for i in range(len(plaintext)):
        result.append(chr(((int(ord(plaintext[i])) - 65) + (int(ord(kunci[i])) - 65)) % 26 + 65))
    return(''.join(result))

def one_time_pad_decrypt(ciphertext, kunci):
    result = []
    for i in range(len(ciphertext)):
        result.append(chr(((int(ord(ciphertext[i])) - 65) - (int(ord(kunci[i])) - 65)) % 26 + 65))
    return(''.join(result))