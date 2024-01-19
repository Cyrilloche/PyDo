# global.py

from tkinter import Tk, Button, Text, Listbox, Entry, END, Message, StringVar
import tkinter as tk
import mysql.connector
from tkcalendar import Calendar
from datetime import datetime, timedelta

#  Connexion à la base de données : -------------------------------------------------------------------------------------------------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pydo"
)
mycursor = mydb.cursor()

# Initialisation des variables : -------------------------------------------------------------------------------------------------
mydate_now = ""
date_now = datetime.today()
date_end = None
task_list = None

# Création du calendrier : -------------------------------------------------------------------------------------------------
def show_calendar():
    global date_end

        # Récupération et conversion de la date limite de la tâche
    def select_date():
        global date_end
        selected_date_str = calendar.get_date()
        date_end_parsed = datetime.strptime(selected_date_str, "%d/%m/%Y")
        date_end = date_end_parsed.strftime("%Y-%m-%d")
        #print(date_end)
        new_window.destroy()

        # Paramètre du calendrier
    mindate = date_now
    maxdate = date_now + timedelta(days=365)
    new_window = tk.Toplevel()
    button_validate = Button(new_window, text="Valider", command=select_date)
    
    calendar = Calendar(new_window, font="Arial 14", selectmode='day', locale='fr_FR',
                        mindate=mindate, maxdate=maxdate, disabledforeground='red',
                        cursor="hand2")
    calendar.pack()
    button_validate.pack()

# Initialisation des fonctions : -------------------------------------------------------------------------------------------------
    
    # Fonction ajouter tâche
def addTask():
    task_name = new_task_name.get()
    task_description = new_task_description.get("1.0", "end-1c")
    #print(task_name)
    #print(task_description)

    mycursor.execute("INSERT INTO taches (nomTache, descriptionTache, creationTache, dateObjectif, etatTache) VALUES (%s,%s,%s,%s,%s)",
                     (task_name, task_description, date_now, date_end, 1))
    mydb.commit()
    show_list()

    # Fonction affichage listBox
def show_list():
    task_list.delete(0, END) # Efface la liste avant de rafraichir
    mycursor.execute("SELECT nomTache FROM taches")
    for x in mycursor:
        s = ""
        for tache in x:
            s = str(tache)
            #print(tache)
            #print(type(tache))
        task_list.insert(END, s)

def delete():
        mycursor('DELETE FROM taches')

    # Fonction affichage des détails des tâches
def show_details():
    
    details_windows = tk.Toplevel()
    details_windows.configure(bg="#333333", padx=10, pady=10)
    details_windows.geometry("300x400")

    mycursor.execute('SELECT nomTache, descriptionTache, creationTache, dateObjectif FROM taches')
    details = StringVar()
    var =""
    for x in mycursor:
        details.set
        for tache in x:
            var = var + " " + str(tache) + " "

    label = Message(details_windows, textvariable=details)
    details.set(var)
    label.pack()

    ok_button = Button(details_windows, text = "OK", command=details_windows.destroy)
    ok_button.pack()

    def delete():
        mycursor.execute('DELETE FROM taches')
        details_windows.destroy()
        show_list()

    delete_button = Button(details_windows, text = "Supprimer", command= delete)
    delete_button.pack()



# Initialisation de la fenêtre principale : -------------------------------------------------------------------------------------------------
class pydo_window(Tk):

    def __init__(self):
        global new_task_name, new_task_description, task_list
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
        calendar_button = Button(self, text="Calendrier", width=25, command=show_calendar)
        calendar_button.grid(column=0, row=2, padx=10, pady=10)
        add_task_button = Button(self, text = "Ajouter", width=25, command=addTask)
        add_task_button.grid(column=1, row=2, padx=10, pady=10)

            # Ligne 4 - Bloc liste
        task_list = Listbox(self, width=50)
        task_list.grid(column=0, row=3, columnspan=2)
        show_list()

            # Ligne 5 - Bouton terminées / Bouton supprimer
        task_finish_button = Button(self, text="Détails", width=25, command= show_details)
        task_finish_button.grid(column=0, row=4, padx=10, pady=10)
        delete_task_button = Button(self, text="Terminées", width=25)
        delete_task_button.grid(column=1, row=4, padx=10, pady=10)

#print("j'ouvre la fenetre")
window = pydo_window()
window.mainloop()