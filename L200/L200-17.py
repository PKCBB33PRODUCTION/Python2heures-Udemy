# Auteur - Noah M.
# 17. Les Dictionnaires : Structurer Vos Données Clés-Valeurs

# Liste de valeur numérique
age = [5, 10, 15, 20]

#Liste de valeur string.
dico = {"Jordan": 5, "Kevin": 10, "Ahmed": 15, "Josephine": 20}
dico2 = {0: "Jordan", 1:"Bob", 2:"Ted"}

#Affichage Dico
print(f"dico = {dico}")

#Affichage Age
print(f"Jordan, {dico["Jordan"]} ans.")
print(f"Kevin, {dico["Kevin"]} ans.")

#Affichage Dico2
print(f"dico2 = {dico2}")
print(f"dico2 val 0 = {dico2[0]}")

#Boucle For Dico.
print("Affichage dico : ")
for i in dico:
    print(f"- {i}, {dico[i]} ans")

#Longueur dictionnaire :
print(f"Longueur dico : {len(dico)}")

#Ajout valeur a dico.
dico["bob"] = 25
print(f"dico = {dico}")
