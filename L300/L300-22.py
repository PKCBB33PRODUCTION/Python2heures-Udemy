# Auteur : Noah M.
# 22. Utiliser les valeurs par défaut pour nos paramètres.
"""
Cette fonction permet de saluer un utilisateur.
Si pas de paramètre noter alors utilisation valeur par défault.
Celle ci affiche le resultat avec print.
(Interaction User => No)
"""
def WelcomeUser(name="Unknow"):
    print(f"Welcome {name} !")
# Execution sans paramètres.
WelcomeUser()

# Execution avec paramètres.
WelcomeUser("Noah")

#Execution avec paramètres précis.
WelcomeUser(name="PK")

#=========================#
#= (c) PKCBB33PRODUCTION =#
#=========================#