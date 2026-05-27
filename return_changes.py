coins = [1, 2, 5, 10]
amount = 11

def return_changes(coins, amount):
    if amount == 0:
        return 0

    if not coins:
        return float("inf")

    coins.sort(reverse=True)
    # [10, 5, 2, 1]

    amount_of_coins = 0
    tmp_amount = amount
    
    for coin in coins:
        if coin > tmp_amount:
            # coins = 5 > amount = 1
            # coins = 2 > amount = 1
            continue
        
        """ Je regarde combien de fois je peux utiliser la pièce pour atteindre le montant restant """
        rest = tmp_amount // coin
        # coin(10) rest = 11 // 10 = 1
        
        # coin(5) pas possible car 5 > 1
        # coin(2) pas possible car 2 > 1
        
        # coin(1) rest = 1 // 1 = 1


        """ Je soustrais le montant que j'ai atteint avec la pièce du montant restant """
        tmp_amount -= rest * coin
        # coin(10) tmp_amount = 11 - 1 * 10 = 1
        # Donc la prochaine iteration de la boucle le tmp_amount sera égal à 1

        # coin(5) Pas possible car 5 > 1
        # coin(2) Pas possible car 2 > 1

        # coin(1) tmp_amount = 11 - 1 * 10 = 1
        # Donc la tmp_amount sera égal à 0 et je pourrai sortir de la boucle

        """ J'ajoute le nombre de pièces utilisées à mon compteur de pièces """
        amount_of_coins += rest
        # coin(10) amount_of_coins = 0 + rest(1) = 1
        # coin(1) amount_of_coins = 1 + rest(1) = 2

        """ 
        Si le montant restant est égal à 0, 
        cela signifie que j'ai atteint le montant cible
        avec les pièces utilisées, donc je peux sortir de la boucle
        """
        if tmp_amount == 0:
            break

    if tmp_amount != 0:
        return -1

    """ Je crée une nouvelle liste de pièces sans la première pièce (la plus grande)"""
    new_coins = coins[1:]

    """ 
    Je compare le nombre de pièces utilisées
    avec le nombre de pièces que j'aurais utilisé
    si je n'avais pas utilisé la première pièce (la plus grande)
    """
    amount_of_coins = min(amount_of_coins, return_changes(new_coins, amount))
    # coin(10) amount_of_coins = min(2, return_changes([5, 2, 1], 11))
    # coin(5) amount_of_coins = min(2, return_changes([2, 1], 11))
    # coin(2) amount_of_coins = min(2, return_changes([1], 11))
    # coin(1) amount_of_coins = min(2, return_changes([], 11)) la recursion s'arrête car la liste de pièces est vide et retourne inf

    return amount_of_coins



print(f"Should return 0: {return_changes([1, 2, 5], 0)}")
print(f"Should return 1: {return_changes([1, 2, 5], 5)}")
print(f"Should return 2: {return_changes([1, 2, 5, 10], 11)}")
print(f"Should return 9: {return_changes([1, 5, 10, 25], 99)}")
print(f"Should return 7: {return_changes([1, 2, 5, 10, 20, 50], 320)}")
print(f"Should return 2: {return_changes([1, 3, 4], 6)}")
print(f"Should return -1: {return_changes([4, 6, 8], 2001)}")