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
    
    