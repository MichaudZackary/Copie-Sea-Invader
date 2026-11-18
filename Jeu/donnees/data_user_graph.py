"""Moldule contenant la classe Datauser servant à exploiter les données du fichier CSV"""
import csv
# from Jeu.main import PirateInvader

class Data_user_graph:
    """Classe qui se sert des fichiers .csv"""

    nom_fichier: str

    def __init__(self, path : str) -> None:
        self.nom_fichier = path


    def create_new_id(self) -> int:
        """Génère un nouvel identifiant"""

        identifiant = 1
        with open(self.nom_fichier, newline='', encoding='utf-8') as fichier_csv:
            reader = csv.reader(fichier_csv, delimiter=',')
            for each in reader:
                identifiant += 1
        return identifiant


    def add_user(self, user : list):
        """Ajoute un nouveau user dans le fichier CSV."""

        if self.nom_fichier == "Jeu/donnees/data.csv" :
            user[0] = self.create_new_id()

            with open(self.nom_fichier, "a", newline='', encoding='utf-8') as fichier_csv:
                write = csv.writer(fichier_csv, delimiter=',')
                write.writerow(user)
        else :
            with open(self.nom_fichier, "w", newline='', encoding='utf-8') as fichier_csv:
                write = csv.writer(fichier_csv, delimiter=',')
                write.writerow("PD")
                for each in user :
                    
                    write.writerow(each)
                    