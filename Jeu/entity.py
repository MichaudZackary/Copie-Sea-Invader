from abc import ABC
from pgzero.builtins import Actor

# Classe mère de tous nos acteurs
class Entity(ABC) :
    acteur : Actor
    def __init__(self,image):
        self.acteur = Actor(image)

    def collision(self,bullet : Actor) :
        return self.acteur.colliderect(bullet)
