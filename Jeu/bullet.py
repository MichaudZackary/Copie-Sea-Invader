from entity import Entity


class Bullet(Entity) :
    """ 
    Classe qui s'occuper de créer les projectile selon le tireur
    """
    vitesse : int
    
    def __init__(self, image : str, posx : int, posy : int):
        super().__init__(image)
        self.vitesse = 10
        self.acteur.x = posx
        if self.acteur.image == "bullet_player.png" :
            self.acteur.y = posy - 40
        elif self.acteur.image == "bullet_enemy.png" :
            self.acteur.y = posy + 40
        elif self.acteur.image == "wave.png" or self.acteur.image == "wave_blood.png" :
            self.acteur.y = posy
    def deplacer(self):
        """
        Déplace les balles du jouer/ennemy et les vagues du boss
        """
        
        if self.acteur.image == "bullet_player.png" :
            self.acteur.y -= self.vitesse
        
        elif self.acteur.image == "bullet_enemy.png" :
            self.acteur.y += self.vitesse   

        elif self.acteur.image == "wave.png" or self.acteur.image == "wave_blood.png" :
            self.acteur.y += self.vitesse/2
    
    def collision(self,bullet):
        return super().collision(bullet)