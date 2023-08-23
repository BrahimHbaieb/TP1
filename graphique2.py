from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QAction

class BibliothequeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 600, 300)
        self.setWindowTitle("Bibliothèque App")

        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()  # Créer un widget central pour la fenêtre
        self.setCentralWidget(self.central_widget)  # Définir le widget central

        layout = QVBoxLayout()

        menubar = self.menuBar()
        file_menu = menubar.addMenu("Bibliothèque")

        ajouter_adherent_action = QAction("Ajouter Adhérent", self)
        ajouter_adherent_action.triggered.connect(self.ajouter_adherent)
        file_menu.addAction(ajouter_adherent_action)

        enlever_adherent_action = QAction("Enlever Adhérent", self)
        enlever_adherent_action.triggered.connect(self.enlever_adherent)
        file_menu.addAction(enlever_adherent_action)

        afficher_adherents_action = QAction("Afficher Adhérents", self)
        afficher_adherents_action.triggered.connect(self.afficher_adherents)
        file_menu.addAction(afficher_adherents_action)

        ajouter_document_action = QAction("Ajouter Document", self)
        ajouter_document_action.triggered.connect(self.ajouter_document)
        file_menu.addAction(ajouter_document_action)

        enlever_document_action = QAction("Enlever Document", self)
        enlever_document_action.triggered.connect(self.enlever_document)
        file_menu.addAction(enlever_document_action)

        afficher_documents_action = QAction("Afficher Documents", self)
        afficher_documents_action.triggered.connect(self.afficher_documents)
        file_menu.addAction(afficher_documents_action)

        layout.addWidget(menubar)
        self.central_widget.setLayout(layout)

    def ajouter_adherent(self):
        pass  # Ajouter la logique pour ajouter un adhérent ici

    def enlever_adherent(self):
        pass  # Ajouter la logique pour enlever un adhérent ici

    def afficher_adherents(self):
        pass  # Ajouter la logique pour afficher les adhérents ici

    def ajouter_document(self):
        pass  # Ajouter la logique pour ajouter un document ici

    def enlever_document(self):
        pass  # Ajouter la logique pour enlever un document ici

    def afficher_documents(self):
        pass  # Ajouter la logique pour afficher les documents ici

app = QApplication([])
bibliotheque_app = BibliothequeApp()
bibliotheque_app.show()
app.exec()
