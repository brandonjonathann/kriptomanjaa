# CONTOH DARI PPT
# plaintext = "NANTIMALAMSAYATUNGGUKAMUDIDEPANWARUNGKOPI"
# kunci = "GTRSKNCVBRWPOATQLJFMXTRPJSRZOLFHTBMAEDPVY"
# ciphertext = "TTELSZCGBDOPMAMKYPLGHTDJMAUDDLSDTSGNKNDKG"

def one_time_pad_encrypt(plaintext, kunci):
    result = []
    for i in range(len(plaintext)):
        result.append(chr(((ord(plaintext[i]) - 65) + (ord(kunci[i]) - 65)) % 26 + 65))
    return(result)

def one_time_pad_decrypt(ciphertext, kunci):
    result = []
    for i in range(len(ciphertext)):
        result.append(chr(((ord(ciphertext[i]) - 65) - (ord(kunci[i]) - 65)) % 26 + 65))
    return(result)