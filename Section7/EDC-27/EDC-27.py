# Autor : Noah M.
# Journal des erreurs.
def journal_erreurs(pathlog, patherror):
    """Cette fonction lit un fichier de log et extrait les lignes contenant des erreurs."""
    with open (pathlog, "r", encoding="utf-8") as logfile:
        logs = logfile.readlines()
        for i in range(len(logs)):
            if "ERROR" in logs[i]:
                # print("Erreur trouvée :", logs[i]) # Mode Verbose.
                with open(patherror, "a", encoding="utf-8") as errorfile:
                    errorfile.write(logs[i])
            else:
                pass
                # print("Pas d'erreur :", logs[i]) # Mode Verbose.
journal_erreurs("Section7/EDC-27/log.txt", "Section7/EDC-27/erreurs.txt")