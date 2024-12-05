class Stylo:
    def __init__(self, couleur, marque):
        self.couleur = couleur
        self.marque = marque
        self.text = ""
        self.encre = 100

    def ecrire(self, texte):
        for lettre in texte:
            self.encre -= 1
            if self.encre < 0:
                print("Plus d'encre")
                break
            self.text += lettre
        print(texte)

    def effacer(self):
        print("Effacer")


stylo1 = Stylo(couleur="rouge", marque="bic")
print(stylo1.couleur)
print(stylo1.encre)
stylo1.ecrire("Bonjour")
print(stylo1.encre)
