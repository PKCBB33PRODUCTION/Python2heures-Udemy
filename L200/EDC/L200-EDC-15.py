# Auteur : Noah M.
# Créer et Parcourir un Dictionnaire
ages = {"Alice": 30, "Bob": 25}
result = []
for nom, age in ages.items():
    result.append(f"{nom} a {age} ans.")
print("\n".join(result))