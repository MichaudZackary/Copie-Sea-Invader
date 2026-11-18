from entity import Entity
from pgzero.builtins import Actor
import random #si pas utiliser on enlève
from bullet import Bullet

class Player(Entity) :
    
    
    vie : int
    vitesse : int
    image : str

    def __init__(self):
        """"
        Constructeur du bateau
        
        """
        self.image="player_dg.png"
        super().__init__(self.image)
        self.acteur.x = 960
        self.acteur.y = 900
        self.vie = 3
        self.vitesse = 10

    def deplacer(self, keyboard) :
        # super().deplacer() pas sur pour ça aussi
        """"
        Déplacement du bateau du joueur
        
        """
        if keyboard.A and self.acteur.x > 120 :
            self.acteur.x -= self.vitesse
            self.acteur.image = "player_dg.png"
        elif keyboard.D and self.acteur.x < 1800 :
            self.acteur.x += self.vitesse
            self.acteur.image = "player_gd.png"
        

    def collision(self, bulletenemy : Actor) :
        
        """""
        Détection de collision entre le bateau et un boulet de cannon venant d'un enemie

        Args:
            bouletenemy (Boulet): boulet avec lequel on regarde si il y a une collision

        Returns:
            bool: vrai si il y a un collision
                faux s'y il n'y a pas de collision

        """""
        if super().collision(bulletenemy) :
            self.vie -= 1
            return True
        return False

        