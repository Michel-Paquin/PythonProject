
# Programme numéro 3 du devoir de programmation linéaire P2 du cours AI-1
# Par Samira Lehlou et Michel Paquin cours 420-004-XX Groupe 12504
'''
Cette fonction récursive permet de calculer la somme de tous les composantes d'un nombre

'''
def add_recursive(nombre):
    if (nombre == 1):
        return 1
    else:
        return add_recursive(nombre - 1) + add_recursive(nombre - 1)


if __name__ == '__main__':
    print("Nombre = 4 :", add_recursive(4))
    print("Nombre = 5 :", add_recursive(5))
    print("Nombre = 10:", add_recursive(10))
    print("Nombre = 30:", add_recursive(30))