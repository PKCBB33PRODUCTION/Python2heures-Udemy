# Auteur - Noah M.
# Script sur la manipulation des liste.

age = [5, 10, 15, 20, 25, 30, 35, 40]

# Boucle for.
print("")
for i in age:
    print(i)

# Boucle for & liste mot.
print("")
for j in ["Bonjour","je","m'appelle","Noah"]:
    print(j)

# Boucle for & range 5.
print("")
for k in range(5):
    print(k)

# Boucle for & condition.
print("")
for l in age:
    if l >= 18:
        print(f"{l} - Vous êtes majeur.")
    else :
        print(f"{l} - Vous êtes mineur.")