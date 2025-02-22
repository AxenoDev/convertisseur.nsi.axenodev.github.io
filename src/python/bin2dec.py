def bin2dec(binary): # pour mettre le nombre binaire pour le changer plus tard en nombre décimal
    decimal = 0 # initialisation de la variable decimal
    for digit in binary: # boucle pour chaque chiffre du nombre binaire
        decimal = decimal * 2 + int(digit) # calcul du nombre binnaire
    print(f"Le chiffre décimal de {binary} est {decimal}") # affichage du nombre décimal
    return decimal # retourne le nombre décimal