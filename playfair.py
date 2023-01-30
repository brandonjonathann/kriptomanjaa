kunci = "JALAN GANESHA SEPULUH"
kunci_tmp = [x for x in kunci]
kunci_asli = []

for i in range(len(kunci_tmp)):
    if (kunci_tmp[i] != ' ' and kunci_tmp[i] != 'J'):
        found = False
        for j in range(len(kunci_asli)):
            if (kunci_tmp[i] == kunci_asli[j]):
                found = True
                break
        if not(found):
            kunci_asli.append(kunci_tmp[i])

for i in range(26):
    found = False
    for j in range(len(kunci_asli)):
        if (kunci_asli[j] == chr(i + 65)):
            found = True
    if not(found):
        if (chr(i + 65) != 'J'):
            kunci_asli.append(chr(i + 65))

kunci_akhir = []
for i in range(5):
    tmp = []
    for j in range(5):
        tmp.append(kunci_asli[5 * i + j])
    kunci_akhir.append(tmp)

print(kunci_asli)
print(kunci_akhir)