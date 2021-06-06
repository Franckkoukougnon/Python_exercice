import random

choicePlayer = ['ciseaux', 'pierre', 'feuille']

cpu = random.choice(choicePlayer)

player = str(input("Choisissez entre: pierre, feuille , ciseaux : ")).capitalize()

if player == cpu:
    print("egalité")

elif player == "ciseau":
    if cpu == "pierre":
        print("vous avez perdu car la pierre casse le ciseau !!!")
    elif cpu == "feuille":
        print("vous avez gagné car le ciseau coupe la feuille")

elif player == "Pierre":
    if cpu == "ciseau":
        print("vous avez gagné car la pierre casse le ciseau !!!")
    elif cpu == "feuille":
        print("vous avez perdu car la feuille couvre la pierre")

elif player == "ciseau":
    if cpu == "pierre":
        print("vous avez perdu car la pierre casse le ciseau !!!")
    elif cpu == "feuille":
        print("vous avez gagné car le ciseau coupe la feuille")

elif player == "feuille":
    if cpu == "pierre":
        print("vous avez gagné car la feuille couvre la pierre !!!")
    elif cpu == "ciseau":
        print("vous avez perdu car le ciseau coupe la feuille")

