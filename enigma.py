# Karena terdapat terlalu banyak jenis mesin enigma,
# digunakan sistem yang diajarkan di kelas
# dengan setting wiring masing-masing rotor yang didapat dari 
# https://en.wikipedia.org/wiki/Enigma_rotor_details

default = []
for i in range(26):
    default.append(chr(i + 65))

#       = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
wiring1 = "DMTWSILRUYQNKFEJCAZBPGXOHV"
wiring2 = "HQZGPJTMOBLNCIFDYAWVEUSRKX"
wiring3 = "UQNTLSZFMREHDPXKIBVYGJCWOA"

rotor1 = [x for x in wiring1]
rotor2 = [x for x in wiring2]
rotor3 = [x for x in wiring3]

position1 = 1
position2 = 1
position3 = 1

ring1 = 1
ring2 = 1
ring3 = 1

notch1 = 7
notch2 = 3
notch3 = 2

plaintext = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
plaintext = [x for x in plaintext]

def find_coordinate(target, plaintext, default):
    for j in range(26):
        if (target == default[j]):
            return j
    
for i in range(len(plaintext)):
    plaintext[i] = rotor1[find_coordinate(plaintext[i], plaintext, default)]
    plaintext[i] = rotor2[find_coordinate(plaintext[i], plaintext, default)]
    plaintext[i] = rotor3[find_coordinate(plaintext[i], plaintext, default)]

    tmp = []
    for j in range(25):
        tmp.append(rotor1[j + 1])
    tmp.append(rotor1[0])

    rotor1 = tmp

    if (position2 == notch2 and position1 == notch1):
        position3 = (position3 + 1) % 26

    if (position1 == notch1):
        position2 = (position2 + 1) % 26

    position1 = (position1 + 1) % 26

    print(position1, position2, position3)


print(plaintext)