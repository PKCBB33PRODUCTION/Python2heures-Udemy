# Auteur : Noah M.
# 21. Utiliser le return dans une fonction
# I- Addition Base.
"""
Cette fonction permet de faire un addition entre a & b.
Pas d'interaction user.
"""
def addition(a, b):
    return a + b

#Execution de ma fonction.
print("addition = ",addition(3, 2))

# II- Addition print.
"""
Cette fonction permet de faire un addition entre a & b.
Celle ci affiche le resultat avec print.
Pas d'interaction user.
"""
def addition_print(a, b):
    print("a+b =",a + b)

result = addition_print(5, 3)
print("result // addition_print = ", result)

# III- Addition return
"""
Cette fonction permet de faire un addition entre a & b.
Celle ci affiche le resultat avec print.
Pas d'interaction user.
"""
def addition_return(a, b):
    return a + b

result = addition_return(5, 3)
print("result // addition_return = ", result)

#=========================#
#= (c) PKCBB33PRODUCTION =#
#=========================#