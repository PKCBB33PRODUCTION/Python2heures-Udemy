# Autor : Noah M.
# Compter les Occurrences d’un Mot dans un Fichier Texte
mot = "Python"
def compter_occurences(patharticle):
    """Cette fonction lit un fichier de log et extrait les lignes contenant des erreurs."""
    with open (patharticle, "r", encoding="utf-8") as article:
        articles = article.readlines()
        nbrpython = 0
        for i in range(len(articles)):
            if mot in articles[i]:
                # print("Erreur trouvée :", logs[i]) # Mode Verbose.
                nbrpython = nbrpython + 1
    return nbrpython

print("Il y a",compter_occurences("Section7/EDC-31/article.txt"),"python dans l'article.")
