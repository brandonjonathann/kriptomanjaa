def check_alphabet(text):
    checked = []
    for i in range(len(text)):
        for j in range(26):
            if (text[i] == chr(j + 65)):
                checked.append(text[i])
            elif (text[i] == chr(j + 97)):
                checked.append(chr(j + 65))
    return(checked)

def create_kunci(plaintext, kunci):
    kunci_asli = []
    for i in range(len(plaintext)):
        kunci_asli.append(kunci[i % len(kunci)])
    return(kunci_asli)

