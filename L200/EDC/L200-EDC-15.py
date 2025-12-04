# Auteur : Noah M.
# Créer et Parcourir un Dictionnaire
# Création du dictionnaire.
ages = {"Alice": 30, "Bob": 25}

# Création d'une liste.
result = []

# Fonction qui parcours le dictionnaires.
for nom, age in ages.items():
    result.append(f"{nom} a {age} ans.")
print("\n".join(result))

#=========================#
#= (c) PKCBB33PRODUCTION =#
#=========================#