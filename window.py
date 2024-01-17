# window.py>

from tkinter import Tk, Button, Text, Listbox, Entry
import setup

# Initialisation de la fenêtre principale : -------------------------------------------------------------------------------------------------
class pydo_window(Tk):

    def __init__(self):

        super().__init__()

            # On change la couleur de fond et les marges de la fenêtre.
        self.configure(bg="#333333", padx=10, pady=10)
            # On renomme la fenêtre
        self.title('PyDo')
            # On définie la taille de la fenêtre
        self.geometry("300x400")
            # Autres paramètres de la fenêtre
        self.resizable(width=False, height=False)

            # On divise la fenetre en 15 row et 12 columns
            # On leur attribut un poids
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=0)


            # uniform="samegroup" force la taille des colonnes
            # La même chaîne de caractère force la même taille
            # weight = 1 force que les colonnes occupe 100% de la largeur de la fenetre
        self.grid_columnconfigure(0, weight=1, uniform="same_group")
        self.grid_columnconfigure(1, weight=1, uniform="same_group")


            # Ligne 1 - Bloc nom
        new_task_name = Entry(self, width=50)
        new_task_name.grid(column=0, row=0, columnspan=2)

            # Ligne 2 - Bloc description
        new_task_description = Text(self, width=50, height=3)
        new_task_description.grid(column=0, row=1, columnspan=2, pady=10)

            # Ligne 3 - Bouton calendrier / Bouton ajouter
        calendar_button = Button(self, text="Calendrier", width=25)
        calendar_button.grid(column=0, row=2, padx=10, pady=10)
        add_task_button = Button(self, text = "Ajouter", width=25, command=setup.test)
        add_task_button.grid(column=1, row=2, padx=10, pady=10)

            # Ligne 4 - Bloc liste
        task_list = Listbox(self, width=50)
        task_list.grid(column=0, row=3, columnspan=2)

            # Ligne 5 - Bouton terminées / Bouton supprimer
        task_finish_button = Button(self, text="Terminées", width=25)
        task_finish_button.grid(column=0, row=4, padx=10, pady=10)
        delete_task_button = Button(self, text = "Supprimer", width=25)
        delete_task_button.grid(column=1, row=4, padx=10, pady=10)
            

print("j'ouvre la fenetre")
window = pydo_window()
window.mainloop()