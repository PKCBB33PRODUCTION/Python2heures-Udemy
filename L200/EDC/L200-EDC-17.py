# Auteur : Noah MAILLET
# Générer une Liste de Nombres avec range
# Variable de liste.
nblist = []

# Boucle qui génère une liste de 2 à 20.
for i in range(2,21,2):
    nblist.append(i)

"""
Explication fonctionnement Range : 
range(debut, fin, step)
exemple : 
range(2,21,2)
Donc range va générer une liste de 2 à 20 avec que des nombres pairs.
"""

# Affichage du resultat
print(nblist)
