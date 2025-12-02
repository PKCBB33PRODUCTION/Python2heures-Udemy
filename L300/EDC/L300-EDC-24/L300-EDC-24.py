# Auteur : Noah M.
# Lecture et Comptage de Mots dans un Fichier Texte

with open("L300/EDC/L300-EDC-24/histoire.txt", "r" ) as file:
    contentline = file.read()
#print(contentline)

def compter_mots(texte):
    """Compte le nombre de mots dans une chaîne de caractères."""
    mots = texte.split()
    return len(mots)

print(compter_mots(contentline))