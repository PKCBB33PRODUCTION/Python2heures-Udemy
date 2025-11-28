# Auteur : Noah MAILLET
# Générer une Liste de Nombres avec range
# Rechercher une Valeur dans un Dictionnaire
# Ensemble des clé dans le dictionnaire
produits = {"pommes": 2, "bananes": 3, "cerises": 5}

"""
# Voici ma version de code que j'ai choisie de mettre en place :
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
if "bananes" in produits:
    result = produits["bananes"]
else:
    result = "Produit non trouvé."
print(result)