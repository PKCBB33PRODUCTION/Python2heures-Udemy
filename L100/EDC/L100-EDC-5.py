facture = 50
pourcentage_pourboire = 15
pourboire = facture * (pourcentage_pourboire/100)
total = facture + pourboire
print(f"Pour une facture de {facture} euros, laissez un pourboire de {pourboire} euros. Le total est de {total} euros.")