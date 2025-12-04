# Auteur : Noah M.
# Calculer la Moyenne d’Âge dans un Fichier CSV
# Importation du module CSV.
import csv

def moyenne_age(fichier_csv) : 
    """Cette fonction permet de calculer la moyenne d'age de personne a partir de deonné dans le fichier CSV."""
    # Initialisation compteur.
    age_total = 0
    nbpersonne = 0
    with open(fichier_csv, "r") as file:
        # Permet de lire le fichiers csv.
        reader = csv.DictReader(file)
        for line in reader:
            # Ajoute de l'age des personnes.
            age_total = age_total + int(line["Age"])
            # Ajout du nombres de personne.
            nbpersonne = nbpersonne + 1
    # Calcul moyenne age.
    moyenne_age = age_total / nbpersonne
    # Retour la la moyenne d'age.
    return moyenne_age
    
resultat = moyenne_age("L300/EDC/L300-EDC-25/employes.csv")
# Affiche le resultat.
print(resultat)

#=========================#
#= (c) PKCBB33PRODUCTION =#
#=========================#