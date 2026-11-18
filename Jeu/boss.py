from enemy import Enemy
import random

class Boss(Enemy):
   
    vie : int
    
    def boss_enemie(self,image):
        """Class qui crée le boss après chaque 5 vague :
        """
        super().__init__(image,960,-500)
        self.vie = 100
    
    def move_boss_projectile(self):
        """
        Déplace le boss  
        """
        pos = random.randint(200,1720)
        self.acteur.x = pos

    def boss_projectile(self,list) :
        pass