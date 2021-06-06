class Voiture:
    def __init__(self, marque):
        self.marque = marque
    def afficher_marque(self):
        print(f"j'ai une {self.marque}")
voiture_01 = Voiture("Nissan")

voiture_02 = Voiture("BMW")

voiture_01.afficher_marque()
Voiture.afficher_marque(voiture_02)
print(voiture_02.marque)




