def leap_year(year):
    """Je dois forcément écrire une documentation alors voilà:
    Ce code prend en entrée une année et vérifie en condition 1 si cette année est divisible par 4. Si elle ne l'est pas alors elle n'est pas bissextile. Mais si elle est divisible par 4 on vérifie si c'est un multiple de 100 via la condition 2. Si elle n'est pas multiple de 100 alors confirmée bissextile, sinon on vérifie la condition sinequanone pour les multiples de 100: être également multiple de 400 avec d'être déclarée bissextile"""
    
    condition_1 = year % 4 == 0
    condition_2 = year % 100 == 0
    condition_3 = year % 400 == 0

    if condition_1:
        if condition_2:
            answer = condition_3
        else:
            answer = True
    else:
        answer = False
        
    return answer
