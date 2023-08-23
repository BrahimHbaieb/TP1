from PyQt6.QtWidgets import *
from classes import *
from gestion_biblio import *

# Définition de la classe pour l'application graphique
class GestionBibliothequeApp(QWidget):
    def __init__(self, bibliotheque):
        super().__init__()
        self.bibliotheque = bibliotheque
        self.setWindowTitle("Gestion Bibliotheque")
        self.setGeometry(100, 100, 1000, 400)

        self.layout = QVBoxLayout()

        self.label = QLabel()
        self.layout.addWidget(self.label)

        # différent bouton de l'interface
        self.btn_ajouter_A = QPushButton("Ajouter adhérent")
        self.btn_ajouter_A.clicked.connect(self.ajouter_adherent)
        self.layout.addWidget(self.btn_ajouter_A)

        self.btn_supprimer_A = QPushButton("Supprimer adhérent")
        self.btn_supprimer_A.clicked.connect(self.supprimer_adherent)
        self.layout.addWidget(self.btn_supprimer_A)

        self.btn_afficher_A = QPushButton("Afficher tous les adhérents")
        self.btn_afficher_A.clicked.connect(self.afficher_adherents)
        self.layout.addWidget(self.btn_afficher_A)

        self.btn_ajouter_D = QPushButton("Ajouter document")
        self.btn_ajouter_D.clicked.connect(self.ajouter_document)
        self.layout.addWidget(self.btn_ajouter_D)

        self.btn_supprimer_D = QPushButton("Supprimer document")
        self.btn_supprimer_D.clicked.connect(self.supprimer_document)
        self.layout.addWidget(self.btn_supprimer_D)

        self.btn_afficher_D = QPushButton("Afficher tous les documents")
        self.btn_afficher_D.clicked.connect(self.afficher_documents)
        self.layout.addWidget(self.btn_afficher_D)

        self.btn_ajouter_E = QPushButton("Ajouter emprunt")
        self.btn_ajouter_E.clicked.connect(self.ajouter_emprunt)
        self.layout.addWidget(self.btn_ajouter_E)

        self.btn_retourner_E = QPushButton("Retour emprunt")
        self.btn_retourner_E.clicked.connect(self.retourner_emprunt)
        self.layout.addWidget(self.btn_retourner_E)

        self.btn_afficher_E = QPushButton("Afficher tous les emprunts")
        self.btn_afficher_E.clicked.connect(self.afficher_emprunts)
        self.layout.addWidget(self.btn_afficher_E)

        self.setLayout(self.layout)

        self.charger_donnees()  # Charger les données une seule fois au début

    # Methode pour charger les donnees
    def charger_donnees(self):
        self.bibliotheque.charger_adherents("Adherents.txt")
        self.bibliotheque.charger_documents("Biblio.txt")
        self.bibliotheque.charger_emprunts("Emprunts.txt")

    def ajouter_adherent(self):
        nom, ok_nom = QInputDialog.getText(self, "Ajouter adhérent", "Nom de l'adhérent :")
        prenom, ok_prenom = QInputDialog.getText(self, "Ajouter adhérent", "Prénom de l'adhérent :")

        if ok_nom and ok_prenom:
            adherent = Adherent(nom, prenom)
            self.bibliotheque.adherents.append(adherent)

            with open("Adherents.txt", "a") as f:
                f.write(f"{adherent.nom},{adherent.prenom}\n")

            self.label.setText(f"{prenom} {nom} a été ajouté comme adhérent.")

    def supprimer_adherent(self):
        nom, ok_nom = QInputDialog.getText(self, "Supprimer adhérent", "Nom de l'adhérent à supprimer :")
        prenom, ok_prenom = QInputDialog.getText(self, "Supprimer adhérent", "Prénom de l'adhérent à supprimer :")

        if ok_nom and ok_prenom:
            adherent_trouve = None

            for adherent in self.bibliotheque.adherents:
                if adherent.nom == nom and adherent.prenom == prenom:
                    adherent_trouve = adherent
                    break

            if adherent_trouve:
                self.bibliotheque.adherents.remove(adherent_trouve)

                with open("Adherents.txt", "r") as f:
                    lines = f.readlines()

                with open("Adherents.txt", "w") as f:
                    adh_supprime = False
                    for line in lines:
                        line_nom, line_prenom = line.strip().split(",")
                        if line_nom != nom or line_prenom != prenom:
                            f.write(line)
                        else:
                            adh_supprime = True

                    if adh_supprime:
                        self.label.setText(f"{prenom} {nom} a été supprimé comme adhérent.")
                    else:
                        self.label.setText(f"L'adhérent {prenom} {nom} n'a pas été trouvé.")
            else:
                self.label.setText(f"L'adhérent {prenom} {nom} n'a pas été trouvé.")

    def afficher_adherents(self):
        adherent_text = "Liste des adhérents :\n"

        if not self.bibliotheque.adherents:
            adherent_text = "Aucun adhérent enregistré."
        else:
            for adherent in self.bibliotheque.adherents:
                adherent_text += f"{adherent.prenom} {adherent.nom}\n"

        self.label.setText(adherent_text)

    def ajouter_document(self):
        types_documents = ["Livre", "Bande Dessinée", "Dictionnaire", "Journal"]
        choix, ok = QInputDialog.getItem(self, "Ajouter document", "Choisissez le type de document à ajouter:",
                                         types_documents)

        if ok:
            if choix == "Livre":
                titre, ok_titre = QInputDialog.getText(self, "Ajouter Livre", "Titre du livre :")
                auteur, ok_auteur = QInputDialog.getText(self, "Ajouter Livre", "Auteur du livre :")
                if ok_titre and ok_auteur:
                    disponible, ok_disponible = QInputDialog.getItem(self, "Ajouter Livre",
                                                                     "Le livre est-il disponible ?", ["True", "False"])
                    if ok_disponible:
                        document = Livre(titre, auteur, disponible)
                        self.bibliotheque.documents.append(document)
                        with open("Biblio.txt", "a") as f:
                            f.write(f"L,{document.titre},{document.auteur},{document.disponible}\n")
                        self.label.setText(f"Le livre '{titre}' a été ajouté.")

            elif choix == "Bande Dessinée":
                titre, ok_titre = QInputDialog.getText(self, "Ajouter Bande Dessinée", "Titre de la bande dessinée :")
                auteur, ok_auteur = QInputDialog.getText(self, "Ajouter Bande Dessinée",
                                                         "Auteur de la bande dessinée :")
                dessinateur, ok_dessinateur = QInputDialog.getText(self, "Ajouter Bande Dessinée",
                                                                   "Dessinateur de la bande dessinée :")
                if ok_titre and ok_auteur and ok_dessinateur:
                    document = BandeDessinee(titre, auteur, dessinateur)
                    self.bibliotheque.documents.append(document)
                    with open("Biblio.txt", "a") as f:
                        f.write(f"BD,{document.titre},{document.auteur},{document.dessinateur}\n")
                    self.label.setText(f"La bande dessinée '{titre}' a été ajoutée.")

            elif choix == "Dictionnaire":
                titre, ok_titre = QInputDialog.getText(self, "Ajouter Dictionnaire", "Titre du dictionnaire :")
                auteur, ok_auteur = QInputDialog.getText(self, "Ajouter Dictionnaire", "Auteur du dictionnaire :")
                if ok_titre and ok_auteur:
                    document = Dictionnaire(titre, auteur)
                    self.bibliotheque.documents.append(document)
                    with open("Biblio.txt", "a") as f:
                        f.write(f"D,{document.titre},{document.auteur}\n")
                    self.label.setText(f"Le dictionnaire '{titre}' a été ajouté.")

            elif choix == "Journal":
                titre, ok_titre = QInputDialog.getText(self, "Ajouter Journal", "Titre du journal :")
                date_parution, ok_date = QInputDialog.getText(self, "Ajouter Journal",
                                                              "Date de parution du journal (AAAA-MM-JJ) :")
                if ok_titre and ok_date:
                    document = Journal(titre, date_parution)
                    self.bibliotheque.documents.append(document)
                    with open("Biblio.txt", "a") as f:
                        f.write(f"J,{document.titre},{document.date_parution}\n")
                    self.label.setText(f"Le journal '{titre}' a été ajouté.")

    def supprimer_document(self):
        titre, ok = QInputDialog.getText(self, "Supprimer document", "Titre du document à supprimer :")

        if ok:
            document_to_remove = None
            with open("Biblio.txt", "r") as f:
                lines = f.readlines()

            with open("Biblio.txt", "w") as f:
                for line in lines:
                    data = line.strip().split(",")
                    if data[1] == titre:
                        document_to_remove = line
                    else:
                        f.write(line)

            if document_to_remove:
                for document in self.bibliotheque.documents:
                    if document.titre == titre:
                        self.bibliotheque.documents.remove(document)
                        break

                self.label.setText(f"Le document '{titre}' a été supprimé du fichier et de la bibliothèque.")
            else:
                self.label.setText(f"Le document '{titre}' n'a pas été trouvé.")

    def afficher_documents(self):

        with open("Biblio.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                document_text = "Aucun document enregistré."
            else:
                document_text = "Liste des documents :\n"
                for line in lines:
                    data = line.strip().split(",")
                    if data[0] == "L":
                        document_type = "Livre"
                        if data[3] == "False":
                            dispo = "Non Disponible"
                        else:
                            dispo = " Disponible"
                    elif data[0] == "BD":
                        document_type = "Bande Dessinée"
                        dispo = ""
                    elif data[0] == "D":
                        document_type = "Dictionnaire"
                        dispo = ""
                    elif data[0] == "J":
                        document_type = "Journal"
                        dispo = ""
                    document_text += f"{document_type} : {data[1]} - {data[2]} - {dispo}\n"
            self.label.setText(document_text)

    def ajouter_emprunt(self):
        nom, ok_nom = QInputDialog.getText(self, "Ajouter emprunt", "Nom de l'adhérent :")
        if ok_nom:
            prenom, ok_prenom = QInputDialog.getText(self, "Ajouter emprunt", "Prénom de l'adhérent :")
            if ok_prenom:
                # Créer l'adhérent
                adherent = Adherent(nom, prenom)

                # Saisir le titre du livre
                livre, ok_livre = QInputDialog.getText(self, "Ajouter emprunt", "Titre du livre :")

                # Vérifier si le titre du livre est valide
                if ok_livre:
                    document_trouve = None
                    livres_trouves = []

                    # Ouvrir le fichier pour chercher le document
                    with open("Biblio.txt", "r") as f:
                        for line in f:
                            data = line.strip().split(",")
                            if data[0] == "L" and data[1] == livre:
                                document_type = "Livre"
                                if data[3] == "True":
                                    dispo = "Disponible"
                                    disponible = True
                                else:
                                    dispo = "Non Disponible"
                                    disponible = False
                                livres_trouves.append(Livre(data[1], data[2], disponible))

                    if not livres_trouves:
                        self.label.setText(f"Le livre '{livre}' n'existe pas dans la bibliothèque.")
                        return

                    # Si un ou plusieurs livres ont été trouvés, demander à l'utilisateur de choisir
                    if len(livres_trouves) == 1:
                        document_trouve = livres_trouves[0]
                    else:
                        livre_titles = [livre.titre for livre in livres_trouves]
                        livre, ok_livre = QInputDialog.getItem(self, "Ajouter emprunt", "Choisissez le livre :",
                                                               livre_titles)

                        if ok_livre:
                            for livre_trouve in livres_trouves:
                                if livre_trouve.titre == livre:
                                    document_trouve = livre_trouve
                                    break

                    if document_trouve and document_trouve.disponible:
                        date_emprunt = datetime.now().date()
                        emprunt = Emprunt(adherent, document_trouve, date_emprunt)
                        document_trouve.disponible = False

                        # Mettre à jour les fichiers
                        with open("Emprunts.txt", "a") as f:
                            f.write(
                                f"{adherent.prenom},{adherent.nom},{document_trouve.titre},{emprunt.date_emprunt}\n")

                        with open("Biblio.txt", "r") as f:
                            lines = f.readlines()

                        with open("Biblio.txt", "w") as f:
                            for line in lines:
                                data = line.strip().split(",")
                                if data[0] == "L" and data[1] == livre:
                                    line = f"L,{data[1]},{data[2]},{False}\n"  # Mettre à jour la disponibilité
                                f.write(line)

                        self.bibliotheque.emprunts.append(emprunt)
                        self.label.setText(
                            f"L'emprunt du document '{document_trouve.titre}' par {adherent.prenom} {adherent.nom} a été enregistré.")
                    else:
                        self.label.setText(f"Le document '{livre}' n'est pas disponible pour l'emprunt.")

    def retourner_emprunt(self):
        titre_document, ok_titre = QInputDialog.getText(self, "Retourner emprunt", "Titre du document à retourner :")
        if ok_titre:
            with open("Emprunts.txt", "r") as f:
                emprunt_lines = f.readlines()

            document_emprunte = False
            date_retour = None

            with open("Emprunts.txt", "w") as f:
                for line in emprunt_lines:
                    data = line.strip().split(",")
                    if data[2] == titre_document:
                        document_emprunte = True
                        date_retour = datetime.now().date()
                        line = f"{data[0]},{data[1]},{data[2]},{data[3]},{date_retour}\n"
                    f.write(line)

            if document_emprunte:
                with open("Biblio.txt", "r") as f:
                    biblio_lines = f.readlines()

                with open("Biblio.txt", "w") as f:
                    for line in biblio_lines:
                        data = line.strip().split(",")
                        if data[1] == titre_document:
                            data[3] = "True"  # Mettre à "True" le statut de disponibilité
                        f.write(",".join(data) + "\n")

                self.label.setText(f"Le document '{titre_document}' a été retourné.")
            else:
                self.label.setText(f"Le document '{titre_document}' n'a pas été emprunté ou a déjà été retourné.")

    def afficher_emprunts(self):
        if not self.bibliotheque.emprunts:
            self.label.setText("Aucun emprunt enregistré.")
        else:
            emprunt_text = "Liste des emprunts :\n"
            for emprunt in self.bibliotheque.emprunts:
                adherent = f"{emprunt.adherent.prenom} {emprunt.adherent.nom}"
                document = emprunt.document.titre
                date_emprunt = emprunt.date_emprunt.strftime("%Y-%m-%d")


                if emprunt.date_retour == None:
                    date_retour = "Non retourné"
                else:
                    date_retour = emprunt.date_retour.strftime ("%Y-%m-%d")

                emprunt_text += f"Adhérent : {adherent}\n"
                emprunt_text += f"Document emprunté : {document}\n"
                emprunt_text += f"Date d'emprunt : {date_emprunt}\n"
                emprunt_text += f"Date de retour : {date_retour}\n"
                emprunt_text += "=================================\n"

            self.label.setText(emprunt_text)

# Fonction pour créer l'interface graphique
def create_graphical_interface(bibliotheque):
    app = QApplication([])
    fen = GestionBibliothequeApp(bibliotheque)
    fen.show()
    app.exec()
