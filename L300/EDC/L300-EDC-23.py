# Auteur : Noah M.
# Analyse des mots d'une phrase
"""
Analyse une phrase et retourne des métriques simples.
Paramètres:
    phrase (str): La chaîne de caractères à analyser.
Retour:
    dict: Un dictionnaire contenant :
        - "mots": le nombre de mots dans la phrase
        - "longueur_max": la longueur (en caractères) du mot le plus long
"""
def analyser_phrase(phrase):
    # Découpe la phrase en mots en utilisant l'espace comme séparateur par défaut.
    mots = phrase.split()

    # Calcule la longueur maximale parmi tous les mots.
    # On itère sur chaque mot et on prend sa longueur avec len(mot).
    # max(...) renvoie la valeur la plus élevée.
    longueur_max = max(len(mot) for mot in mots)

    # Retourne un dictionnaire avec le nombre de mots et la longueur du mot le plus long.
    return {"mots": len(mots), "longueur_max": longueur_max}

resultat = analyser_phrase("Python est puissant et simple à apprendre")
print(resultat)
