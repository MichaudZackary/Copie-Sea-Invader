import random
import pgzrun 
import os
import csv
from pgzero.builtins import Actor

# Importation des classes pour le graphique et le tkinter
from donnees.data_user_graph import Data_user_graph
from form import Form


# Importation des classes pour le jeu 
from bullet import Bullet 
from enemy import Enemy
from player import Player
from power_up import Power_up 
from health import Health
from boss import Boss
from dic import dictenemy



WIDTH = 1920
HEIGHT = 1000

class PirateInvader() :
    # Variable de classe acteur
    player : Player

    # Variable de classe list
    position_enemy : list
    list_ennemy : list[Enemy]
    list_bullet_player : list[Bullet]
    list_bullet_ennemy : list[Bullet]
    list_power_up : list[Power_up]
    list_hp : list[Health]
    list_projectile_boss : list[Bullet]
    list_graph : list[list[int]]
    list_game : list

    # Variable de classe int
    counter : int
    counter_atk_spd : int
    counter_speed : int
    attack_speed : int
    score : int
    counter_wave : int
    direction_boss_x : int
    direction_boss_y : int
    nb_enemy_dead : int
    nb_power : int
    
    # Variable de classe string
    background : str
    
    # Variable de classe bool
    game_over : bool
    boss_move : bool
    boss_hp_half : bool
    first_half_hp : bool
    tkinter : bool

    # Variable de classe tkinter
    form : Form

    
    
    def __init__(self):
        
        # Initialisation des acteur
        self.player = Player()
        self.list_hp = [Health(), Health(), Health()]
       
        # Initialisation des variable listes
        self.list_ennemy = []
        self.list_bullet_ennemy = []
        self.list_bullet_player = []
        self.list_power_up = []
        self.list_projectile_boss = []
        self.position_enemy = []
        self.list_game = []
        self.list_graph = [[0,0]]
        
        # Initialisation des variable string
        self.background = "sea.jpeg"

        # Initialisation des variable int
        self.nb_enemy_dead = 0
        self.counter = 0
        self.counter_atk_spd = 2000
        self.counter_speed = 2000
        self.attack_speed = 20
        self.score = 0
        self.counter_wave = 0
        self.direction_boss_x = 7
        self.direction_boss_y = 3
        self.nb_power = 0
        
        # Music de fond pour le jeu (vien de assasin creed IV black flague)
        music.play("music.wav")

        # Initialisation des variable bool
        self.boss_move = True
        self.boss_hp_half = False
        self.first_half_hp = False
        self.tkinter = True 
        self.game_over = False

    def draw(self,screen) :
        """
            Dessine tous nos acteur
        """
        
        # Efface l'écran
        screen.clear()
        screen.blit(self.background, (0, 0))
        
        # Dessine le joueur
        self.player.acteur.draw()

        # Dessine les different projectile
        for bullet in self.list_bullet_player :
            bullet.acteur.draw()
        for bullet in self.list_bullet_ennemy :
            bullet.acteur.draw()
        for wave in self.list_projectile_boss :
            wave.acteur.draw()

        # Dessine les bonus
        for pow in self.list_power_up :
            pow.acteur.draw()

        # Dessine les ennemies et le boss
        for ennemy in self.list_ennemy:
            ennemy.acteur.draw()
        
        # Dessine les coeurs
        x = 30
        for health in self.list_hp : 
            health.acteur.x = x 
            health.acteur.y = 30
            health.acteur.draw()
            x += 55

        # Dessine les differents textes sur l'écran
        screen.draw.text(f"Score : {str(self.score)}",(10,60), color = "black", fontsize = 50, )
        screen.draw.text(f"Wave : {str(self.counter_wave)}",(1820,20), color = "black", fontsize = 30)
        if self.counter_speed < 2000 :
            screen.draw.text(f"Speed : {self.counter_speed} / 2000" ,(10,90), color = "black", fontsize = 50, )
        if self.counter_atk_spd < 2000 :
            screen.draw.text(f"Atk spd : {str(self.counter_atk_spd)} /2000",(10,120), color = "black", fontsize = 50, )
        if self.game_over :
            screen.draw.text(f"GAME OVER",(WIDTH/2 - 200,300), color = "black", fontsize = 100, )
    
    def update(self,keyboard): 
        """

        Args:
            fait tous nos update pour tous les acteurs

        """
        # Regarde si la partie est finis 
        if self.game_over :
            
            # Se fait seulement une fois a la fin et gère tous ce qui est a faire a la fin 
            if self.tkinter :
                sounds.death.play()
                # Ouvre une page Tkinter pour rentrer le nom du joueur et ensuite l'enregistre dans data.csv
                self.form = Form(self.score, self.counter_wave)
                self.list_game = self.form.player_input()
                
                # Ajouter les donner au fichier data_graph.csv et crée le graphique
                Data_user_graph.add_user(Data_user_graph("Jeu/donnees/data.csv"),self.list_game,)
                Data_user_graph.add_user(Data_user_graph("Jeu/graphs/data_graph.csv"),self.list_graph,)
                self.tkinter = False
            return
        
        if len(self.list_ennemy) <= 0 :
            """
            crée des ennemy par rapport à nos position dans le dictionnaire et le boss
            """
            
            # Augmente le conteur de vague
            self.counter_wave += 1

            # Si la vague est divisible par 5 un boss apparait a la place des ennemies
            if self.counter_wave % 5 == 0 :

                # Change le boss si le fond est différent
                if self.background == "sea.jpeg":
                    image = "boss.png"
                elif self.background == "blood_sea.png" :
                    image = "blood_boss.png"
                # Crée le boss
                self.list_ennemy.append(Boss(image,960,-100))
                self.list_ennemy[0].vie = 200
            
            #Crée les ennemies par rapport aux possitions déja établie dans le dictionnaire
            else:    
                x = 0
                y = random.randint(0,3)
                for pos in dictenemy[y]["pos"] :
                    # une change sur 5 de créé un ennemy different qui a 2 pv au lieu de 1 (max de 5) 
                    if random.randint(0,4) == 1 and x < 5 :
                        image = "enemy_gros.png"
                        x += 1
                    else : 
                        image = "enemy_petit"
                    self.list_ennemy.append(Enemy(image,pos[0],pos[1]))

        # Augmente le conteur pour tirer
        if self.counter < self.attack_speed :
            self.counter += 1

        # Augmente le conteur pour le power-Up de vitesse d'attack
        if self.counter_atk_spd < 2000 :
            self.counter_atk_spd += 1
            if self.counter_atk_spd == 2000 :
                self.attack_speed = 20

        # Augmente le conteur pour le power-Up de vitesse  
        if self.counter_speed < 2000 :
            self.counter_speed += 1
            if self.counter_speed == 2000 :
                self.player.vitesse

        # Deplace le joueur selon la touche enfoncer
        self.player.deplacer(keyboard)
                    
        # Tire un projectile du joueur si le conteur est au bon nombre et que la barre espace est enfonceé
        if keyboard.space and self.counter == self.attack_speed :
            self.list_bullet_player.append(Bullet("bullet_player.png", self.player.acteur.x, self.player.acteur.y))
            self.counter = 0

        
        for bullet in self.list_bullet_ennemy :
            """
                Regarde si un collision a lieu entre les balle des ennemy et le joueur

                si oui la vie du joueur diminue et la balle est retiré
                et si la vie du joeur arrive à zero la partie est finie
                """

            if self.player.collision(bullet.acteur) :
                self.list_bullet_ennemy.remove(bullet)
                self.list_hp.pop(len(self.list_hp) - 1)
                sounds.ack.play()
                if self.player.vie <= 0 :
                    self.game_over = True

            elif bullet.acteur.y >= HEIGHT : 
                self.list_bullet_ennemy.remove(bullet)
        

        for bullet in self.list_bullet_player :     
            for ennemy in self.list_ennemy :
                """
                
                Regarde si un collision a lieu entre les balle du joueur et les ennemy

                si oui le score augment et l'ennemy et la balle est suprimer
                """
                try :    
                    if ennemy.collision(bullet.acteur):
                        self.list_bullet_player.remove(bullet)
                        
                        # Tous les ennemies commence avec 2 PV et selon leur image le nombre de pvc diminue soit de 1 ou 2 
                        if ennemy.acteur.image == "enemy_gros.png" :
                            ennemy.vie -= 1
                        else :    
                            ennemy.vie -= 2
                        
                        # Enlève l'ennemie si c'est PV ateind 0  et augmente le score et le conteur d'ennemie mort
                        if ennemy.vie <= 0 :
                            self.list_ennemy.remove(ennemy)
                            self.score += 100
                            self.nb_enemy_dead += 1
                            
                            # Si l'ennemie est le boss (représenté par un bool qui change durant le boss fight) fait ce code
                            if self.boss_hp_half :
                                
                                # Quand le boss meurt remet les variables à leurt condition de base
                                self.boss_hp_half = False
                                self.boss_move = True
                                self.direction_boss_y = 3
                                
                                # Change le theme à sang ou normale
                                if self.background == "sea.jpeg" :
                                    self.background = "blood_sea.png"
                                else :
                                    self.background = "sea.jpeg"
                            # Quand un ennemy meurt il y a une chance sur dix qu'un bonus apparaise
                            if random.randint(1,10) == 1 :
                                self.list_power_up.append(Power_up(random.choice(["power_up_atk_speed.png", "power_up_heal.png", "power_up_speed.png"]),ennemy.acteur.x,ennemy.acteur.y))
                                
                                # Rajoute des information à la liste utilisé pour faire le graphique
                                self.nb_power += 1
                                self.list_graph.append([self.nb_power,self.nb_enemy_dead])
                except :
                    pass
        #Déplace les balles du joueurs
        for bullet in self.list_bullet_player :
    
            bullet.deplacer()
            if bullet.acteur.y < 0 :
                self.list_bullet_player.remove(bullet)    
        
        # Déplace les balles des ennemy
        for bullet in self.list_bullet_ennemy :
            bullet.deplacer()
            if bullet.acteur.y > HEIGHT  :
                self.list_bullet_ennemy.remove(bullet)

        for pow in self.list_power_up :
            """
            déplace et regarde si une collision a lieu avec un power-Up et le joueur 

            si une collision a lieux soit le joeur a une vie en plus, il attack plus vite ou il ce déplace plus vite 
            """
            pow.deplacer()
            if pow.collision(self.player.acteur) :
                match pow.acteur.image :
                    
                    #Bonus de regeneration
                    case  "power_up_heal.png" :
                        if self.player.vie < 3 :
                            self.player.vie += 1
                            self.list_hp.append(Health())
                        sounds.heal.play()
                    
                    #Bonus vitesse d'attaque
                    case "power_up_atk_speed.png":
                        self.attack_speed = 10
                        self.counter_atk_spd = 0
                        self.counter = self.counter % 2
                        sounds.attack.play()
                    
                    #Bonus vitesse
                    case "power_up_speed.png":  
                        self.player.vitesse = 15
                        self.counter_speed = 0
                        sounds.speed.play()
                
                self.list_power_up.remove(pow)

        # Fait tiré les ennemy aléatoirement
        for ennemy in self.list_ennemy :
            if random.randint(0,500) == 50 :
                self.list_bullet_ennemy.append(Bullet("bullet_enemy.png", ennemy.acteur.x, ennemy.acteur.y))

        # Déplace les vagues et regarde si des collisions avec le joueur est fait
        for wave in self.list_projectile_boss :
            wave.deplacer()
            if wave.collision(self.player.acteur) :
                self.list_projectile_boss.remove(wave)
                self.list_hp.pop(len(self.list_hp) - 1)
                self.player.vie -= 1
                if self.player.vie <= 0 :
                    self.game_over = True
            if wave.acteur.y >= HEIGHT + 500 or not self.boss_hp_half :
                self.list_projectile_boss.remove(wave)
        
        # Déplace le boss 
        if len(self.list_ennemy) == 1 :
   
            if self.list_ennemy[0].acteur.image == "boss.png" or self.list_ennemy[0].acteur.image == "blood_boss.png":
                
                # Regarde si le boss à moin de 100 PV
                if self.list_ennemy[0].vie <= 100 and not self.boss_hp_half :
                    self.boss_hp_half = True
                
                if not self.boss_hp_half :

                    # Descend le boss a la bonne hauteur
                    if self.list_ennemy[0].acteur.y <= -200 :
                        self.list_ennemy[0].acteur.y = -100
                    if self.boss_move :
                        if self.list_ennemy[0].acteur.y < 400  :
                            self.list_ennemy[0].acteur.y += self.direction_boss_y
                        else :
                            self.boss_move = False

                    # Moveset du boss
                    if not self.boss_move  : 
                        
                        # Déplacement en X du boss
                        if self.list_ennemy[0].acteur.x <= 300 or self.list_ennemy[0].acteur.x >= 1600 :
                            self.direction_boss_x = -self.direction_boss_x
                        self.list_ennemy[0].acteur.x += self.direction_boss_x
                        
                        # Déplacement en Y du boss
                        if self.list_ennemy[0].acteur.y <= 300 or self.list_ennemy[0].acteur.y >= 500 :
                            self.direction_boss_y = -self.direction_boss_y
                        self.list_ennemy[0].acteur.y += self.direction_boss_y
                else :
                    
                    # Attaque spécial du boss
                    if len(self.list_projectile_boss) <= 0 :
                        done = False
                        posx = 0 
                        
                        # Choisit la bonne image de vague
                        if self.background == "sea.jpeg" :
                            image = "wave.png"
                        else :
                            image = "wave_blood.png"
                        
                        # Choisit aléatoirement une vague pour etre vidre pour que le joueur puisse esquiver l'attaque
                        while len(self.list_projectile_boss) < 5 :
                            x =  random.randint(1,3)
                            if x == 1 and not done or len(self.list_projectile_boss) == 4 and not done :
                                done = True
                                if posx == 0 :
                                    self.list_ennemy[0].acteur.x = posx + 100
                                else :
                                    self.list_ennemy[0].acteur.x = posx
                            
                            else :
                                self.list_projectile_boss.append(Bullet(image,posx,-100))
                            posx += 400
# Initialisation
game = PirateInvader()



def draw():
    game.draw(screen)

def update():
    game.update(keyboard)

os.environ["SDL_VIDEO_CENTERED"] = "1"
pgzrun.go()