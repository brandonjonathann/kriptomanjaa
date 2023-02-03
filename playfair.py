def create_kunci_playfair(kunci):
    tmp = []

    # Menghilangkan spasi, 'J', huruf redundan
    for i in range(len(kunci)):
        if (kunci[i] != ' ' and kunci[i] != 'J'):
            found = False
            for j in range(len(tmp)):
                if (kunci[i] == tmp[j]):
                    found = True
                    break
            if not(found):
                tmp.append(kunci[i])

    # Menambahkan huruf yang belum ada
    for i in range(26):
        found = False
        for j in range(len(tmp)):
            if (tmp[j] == chr(i + 65)):
                found = True
        if not(found):
            if (chr(i + 65) != 'J'):
                tmp.append(chr(i + 65))

    # Menjadikan matrix
    result = []
    for i in range(5):
        tmp2 = []
        for j in range(5):
            tmp2.append(tmp[5 * i + j])
        result.append(tmp2)
    
    print(result)
    return(result)

def create_plaintext_playfair(plaintext):
    tmp = []
    result = []

    # Menghilangkan spasi, mengganti 'J' menjadi 'I'
    for i in range(len(plaintext)):
        if (plaintext[i] == 'J'):
            tmp.append('I')
        elif (plaintext[i] != ' '):
            tmp.append(plaintext[i])

    # Merancang plaintext playfair
    i = 0
    while(i < len(tmp) - 1):
        first = tmp[i]
        second = tmp[i + 1]
        if (first == second):
            result.append(first)
            result.append('X')
            i += 1
        else:
            result.append(first)
            result.append(second)
            i += 2
    if (i != len(tmp)):
        result.append(tmp[len(tmp) - 1])
        result.append('X')
    print(result)
    return(result)

def playfair_encrypt(plaintext, kunci):
    result = []
    for i in range(int(len(plaintext) / 2)):
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        for j in range(5):
            for k in range(5):
                if (plaintext[i * 2] == kunci[j][k]):
                    x1 = j
                    y1 = k
                if (plaintext[i * 2 + 1] == kunci[j][k]):
                    x2 = j
                    y2 = k
        if (x1 == x2 and y1 != y2):
            result.append(kunci[x1][(y1 + 1) % 5])
            result.append(kunci[x2][(y2 + 1) % 5])
        elif (x1 != x2 and y1 == y2):
            result.append(kunci[(x1 + 1) % 5][y1])
            result.append(kunci[(x2 + 1) % 5][y2])
        else:
            result.append(kunci[x1][y2])
            result.append(kunci[x2][y1])
    return(''.join(result))

def playfair_decrypt(ciphertext, kunci):
    result = []
    for i in range(int(len(ciphertext) / 2)):
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        for j in range(5):
            for k in range(5):
                if (ciphertext[i * 2] == kunci[j][k]):
                    x1 = j
                    y1 = k
                if (ciphertext[i * 2 + 1] == kunci[j][k]):
                    x2 = j
                    y2 = k
        if (x1 == x2 and y1 != y2):
            result.append(kunci[x1][(y1 - 1 + 5) % 5])
            result.append(kunci[x2][(y2 - 1 + 5) % 5])
        elif (x1 != x2 and y1 == y2):
            result.append(kunci[(x1 - 1 + 5) % 5][y1])
            result.append(kunci[(x2 - 1 + 5) % 5][y2])
        else:
            result.append(kunci[x1][y2])
            result.append(kunci[x2][y1])
    return(''.join(result))