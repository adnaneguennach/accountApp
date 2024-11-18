class Compte:
    nb = 0
    def __init__(self,proprietaire, solde):
        self.__proprietaire = proprietaire
        self.__solde = solde
        Compte.nb += 1
        self.__num = Compte.nb

    @property
    def num(self):
        return self.__num

    @property
    def proprietaire(self):
        return self.__proprietaire

    @property
    def solde(self):
        return self.__solde
    
    @property
    def con(self):
        return Compte.nb

    def __str__(self):
        return ("Numéro de Compte : " + str(self.__num) + " Propriétaire : "
                + self.__proprietaire+ " et Solde : "+ str(self.__solde))
    
    @classmethod
    def printcompte():
        print(Compte.nb)


nb = Compte(5, 5)