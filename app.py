import tkinter as tk
from tkinter import messagebox
import random

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

if __name__ == "__main__":
    root = tk.Tk()
    app = JeuDeCartesGUI(root)
    root.mainloop()