# Autor : Noah M.
# Générer un Rapport d'Âge Moyen à partir d’un CSV
import csv

def moyenne_age_rapport(path_csv,path_rapport) : 
    """Cette fonction génère un rapport d'age moyen a partir d'un fichier CSV."""
    age_total = 0
    nbpersonne = 0
    with open(path_csv, "r") as file:
        reader = csv.DictReader(file)
        for line in reader:
            age_total = age_total + int(line["Age"])
            nbpersonne = nbpersonne + 1
    moyenne_age = age_total / nbpersonne

    print("Moyenne age : ", moyenne_age)
    print("Age total : ", age_total)

    with open(path_rapport, "w") as rapport:
        rapport.write("Rapport d'age moyen : \n")
        rapport.write(f"- Nombre de personnes : {nbpersonne}\n")
        rapport.write(f"- Age moyen : {moyenne_age} ans\n")

# Execution de la fonction.
moyenne_age_rapport('Section7/EDC-28/personnes.csv','Section7/EDC-28/rapport.txt')

#=========================#
#= (c) PKCBB33PRODUCTION =#
#=========================#