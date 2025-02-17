import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk  # Pour gérer les images
import random

# Définition des couleurs de l'arc-en-ciel
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
rainbow_active = False  # Variable pour activer/désactiver l'effet arc-en-ciel

def move_away(event):
    """Déplace le bouton 'I'm not gay!' aléatoirement."""
    x = random.randint(50, 300)
    y = random.randint(50, 300)
    button1.place(x=x, y=y)

def change_bg_color(index=0):
    """Change le background en mode arc-en-ciel si activé."""
    global rainbow_active
    if rainbow_active:  # Vérifie si l'effet arc-en-ciel doit être actif
        root.configure(bg=rainbow_colors[index])  
        root.after(300, change_bg_color, (index + 1) % len(rainbow_colors))  # Change la couleur toutes les 300ms

def reset_interface():
    """Réinitialise l'interface après 10 secondes."""
    global rainbow_active
    rainbow_active = False  # Désactive l'effet arc-en-ciel

    # Supprime la pop-up si elle existe encore
    if "popup" in globals():
        popup.destroy()
    
    # Réinitialise le fond en gris clair
    root.configure(bg="#f0f0f0")
    
    # Réaffiche les boutons
    button1.place(x=150, y=150)
    button2.pack(pady=20)

def show_message_with_image():
    """Affiche une nouvelle fenêtre contenant le message et l'image."""
    global popup, rainbow_active
    rainbow_active = True  # Active l'effet arc-en-ciel

    popup = Toplevel(root)  # Crée une nouvelle fenêtre pop-up
    popup.title("Confirmation")
    popup.geometry("400x400")
    popup.configure(bg="white")  # Fond initial blanc
    
    # Texte dans la boîte de dialogue
    label = tk.Label(popup, text="You are gay!", font=("Arial", 16, "bold"), fg="black", bg="white")
    label.pack(pady=10)

    # Affichage de l'image dans la boîte de dialogue
    img_label_popup = tk.Label(popup, image=img, bg="white")
    img_label_popup.pack()

    # Lancer l'effet arc-en-ciel sur la fenêtre principale
    change_bg_color()

    # Attendre 10 secondes, puis réinitialiser tout
    root.after(10000, reset_interface)

def respond():
    """Affiche la boîte de dialogue avec l'image et active l'animation du background."""
    show_message_with_image()
    button1.place_forget()  # Cache le bouton "I'm not gay!"
    button2.pack_forget()   # Cache aussi le bouton "Who says I'm gay?"

# Création de la fenêtre principale avec un fond initial clair
root = tk.Tk()
root.title("Question Form")
root.geometry("500x500")
root.configure(bg="#f0f0f0")  # Fond initial gris clair

# Label de la question avec un style amélioré
question_label = tk.Label(root, text="Why are you gay?", font=("Arial", 16, "bold"), fg="black", bg="#f0f0f0")
question_label.pack(pady=20)

# Bouton "I'm not gay!" qui fuit lorsqu'on passe dessus
button1 = tk.Button(root, text="I'm not gay!", font=("Arial", 12, "bold"), bg="red", fg="white", relief="raised")
button1.place(x=150, y=150)
button1.bind("<Enter>", move_away)

# Bouton "Who says I'm gay?" avec un style plus joli
button2 = tk.Button(root, text="Who says I'm gay?", command=respond, font=("Arial", 12, "bold"), 
                    bg="purple", fg="white", relief="raised")
button2.pack(pady=20)

# Chargement de l'image avec PIL
img = Image.open("c:/Users/seanf/Documents/Creation_Programming/wayg.jpg")  # Remplace par ton chemin correct
img = img.resize((250, 250))   # Ajuster la taille
img = ImageTk.PhotoImage(img)  # Convertit pour Tkinter

# Lancement de l'interface
root.mainloop()



