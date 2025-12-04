# Auteur : Noah M.
# 20. Comprendre les fonctions et ajouter des paramètres
# I- Première fonction.
"""
Cette fonction permet d'afficher Hello World.
"""
def HelloWorld():
    print("Hello World!")

#Ici cette ligne de code s'affiche avant la fonction
print("1-Line")

#Execution de ma fonction.
HelloWorld()

# II- Deuxième Fonction
"""
Cette fonction permet de saluer un utilisateur.
(Interaction => No)
"""
def WelcomeUser(name):
    print(f"Welcome {name}")

# Nom par défaut ici noah.
WelcomeUser("Noah")

# II-bis- Deuxième Fonction
"""
Cette fonction permet de saluer un utilisateur.
(Interaction => Yes.) 
"""
def WelcomeUser(name):
    print(f"Welcome {name}")

name = input("Enter your name: ")
WelcomeUser(name)

#=========================#
#= (c) PKCBB33PRODUCTION =#
#=========================#