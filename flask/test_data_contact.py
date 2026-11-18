"""Module contenant les tests programmés de ValidateurDataContact"""
import unittest
from donnees.data_contact import DataContact
from vue_editer_contact import VueEditerContact


class TestValidateurDataContact(unittest.TestCase):
    """Classe contenant des tests de DataContact."""
    
    def test_crud(self):
        """Teste la classe ValidateurDataContact"""
        
        "initialise DataContact"
        data_contact = DataContact()
        
        "#test l'ajout de nouveau users"
        nouveau_user = [0, "Testeur", 10, 696969]
        data_contact.ajouter_user(nouveau_user)
        
            #Obtention du nouveau contact
        contact_user = data_contact.obtenir_liste_user()[-1]
        
            #Assertions
        self.assertEqual(nouveau_user[0], contact_user[0])
        self.assertEqual(nouveau_user[1], contact_user[1])
        self.assertEqual(nouveau_user[2], contact_user[2])
        self.assertEqual(nouveau_user[3], contact_user[3])
    



    #test si le dernier identifiant rajouter a la liste 
    def liste_erreur(self):
        """Teste si la liste d'erreur fonctionne"""
        
        "initialise DataContact"
        data_contact = DataContact()
        
        "#test l'ajout de nouveau users"
        nouveau_user = [0, "Testeur", "vague10", 696969]
        data_contact.ajouter_user(nouveau_user)
        
        vue_editer_contact = VueEditerContact()
        identifiant = data_contact.obtenir_identifiant_user(nouveau_user)
        liste = vue_editer_contact.dispatch_request(identifiant)
        if len(liste) >=1 :
            print (f"il y a  ${len(liste)} d'erreur pour le dernier utilisateur de la liste. ")
    