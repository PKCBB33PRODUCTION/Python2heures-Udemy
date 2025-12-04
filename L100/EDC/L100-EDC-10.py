# Autor : Noah M.
# Création menu interactif.
# Definition valeur.
choix = 3  # Exemple : option choisie
a = 5  # Nombres à traiter
b = 3  # Nombres à traiter

# Confidtion
if choix == 1:
    # Si choix = 1
    addition = a + b
    print("Choix Addition")
    print(f"{a} + {b}  = {addition}")
elif choix == 2:
    # Si choix = 2
    multiplication = a * b
    print("Choix Multiplication")
    print(f"{a} * {b} = {multiplication}")
elif choix == 3:
    # Si choix = 3
    print("Au revoir")
else:
    # Sinon
    print("Erreur 404 - Choix non trouvé.")
    print("Au revoir")

#=========================#
#= (c) PKCBB33PRODUCTION =#
#=========================#