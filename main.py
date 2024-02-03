from CompteBancaire import CompteBancaire

compte1 = CompteBancaire(123, 500)
compte2 = CompteBancaire(456, 1000)
compte3 = CompteBancaire(789, 1500)

listeComptes = [compte1, compte2, compte3]


print("Solde des comptes : ")
print(compte1.solde)
print(compte2.solde)
print(compte3.solde)


listeComptes = CompteBancaire.augmenterSolde(listeComptes, 100)

print("Nouveau solde des comptes : ")
for compte in listeComptes:
    print(compte.solde)


CompteBancaire.appliquerInteret(listeComptes, 5)

print("Nouveau solde des comptes : ")
for compte in listeComptes:
    print(compte.solde)
