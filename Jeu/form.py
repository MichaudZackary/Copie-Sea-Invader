"""Démonstation"""
import tkinter as tk
from tkinter import messagebox, StringVar, Tk

class Form:
    
    # Variable de la classe
    username: str
    var_username: StringVar
    window: Tk
    input_done: bool
    score : int
    wave : int 

    # Initialise les variables
    def __init__(self, score : int ,wave : int ) -> None:
        self.username = ""
        self.input_done = False
        self.score = score
        self.wave = wave

    def player_input(self):

        self.window = tk.Tk()
        # Titre
        self.window.title("Who are you ?")

        self.var_username = tk.StringVar()
        
        # Label qui indique ou rentrer le Username
        lbl_username = tk.Label(self.window, text="Username :")
        lbl_username.pack()
        # Endroit ou le joueur rentre son Username
        txt_username = tk.Entry(self.window, textvariable=self.var_username, width=40)
        txt_username.pack()
        
        # Affiche le nombre de vague réussi
        lbl_wave = tk.Label(self.window, text=f"Wave : {self.wave}")
        lbl_wave.pack() 
        
        # Affiche le score obtenue       
        lbl_score = tk.Label(self.window, text=f"Score : {self.score}")
        lbl_score.pack()

        # Boutton pour valider nos informations
        button_done = tk.Button(self.window, text="Done", command=self.confirm_name)
        button_done.pack()

        self.window.mainloop()
        return [0,self.username,self.wave,self.score]

    def confirm_name(self):

        self.username = self.var_username.get()
        # Regarde si le nom est plus grand que trois caractères
        if len(self.username) < 3 :
            messagebox.showinfo("Wrong input", "The name must be 3 letter long or more ")
        else:
            self.window.destroy()
        