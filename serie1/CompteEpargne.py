from serie1.Compte import Compte
class CompteEpargne(Compte):
    def __init__(self,proprietaire,solde,interet):
        Compte.__init__(self,proprietaire, solde)
        self.__interet = interet
        print(Compte.nb)
    @property
    def getInteret(self):
        return self.__interet
    def __str__(self):
        return Compte.__str__(self) + " Interet " + str(self.getInteret)
