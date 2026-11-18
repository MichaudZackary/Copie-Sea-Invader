# Equipe10

Le jeu est un space invader avec des pirattes a la place

Le jeu se joue comme si :

"A" et "D" pour les deplacement ("A" = gauche "D" = droite).

appuyer sur "SPACE" pour tiré des projectiles.

Tu doit esquiver les projectiles ennemies durant que tu les tues.

Des Bonus peuvent aléatoirement tomber lorsque les ennemies meures il y en a trois un qui redonne 1 pv, un qui te fait aller 1.5x plus vite et un qui te fait tiré 2x plus vite les deux dure approximativement 1 minute 30

Pour lancer le jeu tu doit executé main.exe

/////////////////////////////////////////////////////////////////

Graphique

Pour la partir graphique apres chaque partie le fichier data_graph est modifier avec les données recueil lors du spawn des bonus 

tu dois ensuite lancer le script "graph.py"

il y a des point pour facilement comprendre ou est chaque bonus récupéré

/////////////////////////////////////////////////////////////////

Flask

Le flask ouvre une page web local contenant les scores des joueurs précédents avec leurs Usernames, leurs nombre de vague terminer et le score final.

Le  flask s'ouvre avec le dossier app.py.

Il doit être executée avec le débogeur flask se trouvant sur le coté gauche avec le bouton start et une bestiole.

Le fichier Flask va lire et afficher du contenu de fichier .csv

Pour avoir le score qui des nouvelle partie jouer, l'utilisateur doit manuellement copier le fichier data.csv qui se trouve dans Jeu/donnees/data.csv et le coller dans le fichier du même nom se trouvant dans flask/donnees/.

/////////////////////////////////////////////////////////////////

Unittest

Le test pour ajouter le nouvel utilisateur fonctionne le reste je n'est pas été capable de recrée un débogeur.
    Le test s'execute comme ceci :
    Il va crée un utilisateur, va regareder si l'utilisateur respect toutes les règles consernant les données entrées.
    Il va ensuite se crée un identifiant.
    Il va s'ajouter au fichier csv.
Pour executer le test, il faut
    # Pour pouvoir déboguer les tests :
    Dans le menu de gauche, dans VS Code, cliquez sur le sablier.
    Clicker ensuite sur le petit bouton play.
    Il va ensuite dire si le test s'est effectuer avec succèes ou non.
    Il y a aussi l'option de l'executer avec le débogeur affin de s'avoir ou exactement s'execute le ou les problèmes
    Cependant, je ne sais pas pourquoi, mais je ne peut pas crée de nouveau test si un test est dejà crée.


En Général pour le prof:
Nous avons souvent travailler en dehors des cours.
Cela entrainait que nous fessions des appels qui menait a se que les deux ont parle ensemble du projets et avançons, mais sur le compte de Zach plus que sur celui de Simon.
Pour résumer Simon n'a pas fait rien sur la partie pgzero et Zach na pas rien fait sur la partie flask non plus.