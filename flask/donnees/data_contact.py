"""Moldule contenant la classe DataContact servant à exploiter les données du fichier CSV"""
import csv

class DataContact:
    """Classequi se sert des fichiers .csv"""

    nom_fichier: str

    #va initialiser le fichier sous forme de variable
    def __init__(self) -> None:
        self.nom_fichier = "flask/donnees/data.csv"

    #sert a obtenir la liste des Users pour permettre de l'affichier sous form de tableau
    def obtenir_liste_user(self) -> list:
        liste = []
        with open(self.nom_fichier, newline='', encoding='utf-8') as fichier_csv:
            reader = csv.reader(fichier_csv, delimiter=',')
            for User in reader:
                if int(User[0]) != 0:
                    liste.append([int(User[0]),
                            (User[1]),
                            int(User[2]),
                            int(User[3])])
        return liste
        

    def generer_nouvel_identifiant(self) -> int:
        """Génère un nouvel identifiant"""

        identifiant = 1
        with open(self.nom_fichier, newline='', encoding='utf-8') as fichier_csv:
            Reader = csv.reader(fichier_csv, delimiter=',')
            for User in Reader:
                identifiant += 1
        return identifiant


    def ajouter_user(self, contact: list):
        """Ajoute un nouveau contact dans le fichier CSV."""

        contact[0] = self.generer_nouvel_identifiant()

        with open(self.nom_fichier, "a", newline='', encoding='utf-8') as fichier_csv:
            writer = csv.writer(fichier_csv, delimiter=',')
            writer.writerow(contact)





    #sert a obtenir l'identifiant du dernier user ajouter pour faire le test dans la liste d'erreur
    def obtenir_identifiant_user(self,liste):
        liste = []
        with open(self.nom_fichier, newline='', encoding='utf-8') as fichier_csv:
            reader = csv.reader(fichier_csv, delimiter=',')
            for User in reader:
                if int(User[0]) != 0:
                    liste.append(int(User[0]))
        identifiant = len(liste) - 1
        return identifiant