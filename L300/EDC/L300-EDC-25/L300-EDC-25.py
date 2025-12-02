# Auteur : Noah M.
# Calculer la Moyenne d’Âge dans un Fichier CSV
import csv

def moyenne_age(fichier_csv) : 
    age_total = 0
    nbpersonne = 0
    with open(fichier_csv, "r") as file:
        reader = csv.DictReader(file)
        for line in reader:
            age_total = age_total + int(line["Age"])
            nbpersonne = nbpersonne + 1
    moyenne_age = age_total / nbpersonne
    
    return moyenne_age
    
resultat = moyenne_age("L300/EDC/L300-EDC-25/employes.csv")
print(resultat)