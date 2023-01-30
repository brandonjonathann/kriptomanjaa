def extended_vigenere_encrypt(plaintext, kunci_extended):
    result = []
    for i in range(len(plaintext)):
        x = ord(plaintext[i]) 
        y = ord(kunci_extended[i]) 
        result.append(chr((x + y) % 256))
    return(result)

def extended_vigenere_decrypt(ciphertext, kunci_extended):
    result = []
    for i in range(len(ciphertext)):
        x = ord(ciphertext[i]) 
        y = ord(kunci_extended[i])
        result.append(chr((x - y) % 256))
    return(result)