class CompteBancaire:
    def __init__(self, numeroCompte, solde):
        self.numeroCompte = numeroCompte
        self.solde = solde

    @classmethod
    def augmenterSolde(cls, compte, montant):
        return list(map(lambda compte: cls(compte.numeroCompte, compte.solde + montant), compte))