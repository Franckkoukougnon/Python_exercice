texte=str(input('donnez votre nom et prenom : '))
mots=texte.split()
accro =""
for i in mots:
    accro=accro+str(i[0].upper())

print(f"votre accronyme est {accro}")