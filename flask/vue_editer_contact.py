"""Module contenant la génération du formulaire servant à ajouter ou modifier un conctact"""
from flask import render_template, request
from flask.views import View
from donnees.data_contact import DataContact
import string

class VueEditerContact(View):

    def dispatch_request(self, identifiant: int = 0) -> str:
        """ajoute un utilisateur.
        Si l'identifiant est « 0 », un nouvel utilisateur sera créé. 
        """

        # Initialisation
        data_contact = DataContact()
        liste_erreur = []
        contact_en_cours = [0, "", "", ""] # contact vide

        if request.method == "POST":

            # Récupérer les données
            Username = request.form["Username"].strip()
            Score = request.form["Score"].strip()
            Wave = request.form["Wave"].strip()

            # contact en cours avec les dnnées saisies
            contact_en_cours[1] =Username
            contact_en_cours[2] = Score
            contact_en_cours[3] = Wave

            # Générer les messages d'erreurs pour le nom et le prénom qui sont obligatoires.
            if len(Username) < 1:
                liste_erreur.append("Le Username est obligatoire.")
            if len(Score) < 1:
                liste_erreur.append("Le joueur doit faire 100 de score obligatoire.")
            if string.ascii_letters or string.ascii_lowercase or string.ascii_uppercase in Score:
                liste_erreur.append("Le score invalide")
            if string.ascii_letters or string.ascii_lowercase or string.ascii_uppercase in Wave:
                liste_erreur.append("le nombre de vague est invalide")


            "s'il n'y a aucune erreur, sauvegarde."
            if len(liste_erreur) == 0:
                try:
                    # ajoute le contact en cours
                    if identifiant == 0:
                        data_contact.ajouter_user(contact_en_cours)

                    # Afficher le message de confirmation
                    return render_template("fin.html", liste_message=["Score ajouté au leaderboard"])

                except:
                    liste_erreur.append("Erreur lors de le sauvegarde")


        "retourne tous les information et les message d'erreur s'y il y en as au template"
        return render_template("formulaire.html", contact=contact_en_cours, liste_message=liste_erreur)
