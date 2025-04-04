import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox, font 
from PIL import Image, ImageTk
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer les mots de passe depuis les variables d'environnement
ROOT_PASSWORD = os.getenv("ROOT_PASSWORD")
USER_PASSWORD = os.getenv("USER_PASSWORD")

# Vérifier que les mots de passe ont été correctement chargés
if not ROOT_PASSWORD or not USER_PASSWORD:
    raise ValueError("Les mots de passe n'ont pas été correctement chargés depuis le fichier .env")

# Connexion à la base de données
con = sqlite3.connect("world_of_warships.db")
cur = con.cursor()

# Stocker les mots de passe en clair (non recommandé pour la production)
USER_CREDENTIALS = {
    "root": ROOT_PASSWORD,
    "user": USER_PASSWORD
}

current_user = None

def login():
    global current_user
    username = entry_user.get()
    password = entry_pass.get()

    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        current_user = username
        messagebox.showinfo("Succès", "Connexion réussie !")
        login_window.destroy()
        open_main_interface()
    else:
        messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")

def guest_login():
    global current_user
    current_user = "user"
    messagebox.showinfo("Succès", "Connexion en mode invité réussie !")
    login_window.destroy()
    open_main_interface()

def open_main_interface():
    # Création de la fenêtre principale
    root = tk.Tk()
    root.title("World of Warships - Database Viewer")

    # Charger l'image du logo et définir l'icône de la fenêtre
    logo_image = Image.open("assets/WOW_db_logo.png")
    logo_photo = ImageTk.PhotoImage(logo_image)
    root.iconphoto(False, logo_photo)

    # Obtenir la taille de l'écran et définir la taille de la fenêtre à 75% de l'écran
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = int(screen_width * 0.75)
    window_height = int(screen_height * 0.75)
    root.geometry(f"{window_width}x{window_height}")

    # Appliquer un thème ttk
    style = ttk.Style(root)
    style.theme_use('clam')  # Vous pouvez essayer d'autres thèmes comme 'alt', 'default', 'classic'

    # Création des onglets
    tab_control = ttk.Notebook(root)
    tab_control.pack(expand=True, fill=tk.BOTH)

    # Liste des tables à afficher
    tables = ["Tier", "Class", "Nation", "Navires", "Navires_premium", "Navires_test", "Capa_de_polonger", "Main_Battery", "AP_Shells", "HE_Shells", "SAP_Shells", "Secondaries", "Sonar", "Torpedoes", "Anti_Aircraft", "Deep_Charges", "Airstrike", "Attack_aircraft", "Torpedo_Bombers", "Bombers", "Skip_Bombers"]

    # Création des onglets pour chaque table
    for table in tables:
        create_table_tab(tab_control, table)

    # Ajout du bouton pour ouvrir la console SQL si l'utilisateur est root
    if current_user == "root":
        btn_open_console = ttk.Button(root, text="Ouvrir la console SQL", command=open_sql_console, style='Accent.TButton')
        btn_open_console.pack(pady=10)

    # Lancement de la boucle principale de l'interface
    root.mainloop()

def open_sql_console():
    console_window = tk.Toplevel()
    console_window.title("World of Warships Database Console")
    console_window.geometry("600x400")

    ttk.Label(console_window, text="Entrez votre commande SQL:", font=("Arial", 12)).pack(pady=5)
    sql_entry = ttk.Entry(console_window, font=("Arial", 12), width=80)
    sql_entry.pack(pady=5)

    result_text = tk.Text(console_window, font=("Arial", 12), height=15, width=80)
    result_text.pack(pady=5)

    def execute_sql():
        command = sql_entry.get()
        try:
            cur.execute(command)
            con.commit()
            result = cur.fetchall()
            result_text.delete(1.0, tk.END)
            for row in result:
                result_text.insert(tk.END, str(row) + "\n")
            messagebox.showinfo("Succès", "Commande exécutée avec succès.")
        except sqlite3.Error as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'exécution de la commande : {e}")

    execute_button = ttk.Button(console_window, text="Exécuter", command=execute_sql, style='Accent.TButton')
    execute_button.pack(pady=10)

# Fonction pour récupérer les données d'une table
def fetch_data(table_name):
    cur.execute(f"SELECT * FROM {table_name}")
    return cur.fetchall()

# Fonction pour rafraîchir le tableau
def refresh_table(tree, table_name):
    for item in tree.get_children():
        tree.delete(item)
    for row in fetch_data(table_name):
        tree.insert("", tk.END, values=row)
    # Ajuster la largeur des colonnes automatiquement
    for col in tree["columns"]:
        max_width = max(font.Font().measure(item) for item in [col] + [str(tree.set(k, col)) for k in tree.get_children()])
        tree.column(col, width=max_width)

# Fonction pour trier les colonnes
def sort_column(tree, col, reverse):
    data = [(tree.set(child, col), child) for child in tree.get_children('')]
    data.sort(reverse=reverse)
    for index, (val, child) in enumerate(data):
        tree.move(child, '', index)
    tree.heading(col, text=f"{col} {'▲' if reverse else '▼'}", command=lambda: sort_column(tree, col, not reverse))

# Fonction pour supprimer une entrée
def delete_entry(tree, table_name):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Avertissement", "Veuillez sélectionner une ligne à supprimer.")
        return
    
    row_id = tree.item(selected_item, "values")[0]  # Suppose que la première colonne est l'ID
    try:
        cur.execute(f"DELETE FROM {table_name} WHERE id = ?", (row_id,))
        con.commit()
        tree.delete(selected_item)
    except sqlite3.Error as e:
        messagebox.showerror("Erreur", f"Impossible de supprimer l'entrée : {e}")

# Fonction pour modifier une entrée
def update_entry(tree, table_name):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Avertissement", "Veuillez sélectionner une ligne à modifier.")
        return
    
    row_values = tree.item(selected_item, "values")
    
    update_window = tk.Toplevel()
    update_window.title("Modifier une entrée")
    
    cur.execute(f"PRAGMA table_info({table_name})")
    columns = [col[1] for col in cur.fetchall()]
    
    entries = {}
    for i, col in enumerate(columns):
        ttk.Label(update_window, text=col).grid(row=i, column=0)
        entry = ttk.Entry(update_window)
        entry.grid(row=i, column=1)
        entry.insert(0, row_values[i])
        entries[col] = entry
    
    def save_changes():
        new_values = {col: entries[col].get() for col in columns}
        update_query = f"UPDATE {table_name} SET " + ", ".join(f"{col} = ?" for col in columns[1:]) + " WHERE id = ?"
        try:
            cur.execute(update_query, list(new_values.values())[1:] + [new_values[columns[0]]])
            con.commit()
            refresh_table(tree, table_name)
            update_window.destroy()
        except sqlite3.Error as e:
            messagebox.showerror("Erreur", f"Impossible de mettre à jour l'entrée : {e}")

    ttk.Button(update_window, text="Enregistrer", command=save_changes, style='Accent.TButton').grid(row=len(columns), columnspan=2)

# Fonction pour ajouter une nouvelle entrée
def add_entry(tree, table_name):
    add_window = tk.Toplevel()
    add_window.title("Ajouter une nouvelle entrée")

    cur.execute(f"PRAGMA table_info({table_name})")
    columns = [col[1] for col in cur.fetchall()]
    
    entries = {}
    for i, col in enumerate(columns):
        ttk.Label(add_window, text=col).grid(row=i, column=0)
        entry = ttk.Entry(add_window)
        entry.grid(row=i, column=1)
        entries[col] = entry
    
    def insert_data():
        new_values = {col: entries[col].get() for col in columns}
        insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['?'] * len(columns))})"
        try:
            cur.execute(insert_query, list(new_values.values()))
            con.commit()
            refresh_table(tree, table_name)
            add_window.destroy()
        except sqlite3.Error as e:
            messagebox.showerror("Erreur", f"Impossible d'ajouter l'entrée : {e}")

    ttk.Button(add_window, text="Ajouter", command=insert_data, style='Accent.TButton').grid(row=len(columns), columnspan=2)

# Fonction pour créer un tableau avec les boutons de gestion
def create_table_tab(tab_control, table_name):
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text=table_name)
    
    tree = ttk.Treeview(tab, show='headings')
    tree.pack(expand=True, fill=tk.BOTH)
    
    cur.execute(f"PRAGMA table_info({table_name})")
    columns = [col[1] for col in cur.fetchall()]
    tree["columns"] = columns
    
    for col in columns:
        tree.heading(col, text=col, command=lambda _col=col: sort_column(tree, _col, False))
    
    refresh_table(tree, table_name)
    
    # Ajout des boutons sous le tableau
    button_frame = ttk.Frame(tab)
    button_frame.pack(fill=tk.X, padx=5, pady=5)
    
    btn_refresh = ttk.Button(button_frame, text="Rafraîchir", command=lambda: refresh_table(tree, table_name), style='Accent.TButton')
    btn_refresh.pack(side=tk.LEFT, padx=5)
    
    btn_update = ttk.Button(button_frame, text="Modifier", command=lambda: update_entry(tree, table_name), style='Accent.TButton')
    btn_update.pack(side=tk.LEFT, padx=5)
    
    btn_delete = ttk.Button(button_frame, text="Supprimer", command=lambda: delete_entry(tree, table_name), style='Accent.TButton')
    btn_delete.pack(side=tk.LEFT, padx=5)

    btn_add = ttk.Button(button_frame, text="Ajouter", command=lambda: add_entry(tree, table_name), style='Accent.TButton')
    btn_add.pack(side=tk.LEFT, padx=5)

    # Désactiver les boutons de modification, suppression et ajout si l'utilisateur est un utilisateur régulier
    if current_user == "user":
        btn_update.config(state=tk.DISABLED)
        btn_delete.config(state=tk.DISABLED)
        btn_add.config(state=tk.DISABLED)

# Création de la fenêtre de connexion
login_window = tk.Tk()
login_window.title("Connexion")
login_window.geometry("400x500")

# Appliquer un thème ttk
style = ttk.Style(login_window)
style.theme_use('clam')  # Vous pouvez essayer d'autres thèmes comme 'alt', 'default', 'classic'

# Ajout du logo
logo_image = Image.open("assets/logo.webp")
logo_image = logo_image.resize((200, 200), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = ttk.Label(login_window, image=logo_photo)
logo_label.pack(pady=10)

# Ajout des champs de saisie et des boutons
ttk.Label(login_window, text="Nom d'utilisateur", font=("Arial", 12)).pack(pady=5)
entry_user = ttk.Entry(login_window, font=("Arial", 12))
entry_user.pack(pady=5)

ttk.Label(login_window, text="Mot de passe", font=("Arial", 12)).pack(pady=5)
entry_pass = ttk.Entry(login_window, show="*", font=("Arial", 12))
entry_pass.pack(pady=5)

btn_login = ttk.Button(login_window, text="Se connecter", command=login, style='Accent.TButton')
btn_login.pack(pady=20)

# Ajout du bouton Mode Invité
btn_guest = ttk.Button(login_window, text="Mode Invité", command=guest_login, style='Accent.TButton')
btn_guest.pack(pady=10)

# Lancement de la boucle principale de la fenêtre de connexion
login_window.mainloop()

# Fermeture de la connexion à la base de données
con.close()