
    # Programme numéro 4 du devoir de programmation linéaire P2 du cours AI-1
    # Par Samira Lehlou et Michel Paquin cours 420-004-XX Groupe 12504
'''
    Cette fonction récursive permet de calculer la somme de tous les composantes d'un nombre
    en sauvegardant les résultats intermédiaires.
    En dépilant les valeurs sont
'''
def add_recursive_mem(nombre:int , memo={}):
    if (nombre == 1):
        return 1
    else:
        if nombre in memo:
            return memo[nombre]
        else:
            memo[nombre] = add_recursive_mem(nombre - 1, memo) + add_recursive_mem(nombre - 1, memo)
            return memo[nombre]


if __name__ == '__main__':
    print("Nombre = 4 :", add_recursive_mem(4))
    print("Nombre = 5 :", add_recursive_mem(5))
    print("Nombre = 10:", add_recursive_mem(10))
    print("Nombre = 30:", add_recursive_mem(30))