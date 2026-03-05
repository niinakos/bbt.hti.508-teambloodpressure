import tkinter as tk
from tkinter import ttk
root = tk.Tk()

root.geometry("360x640")
root.title("GUI App")
root.configure(bg="#e5e5e5")

header = tk.Frame(root, bg="#d9d9d9", height=60)
header.pack(fill="x")

title= tk.Label(header, text="Blood Pressure Tracker", bg="#d9d9d9", font=("Arial", 14, "bold"))
title.pack(padx=20, pady=20)

search_frame= tk.Frame(root, bg="#e5e5e5", pady=10)
search_frame.pack(fill="x")

search_icon = tk.Label(search_frame, text="🔍", bg="#e5e5e5", font=("Arial", 12))
search_icon.pack(side="left", padx=(15,5))

search_entry = tk.Entry(search_frame, font=("Arial", 12))
search_entry.pack(side="left", expand=True, padx=(0,15), fill="x")

info_frame = tk.Frame(root, bg="#e5e5e5")
info_frame.pack(fill="x", padx=15, pady=5)

patients_label = tk.Label(info_frame, text="Patients\n95/495",
                          bg="#e5e5e5", font=("Arial", 11, "bold"),
                          justify="left")
patients_label.pack(side="left")

badge = tk.Label(info_frame,
                 text=" critical condition ",
                 bg="#e53935", fg="white",
                 font=("Arial", 10))
badge.pack(side="right")

list_container = tk.Frame(root)
list_container.pack(fill="both", expand=True, padx=10)

canvas = tk.Canvas(list_container, bg="#e5e5e5", highlightthickness=0)
scrollbar = ttk.Scrollbar(list_container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#e5e5e5")

scrollable_frame.bind( "<Configure>", lambda e: canvas.configure( scrollregion=canvas.bbox("all")
                                                                  )
                       )
window = canvas.create_window((0, 0),window=scrollable_frame, anchor="nw")


def resize_canvas(event):
    canvas.itemconfig(window, width=event.width)

canvas.bind("<Configure>", resize_canvas)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))

def create_patient(name, patient_id):
    card = tk.Frame(
        scrollable_frame,
        bg="white",
        highlightbackground="#cccccc",
        highlightthickness=1
    )

    card.pack(fill="x", padx=10, pady=8)

    def on_click(event):
        print(f"Clicked {name}")

    card.bind("<Button-1>", on_click)

    name_label = tk.Label(
        card,
        text=name,
        font=("Calibri", 11, "bold"),
        bg="white"
    )
    name_label.pack(anchor="w", padx=10)

    id_label = tk.Label(
        card,
        text=patient_id,
        font=("Arial", 9),
        bg="white"
    )
    id_label.pack(anchor="w", padx=10)


for i in range(30):
    create_patient("Patient Name", "Patient ID")


bottom = tk.Frame(root, bg="#d9d9d9", height=60)
bottom.pack(fill="x")

user_label = tk.Label(
    bottom,
    text="Dr. JohnDoe",
    bg="#d9d9d9",
    font=("Arial", 11)
)
user_label.pack(side="left", padx=15, pady=15)

logout_btn = tk.Button(bottom, text="Logout")
logout_btn.pack(side="right", padx=15)

root.mainloop()
