# Autor : Noah M.
# Trouver la Ligne Contenant un Mot dans un Fichier Texte
def trouver_ligne(patharticle, mot):
    """Cette fonction lit un texte et trouve le mot python."""
    with open (patharticle, "r", encoding="utf-8") as article:
        articles = article.readlines()
        wordfind = ""
        for i in range(len(articles)):
            if mot in articles[i]:
                #print("Python trouvé :", articles[i]) # Mode verbose.
                wordfind =  articles[i]
    return wordfind

print(trouver_ligne("Section7/EDC-32/manuel.txt","Python"))