
from pulp import *

# Programme numéro 1 du devoir de programmation linéaire P2 du cours AI-1
# Par Samira Lehlou et Michel Paquin cours 420-004-XX Groupe 12504
'''
Cette fonction utilise le module Pulp pour résoudre le problème suivant:
    Nicki a deux emplois à temps partiel
        Emploi no 1 (E1):
            Salaire(S1) = $40/heure
            Préparation(P1) = 2 heures
        Emploi no 2 (E2):
            Salaire = $30/heure
            Préparation(P2) = 1 heure 
        Contraintes:
            Heures Emploi 1 (H1) + Heures Emploi 2 (H2) <= 12 heures.
            Préparation(P1) + Préparation(P2) <= 16 heures.
            Les nombre d'heures H1 et H2 ne peuvent être négatives: H1 >=0 et H2 >= 0;

    Il faut trouver la combinaison qui donnera un revenu maximal
'''
def programmation_linéaire():
    #Programmation Standard
    Salaire_Optimum = 0
    H1 = 0
    H2 = 0
    preparation_finale =0

    for Heures1 in range(12, 0, -1):
        for Heures2 in range((12 - Heures1),0,-1):
            Preparation = (Heures1 * 2) + Heures2
            if Preparation <= 16:
                Salaire = (Heures1 * 40) + (Heures2 *30)
                if Salaire > Salaire_Optimum:
                    Salaire_Optimum = Salaire
                    H1 = Heures1
                    H2 = Heures2
                    preparation_finale = Preparation

    print ('Résultats Programmation Standard:')
    print('Salaire Optimum : $', Salaire_Optimum)
    print("Nombre d'heures Emploi à $40 :", H1)
    print("Nombre d'heures Emploi à $30 :", H2)
    print("Préparation :" , str(preparation_finale))

    # Programmation avec Pulp
    problème : LpProblem = LpProblem('Salaire', LpMaximize)
    # Définition des variables
    h1 = LpVariable('h1', 0, 12, LpInteger)
    h2 = LpVariable('h2', 0, 12, LpInteger)
    # définition des Contraintes
    problème += (h1 + h2) <= 12
    problème += ((h1*2) + h2) <=16
    #définition de l'objectif
    problème += (h1*40) + (h2*30)
    print('Résultat ave PuLP')
    # On affiche le résultat
    print(LpStatus[problème.solve(PULP_CBC_CMD(msg=False))])
    #Show the final value of the optimal objective function
    print(f"Salaire total : $ {problème.objective.value()}")


if __name__ == "__main__":
    programmation_linéaire()