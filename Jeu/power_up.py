from entity import Entity

class Power_up(Entity) :
    """ 
    Classe qui s'occuper de créer les power up
    """
    vitesse : int
    
    def __init__(self, image : str, posx : int, posy : int):
        super().__init__(image)
        self.acteur.x = posx
        self.acteur.y = posy
        self.vitesse = 5

    def deplacer(self):
            self.acteur.y += self.vitesse

    def collision(self,player):
        return super().collision(player)