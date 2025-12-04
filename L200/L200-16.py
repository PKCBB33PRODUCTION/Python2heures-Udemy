# Auteur - Noah M.
# 16. Les Boucles : Répéter et Automatiser avec For
# Definition de la listes.
age = [5, 10, 15, 20, 25, 30, 35, 40]

# Boucle for.
print("")
for i in age:
    # Affiche la liste age.
    print(i)

# Boucle for & liste mot.
print("")
mot = ["Bonjour","je","m'appelle","Noah"]
for j in mot:
    # Affiche de la liste de mot.
    print(j)

# Boucle for & range 5.
print("")
for k in range(5):
    # Affiche un compteur de 0 à 5.
    print(k)

# Boucle for & condition.
print("")
for l in age:
    if l >= 18:
        print(f"{l} - Vous êtes majeur.")
    else :
        print(f"{l} - Vous êtes mineur.")

#=========================#
#= (c) PKCBB33PRODUCTION =#
#=========================#