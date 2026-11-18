
"importation de module"
from flask import Flask
from vue_editer_contact import VueEditerContact
from vue_liste_contact import VueListeContact

app = Flask(__name__)

#L'url de base qui sert a voir le Scoreboard
app.add_url_rule('/', view_func=VueListeContact.as_view("afficher_liste_contact"))

# Ajout d'un contact manuellement
app.add_url_rule(
    "/ajouter/",
    view_func=VueEditerContact.as_view("ajouter"),
    methods=["GET", "POST"],
)
