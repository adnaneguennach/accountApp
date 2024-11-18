from serie1.Compte import Compte
class CompteCourant(Compte):
    def __init__(self, proprietaire, solde, montantDecouvert):
        Compte.__init__(self,proprietaire, solde )
        self.__montantDecouvert = montantDecouvert
        print(Compte.nb)
    @property
    def getMontantDecouvert(self):
        return self.__montantDecouvert
    def __str__(self):
        return str(Compte.__str__(self)) + str(" Montant découvert ") + str(self.getMontantDecouvert)
