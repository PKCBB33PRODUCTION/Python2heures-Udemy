# Auteur : Noah M.
# Calculer la Fréquence des Mots dans une Phrase

# Phrase par défaut.
phrase = "Python est simple mais Python est puissant"

# La variable sépare tout les mot dans phrase.
mots = phrase.split()
# Mode Verbose
#print("prhase.split() :",mots)

# Initialisation du dictionnaire frequence.
frequence = {}

# Boucle for pour le comptage.
for mot in mots:
    # Condition si mot est déjà dans frequence
    if mot in frequence:
        # Doublon de mot => Ajout du mot +1.
        frequence[mot] += 1
        # Mode Verbose
        #print(mot," - ",frequence[mot])
    else:
        # Pas de doublon => Ajout du mot
        frequence[mot] = 1
        # Mode Verbose
        #print(mot," - ",frequence[mot])

print(frequence)

"""
Fonctionnement Mode Verbose :
Enlever tout les commentaire pour avoir un script plus parlant.
"""

#=========================#
#= (c) PKCBB33PRODUCTION =#
#=========================#