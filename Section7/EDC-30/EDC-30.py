# Autor : Noah M.
# Lecture et Analyse d’un Fichier de Configuration
def lire_config(fichier):
    config = {}
    with open(fichier, "r") as f:
        for ligne in f:
            if "=" in ligne:
                cle, valeur = ligne.strip().split("=", 1)
                config[cle] = valeur
    return config

# Exemple d'utilisation
resultat = lire_config("Section7/EDC-30/config.txt")
print(resultat)