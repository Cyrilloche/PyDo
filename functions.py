# functions.py>

from tkinter import messagebox, Tk
from tkcalendar import Calendar
from datetime import datetime, timedelta
import setup



# Initialisation des variables  : -------------------------------------------------------------------------------------------------
new_task_name = ""
new_task_description = ""
mydate_now = ""
#global date_end
date_now = datetime.today()
date_end = None  

# Initialisation des fontions : -------------------------------------------------------------------------------------------------

    # Fonction addTask
def addTask():
    global new_task_name, new_task_description, date_now, date_end

    task_name = setup.show_window.new_task_name.get(new_task_name)
    task_description = setup.show_window.new_task_description.get("1.0", "end-1c")
    #date_end = show_calendar()
    print(task_name)

    print("je suis la tache")
    # config.mycursor.execute("INSERT INTO taches (nomTache, descriptionTache, creationTache, dateObjectif, etatTache) VALUES (%s,%s,%s,%s,%s)",
    #                  (task_name, task_description, date_now, date_end,1))