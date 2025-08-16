
# Programme numéro 5 du devoir de programmation linéaire P2 du cours AI-1
# Par Samira Lehlou et Michel Paquin cours 420-004-XX Groupe 12504
'''
Cette fonction appelle successivement les méthodes récursives et récursives dynamiques
Elle imprime le résultat de chacune et le temps de traitement pour les exécuter.
'''
from Programmation_dynamique import *
from Récursivité_simple import*
import time

def performance(nombre):
    #Exécution de récursivité simple
    heure_début_simple = time.perf_counter() # calcul de l'heure du début
    print('Simple: ',str(add_recursive(nombre))) # Impression du résultat du calcul simple
    heure_fin_simple = time.perf_counter() # calcul de l'heure de fin

    #Exécution de récursivité complexe
    heure_début_dynamique = time.perf_counter()
    print('Dynamique: ', str(add_recursive_mem(nombre))) #impression du résultat du calcul dynamique
    heure_fin_dynamique = time.perf_counter()

    #calcul des temps d'exécution
    runtime_simple= heure_fin_simple - heure_début_simple # calcul du temps de traitement récursif
    runtime_dynamique = heure_fin_dynamique - heure_début_dynamique # Calcul du temps réponse dynamique

    #Impression des temps de traitement
    print('simple(' + str(nombre) + f') {runtime_simple:.3f} secondes')
    print('dynamique(' + str(nombre) + f') {runtime_dynamique:.3f} secondes')

if __name__ == '__main__':
    performance(30)
