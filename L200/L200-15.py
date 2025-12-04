# Auteur - Noah M.
# 15. Transformer vos Listes : Ajouter, Supprimer, Insérer
#Definition de la liste.
age = [10, 20, 30, 40]

# Len affiche la longueur de la liste.
print("Longueur liste : ",len(age))

valappend = 50
age.append(valappend)
# Ajout de le valeur 50 a la fin de la liste.
print(f"Valeur ajouté à la fin de la liste {valappend} : {age}")

valinsert = 15
placeinsert = 1
# Ajout de "15" à la place "1".
age.insert(placeinsert, valinsert)
print(f"La Valeur {valinsert} est placé à la place {placeinsert} : {age}")

placesuppr = 0
valdel = age[placesuppr]
# Suppression de la valeur 0.
del(age[placesuppr])
print(f"La valeur {placesuppr} - {valdel} est supprimé : {age}")

#=========================#
#= (c) PKCBB33PRODUCTION =#
#=========================#