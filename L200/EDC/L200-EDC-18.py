# Auteur : Noah MAILLET
# Générer une Liste de Nombres avec range
# Rechercher une Valeur dans un Dictionnaire
# Ensemble des clé dans le dictionnaire
produits = {"pommes": 2, "bananes": 3, "cerises": 5}

"""
La version ci dessous implique un contact avec l'utilisateur pour vérifier le prix.
Elle ne prends pas en compte l'in
# Demande de choix à l'utilisateur.
choix = input("Saisissez une clé: ")

# Verficiation existence du produit.
if choix in produits:
    # Produit existant => Affichage
    print(f"Vous avez choisi {choix} voici le prix : {produits[choix]} euros")
else:
    # Produit inexistant => Erreur.
    print("Clé introuvable")
"""

# Correction.
# Vérif présences bananes
if "bananes" in produits:
    # Bananes => Ok.
    result = produits["bananes"]
else:
    # Bannanes => Ko.
    result = "Produit non trouvé."
print(result)