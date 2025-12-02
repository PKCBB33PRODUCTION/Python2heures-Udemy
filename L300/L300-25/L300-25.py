# Auteur : Noah M.
# 25. Le CSV notre premier format de données structurées

# Lecture du fichier contact.csv
with open("L300/L300-25/contact.csv", "r") as file:
    content = file.read()
print(content)

print("Lecture ligne/ligne :")
# Importation du module csv
import csv
# Lecture du fichier contact.csv avec le module csv
with open("L300/L300-25/contact.csv", "r") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)

print("")
print("Lecture colonne/colonne :")
# Lecture du fichier contact.csv colonne / colonne
with open("L300/L300-25/contact.csv", "r") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line[0],"//", line[1],"//", line[2])

# Création d'un nouveau fichier csv.
with open("L300/L300-25/new_contact.csv","w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Phone", "Mail"])
    writer.writerow(["Teddy", "111-222", "teddy@example.com"])

print("")
print("Lecture en dictionnaire :")
# Lecture du fichier contact.csv en dictionnaire.
with open("L300/L300-25/contact.csv", "r") as file:
    reader = csv.DictReader(file)
    for line in reader:
        print(line)

print("")
print("Lecture ligne dictionnaire :")
# Lecture du fichier contact.csv en dictionnaire ligne par ligne.
with open("L300/L300-25/contact.csv", "r") as file:
    reader = csv.DictReader(file)
    for line in reader:
        print(line["Name"])
