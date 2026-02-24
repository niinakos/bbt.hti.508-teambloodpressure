import tkinter as tk

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

button= tk.Button(root, text="Patient Name", font=("Arial", 14))
button.pack(padx=20, pady=20)
root.mainloop()