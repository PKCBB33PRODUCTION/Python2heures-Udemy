# Auteur : Noah M.
# Travailler avec des fichiers texte.
# Lecture du fichier en entier.
with open("L300/L300-24/exemple.txt", "r" ) as file:
    content = file.read()
print(content)

print("Lecture ligne/ligne :")
with open("L300/L300-24/exemple.txt", "r" ) as file:
    contentline = file.readline()
print(contentline)

print("Lecture sous forme de liste:")
with open("L300/L300-24/exemple.txt", "r" ) as file:
    contentline = file.readlines()
print(contentline)

# Ajout nouvelle ligne à la fin du fichier
with open("L300/L300-24/exemple.txt", "a" ) as file:
    file.write("\nLine 4 - Add a new line.")

# Remplacement du contenu du fichier
with open("L300/L300-24/exemple.txt", "w" ) as file:
    file.write("It Will erase the file.")

#=========================#
#= (c) PKCBB33PRODUCTION =#
#=========================#