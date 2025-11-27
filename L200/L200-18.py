# Auteur - Noah M.
# 18. Découpez vos Chaînes : La Puissance de Split

# Ecriture de base split.
#string.split(separator,maxsplit)

# Cas 1:
stg = "My name is Noah"
print(f"String = {stg}")

# Decoupage de string.
print(f"Decoupage stg via les espace : {stg.split()}")

# Cas 2:
stg2 = "Noah, Camille, Laurent, MarieF"
print(f"String2 = {stg2}")

# Decoupage de string2 - séparateur 'virgule'.
print(stg2.split(","))

# Cas 3:
stg3 = "My name is Camille"
print(f"String = {stg}")
print(f"Decoupage max 2 & sep espace =>{stg3.split(" ",2)}")
