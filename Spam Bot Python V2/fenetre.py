from tkinter import Tk, Label, Entry, Button, messagebox
import pyautogui
import time
import pyperclip

message_entry = None  # Déclaration globale
nombre_entry = None   # Déclaration globale

def ma_fenetre():
    fenetre = Tk()
    fenetre.geometry('500x300')
    fenetre.title('Spam Discord')

    # Label et champ de saisie pour le message
    global message_entry  # Utilisez 'global' pour indiquer que vous faites référence à la variable globale
    message_label = Label(fenetre, text="Choix message")
    message_label.pack()
    message_entry = Entry(fenetre)
    message_entry.pack()

    # Label et champ de saisie pour le nombre
    global nombre_entry  # Utilisez 'global' pour indiquer que vous faites référence à la variable globale
    nombre_label = Label(fenetre, text="Choix nombre")
    nombre_label.pack()
    nombre_entry = Entry(fenetre)
    nombre_entry.pack()

    # Bouton "Envoyer"
    envoyer_button = Button(fenetre, text="Envoyer", command=envoyer_message)
    envoyer_button.pack()

    fenetre.mainloop()

def envoyer_message():
    message = message_entry.get()
    nombre = nombre_entry.get()
    
    if message and nombre:
        try:
            nombre = int(nombre)  # Convertir 'nombre' en entier
            c = 0
            pyautogui.hotkey('alt', 'tab') 
            pyautogui.click(1040, 1000)
            time.sleep(1)
            for i in range(nombre):
                time.sleep(0.5)
                pyperclip.copy(message)  
                pyautogui.hotkey('ctrl', 'v') 
                pyautogui.press('enter')
                c = c + 1
                if c == nombre:
                    time.sleep(1)
                    pyautogui.hotkey('alt', 'tab') 
        except ValueError:
            messagebox.askyesno('Titre 1', 'Le nombre de messages doit etre un nombre entier !')
            

if __name__ == '__main__':
    ma_fenetre()
