# Auteur : Noah M.
# 23. Récapitulatif concernant les fonctions.
"""
Cette fonction permet de calculer le prix total d'une commande avec une TVA par défaut.
Si pas de paramètre renseigner alors utilisation valeur par défault..
(Interaction User => No)
"""
def PrixTTC(pHT, quantity, tva=0.2):
    pTTC = pHT * quantity * (1+tva)
    return pTTC

# Quantité & PrixHT
print("Prix TTC = ", PrixTTC(100, 2))

# Quantité & PrixHT & TVA
print("Prix TTC = ", PrixTTC(100, 2,0.05))

# Quantité & PrixHT & TVA
print("Prix TTC = ", PrixTTC(100, 2, tva=0.05))

# Quantité & PrixHT & TVA => Mis en valeur.
price = 100
quantity = 5
tax = 0.5
print("Prix TTC = ", PrixTTC(price, quantity, tax))

#=========================#
#= (c) PKCBB33PRODUCTION =#
#=========================#