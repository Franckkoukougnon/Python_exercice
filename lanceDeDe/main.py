import random

while True:
    x=int(input("cliquer sur les boutons : "))
    if x==0:
        print('Bye, à la prochaine')
        break
    else:
        print(random.randint(1, 9))

