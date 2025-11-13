#
#   Diese Datei wurde mit KI-Unterstützung erzeugt
#

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import webbrowser
import api.crud as crud


class YouTubeShortsGUI:
    def __init__(self, master):
        self.master = master
        master.title("YouTube Shorts Manager")
        master.geometry("600x400")

        # --- Überschrift ---
        #tk.Label(master, text="YouTube Shorts Verwaltung", font=("Arial", 16, "bold")).pack(pady=10)

        # --- Treeview für Datensätze ---
        self.tree = ttk.Treeview(master, columns=("id", "url"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("url", text="Short URL")
        self.tree.column("id", width=50)
        self.tree.column("url", width=450)
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # --- Buttons ---
        btn_frame = tk.Frame(master)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Neu", command=self.add_short).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Löschen", command=self.delete_short).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Zufälliger Short", command=self.show_random).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Neu laden", command=self.load_all).grid(row=0, column=3, padx=5)

        # Doppelklick öffnet Link in Browser
        self.tree.bind("<Double-1>", self.open_link)

        # --- Start mit Daten ---
        self.load_all()

    # ---------------------------------------------------------------------
    def load_all(self):
        """Lädt alle vorhandenen Shorts aus der DB"""
        for i in self.tree.get_children():
            self.tree.delete(i)

        urls: list[str] = crud.read_all()
        id:int = 0
        for url in urls:
            self.tree.insert("", "end", values=(id, url))
            id += 1


    def open_link(self, event):
        """Öffnet den angeklickten Short-Link im Browser"""
        selected = self.tree.selection()
        if not selected:
            return

        item = self.tree.item(selected[0])
        url = item["values"][1]

        if not url.startswith("http"):
            messagebox.showwarning("Ungültiger Link", f"'{url}' ist keine gültige URL.")
            return

        try:
            webbrowser.open(url)
        except Exception as e:
            messagebox.showerror("Fehler", f"Browser konnte nicht geöffnet werden:\n{e}")


    def add_short(self):
        """Neuen Short-Link hinzufügen"""
        url = simpledialog.askstring("Neuer Short", "YouTube Short URL eingeben:")
        if not url:
            return
        try:
            new_id = crud.create_short(url)
            messagebox.showinfo("Erfolg", f"Short wurde angelegt (ID={new_id})")
            self.load_all()
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Hinzufügen:\n{e}")

    def delete_short(self):
        """Ausgewählten Short löschen"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Hinweis", "Bitte einen Eintrag auswählen.")
            return

        item = self.tree.item(selected[0])
        id:int = int(item["values"][0])

        if not messagebox.askyesno("Bestätigung", f"Short mit ID {id} wirklich löschen?"):
            return

        try:
            crud.delete_short(id)
            messagebox.showinfo("Erfolg", f"Short mit ID {id} wurde gelöscht.")
            self.load_all()
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Löschen:\n{e}")

    def show_random(self):
        """Zufälligen Short anzeigen"""
        try:
            url = crud.read_short_random()
            if url:
                webbrowser.open(url)
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Abrufen:\n{e}")


# -------------------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeShortsGUI(root)
    root.mainloop()
