class CompteBancaire:
    def __init__(self, numeroCompte, solde):
        self.numeroCompte = numeroCompte
        self.solde = solde

    @classmethod
    def augmenterSolde(cls, listeComptes, montant):
        return list(map(lambda compte: cls(compte.numeroCompte, compte.solde + montant), listeComptes))
    
    @staticmethod
    def appliquerInteret(listeComptes, tauxInteret):
        for compte in listeComptes:
            compte.solde *= (1 + tauxInteret/100)
    
    @staticmethod
    def filtrerComptes(listeComptes, soldeMin):
        return list(filter(lambda compte: compte.solde >= soldeMin, listeComptes))
    
    def afficherInfo(self):
        return print("Numéro de compte : " + str(self.numeroCompte) + "Solde :" + str(self.solde) +"€")