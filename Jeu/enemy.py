from entity import Entity 

class Enemy(Entity) :
    """"constructeur d'un enemie
        Appeler le constructeur de la classe parent en lui passant en paramètre le nom d'une image de votre choix.
        L'image changera selon le type d'enemie.
        Positionner l'acteur en appelant le dictionaire.
        """
    vie : int

    def __init__(self,image,posx,posy):
        super().__init__(image)
        self.acteur.x = posx
        self.acteur.y = posy
        self.vie = 2
        

    def collision(self,bullet) :
        return super().collision(bullet)





