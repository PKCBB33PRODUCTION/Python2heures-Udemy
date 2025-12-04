# Autor : Noah M.
# Compter les Occurrences d’un Mot dans un Fichier Texte
mot = "Python"
def compter_occurences(patharticle):
    """Cette fonction lit le fichier article.txt, compte le nombre d'occurence du mot Python, retourne la valeur."""
    with open (patharticle, "r", encoding="utf-8") as article:
        articles = article.readlines()
        nbrpython = 0
        for i in range(len(articles)):
            if mot in articles[i]:
                # print("Python trouvé :", articles[i]) # Mode verbose.
                nbrpython = nbrpython + 1
    return nbrpython

# Affiche le nombre d'occurence.
print("Il y a",compter_occurences("Section7/EDC-31/article.txt"),"python dans l'article.")

#=========================#
#= (c) PKCBB33PRODUCTION =#
#=========================#