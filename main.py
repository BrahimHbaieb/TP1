
from gestion_biblio import *
from graphique import create_graphical_interface


# Fonction pour afficher le menu principal
def afficher_menu():
    print("*************************************************************")
    print("*         Bienvenue à votre bibliothèque                    *")
    print("*                     Faites un choix :                     *")
    print("*************************************************************")
    print("*    1       Ajouter adhérent                               *")
    print("*    2       Supprimer adhérent                             *")
    print("*    3       Afficher tous les adhérents                    *")
    print("*    4       Ajouter Document                               *")
    print("*    5       Supprimer Document                             *")
    print("*    6       Afficher tous les Documents                    *")
    print("*    7       Ajouter Emprunt                                *")
    print("*    8       Retour d’un Emprunt                            *")
    print("*    9       Afficher tous les Emprunts                     *")
    print("*    Q       Quitter                                        *")
    print("*************************************************************")

# Fonction pour démarrer la boucle du menu
def demarrer (bibliotheque):
    while True:
        afficher_menu()
        choix = input("Choisissez une action : ")

        if choix.upper() == "Q":
            print("Au revoir !")
            break

        if choix in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if choix == "1":
                bibliotheque.ajouter_adherent()
            elif choix == "2":
                bibliotheque.enlever_adherent()
            elif choix == "3":
                bibliotheque.afficher_adherents()
            elif choix == "4":
                bibliotheque.ajouter_document()
            elif choix == "5":
                bibliotheque.enlever_document()
            elif choix == "6":
                bibliotheque.afficher_documents()
            elif choix == "7":
                bibliotheque.ajouter_emprunt()
            elif choix == "8":
                bibliotheque.retourner_livre()
            elif choix == "9":
                bibliotheque.afficher_emprunts()
        else:
            print("Choix erroné! Veuillez entrer un choix valide.")


bibliotheque = Bibliotheque()  # Créer une instance de la bibliothèque

# Boucle pour choisir entre l'interface en ligne de commande et l'interface graphique, ou quitter
while True:
    interface_choice = input("Choisissez une interface (T pour terminal, G pour graphique, Q pour quitter) : ")

    if interface_choice.upper() == "T":
        demarrer(bibliotheque) # Démarrage de l'interface en ligne de commande
    elif interface_choice.upper() == "G":
        create_graphical_interface(bibliotheque)  # Démarrage de l'interface graphique
    elif interface_choice.upper() == "Q":
        print("Au revoir !")
        break
    else:
        print("Choix erroné! Veuillez entrer T, G ou Q.")