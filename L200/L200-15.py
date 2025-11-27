# Auteur - Noah M.
# Script sur la manipulation des liste.
age = [10, 20, 30, 40]
print("Longueur liste : ",len(age))

valappend = 50
age.append(valappend)
print(f"Valeur ajouté à la fin de la liste {valappend} : {age}")

valinsert = 15
placeinsert = 1
age.insert(placeinsert, valinsert)
print(f"La Valeur {valinsert} est placé à la place {placeinsert} : {age}")

placesuppr = 0
valdel = age[placesuppr]
del(age[placesuppr])
print(f"La valeur {placesuppr} - {valdel} est supprimé : {age}")

