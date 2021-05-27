import random

nmbre_proposé = random.randint(1, 6)

resultat=0

for i in range(3):
    nmbre_choisi = int(input('saisir un nbre : '))
    if nmbre_proposé == nmbre_choisi:
        resultat=1
        break

    elif nmbre_proposé > nmbre_choisi:
        print("Le nmbre que vous avez choisi est superieur")

    elif nmbre_proposé < nmbre_choisi:
        print("Le nmbre que vous avez choisi est inferieur")

if resultat==1:
    print("Bravo vous avez Gagné !!")
    print(f"le bon numero est {nmbre_proposé}")
else:
    print(f"vous avez perdu, le bon numero est {nmbre_proposé}")

#print(f"le nombre choisi est {nmbre_choisi}")
#print(f"le nombre proposé est {nmbre_proposé}")
