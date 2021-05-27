import random

longpasswd = int(input("donner la longueur du mot de passe "))
choice_letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&()*+,-./:;<=>?@[]^_`{|}~'

password ="".join(random.sample(choice_letter, longpasswd))
print(longpasswd)
print("votre mot de passe est "+ password)