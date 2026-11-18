"""Module contenant la génération de la liste des contacts"""
from flask import render_template
from flask.views import View
from donnees.data_contact import DataContact

class VueListeContact(View):
    """Classe représentant la page qui affiche la liste des contacts"""

    def dispatch_request(self) -> str:
        """Affiche les contacts
        """

        data_contact = DataContact()
        Users = data_contact.obtenir_liste_user()
        print(Users)

        """ Retourne les pages selon la taille de la liste
        """
        if len(Users) == 0 :
            return render_template("vide.html")
        else:
            return render_template("liste_contact.html", liste_contacts=Users)
        