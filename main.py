# Cypher

def encrypt(mot, clef, direct):
    mot_encrypt = ""
    ind = ""
    for item in range(0, len(alpha)):
        if direct == "encode":
            if item + clef < 25:
                ind = item + clef
            else:
                ind = (item + clef) % 26
        elif direct == "decode":
            if item - clef < 0:
                ind = 26 + (item - clef)
            else:
                ind = (item - clef)
        alpha_swap.append(alpha[ind])

    for lettre in mot:
        pos = alpha.index(lettre)
        mot_encrypt += alpha_swap[pos]
    print(mot_encrypt)

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direct = input("Tape 'encode' pour encrypter, tape 'decode' pour decrypter:\n")
mot = input("Taper votre message:\n").lower()
clef = int(input("Taper la clé d'encryption en chiffre:\n"))

alpha_swap = []
shift_clean = clef % 26

encrypt(mot, shift_clean, direct)