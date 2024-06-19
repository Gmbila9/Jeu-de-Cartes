""" Docstring
    @author; Germain MBILA
    @File: Jeu_de_carte.py
    @Description: l'utilisateur doit atteindre 100 points pour gagner le jeu de cartes
"""
import tkinter as tk
from tkinter import messagebox
import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"

    def points(self):
        if self.couleur in ['Cœurs', 'Carreaux']:
            return 50
        else:
            return 25

class JeuDeCartes:
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
    couleurs = ['Cœurs', 'Carreaux', 'Trèfles', 'Piques']

    def __init__(self):
        self.jeu = [Carte(valeur, couleur) for couleur in self.couleurs for valeur in self.valeurs]
        self.melanger()

    def melanger(self):
        random.shuffle(self.jeu)

    def tirer_une_carte(self):
        if len(self.jeu) == 0:
            return None
        return self.jeu.pop()


class JeuDeCartesGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de Tirage de Cartes")

        self.jeu = JeuDeCartes()
        self.points = 0
        self.tirages = 0

        self.label_points = tk.Label(root, text=f"Points totaux: {self.points}")
        self.label_points.pack()

        self.button_tirer = tk.Button(root, text="Tirer une carte", command=self.tirer_carte)
        self.button_tirer.pack()

        self.label_carte = tk.Label(root, text="Carte tirée: ")
        self.label_carte.pack()

    def tirer_carte(self):
        if self.tirages < 3:
            carte = self.jeu.tirer_une_carte()
            if carte:
                self.tirages += 1
                carte_points = carte.points()
                self.points += carte_points
                self.label_carte.config(text=f"Carte tirée: {carte}")
                self.label_points.config(text=f"Points totaux: {self.points}")
            else:
                messagebox.showinfo("Jeu terminé", "Il n'y a plus de cartes dans le jeu.")
                return

        if self.tirages == 3:
            if self.points >= 100:
                messagebox.showinfo("Félicitations!",
                                    f"Vous avez atteint {self.points} points en {self.tirages} tirages.")
            else:
                messagebox.showinfo("Désolé",
                                    f"Vous avez seulement atteint {self.points} points en {self.tirages} tirages.")
            self.button_tirer.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = JeuDeCartesGUI(root)
    root.mainloop()
