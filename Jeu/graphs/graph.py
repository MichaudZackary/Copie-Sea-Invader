import pandas as pd
import matplotlib.pyplot as plt

class Graph :
    def __init__(self) -> None:
        
        # Ouverture du fichier data_rgaph.csv avec pandas
        df = pd.read_csv("Jeu/graphs/data_graph.csv", encoding='utf8')

        # Fait la courbe D est l'axe des x et P l'axe des y         
        plt.plot(df["D"], df["P"],color="darkred")

        # Nom de l'axe des x
        plt.xlabel("killed Enemy")

        # Nom de l'axe des y
        plt.ylabel("Power Up")

        # Titre
        plt.title("Number of kill did before the next Power Up")

        # Fait des point sur la ligne 
        plt.plot(df["D"], df["P"], color = "darkred", marker = 'o', label = "Power Up pick up")

        # Affichage du graphique
        plt.legend()
        plt.show()