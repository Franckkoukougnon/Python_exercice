texte = str(input('donnez votre nom et prenom : '))


def accro_gen(chaine):
    mots = chaine.split()
    accro = ""
    for i in mots:
        accro = accro + str(i[0].upper())
    return accro


resultat = accro_gen(texte)

print(f"votre accronyme est {resultat}")
