
# Programme sommaire de programmation pour le Projet no 2 du cours AI-1
# Par Samira Lehlou et Michel Paquin cours 420-004-XX Groupe 12504
'''
Ce petit programme affiche les différentes options à exécuter pour la partie 2
du projet du cours d'intelligence artificielle no 1
'''
import Récursivité_simple
from Programmation_Linéaire import *
from Programmation_dynamique import *
from Récursivité_simple import *
from Test_de_performance import *

option = '1'
while option in ('1','2','3','4'):
    print('Intelligence Artificielle 1 - Projet partie 2')
    print("1 - Exécuter l'exercice de programmation linéaire")
    print("2 - Exécuter l'exercice de récursivité simple")
    print("3 - Exécuter l'exercice de récursivité dynamique")
    print("4 - Exécuter l'exercice de comparaison entre récursivité simple et dynamique")
    print("Appuyez sur n'importe quelle autre touche pour terminer")
    option = input("Entrez votre choix et faites <enter>: ")
    if option == '1':
        print('1- Programmation Linéaire')
        programmation_linéaire()
    elif option == '2':
        print('2- récursivité simple')
        print("Nombre = 4 :", add_recursive(4))
        print("Nombre = 5 :", add_recursive(5))
        print("Nombre = 10:", add_recursive(10))
        print("Nombre = 30:", add_recursive(30))
    elif option == '3':
        print('3- Programmation Dynamique')
        print("Nombre = 4 :", add_recursive_mem(4))
        print("Nombre = 5 :", add_recursive_mem(5))
        print("Nombre = 10:", add_recursive_mem(10))
        print("Nombre = 30:", add_recursive_mem(30))
    elif option == '4':
        print('4- Test_de_performance')
        performance(4)
        performance(5)
        performance(10)
        performance(30)
    else:
        print('Fin')