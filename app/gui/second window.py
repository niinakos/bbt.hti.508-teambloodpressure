import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Lisätty potilasnäkymä ja graafin pohja
#laita def avaa_potilasikkuna(patient_id)
#def avaa_potilasikkuna():
uusi_ikkuna=tk.Toplevel()
uusi_ikkuna.title("Patient Detail View")
uusi_ikkuna.geometry("360x640")
uusi_ikkuna.configure(bg="#ffffff")

# Yläpalkki
header=tk.Frame(uusi_ikkuna, bg="#d9d9d9", height=60)
header.pack(fill="x")
tk.Label(header, text="Blood Pressure Tracker", bg="#d9d9d9", font=("Arial", 14, "bold")).pack(pady=15)

# Potilaan perustiedot ja Back-nappi
info_header=tk.Frame(uusi_ikkuna, bg="#ffffff", pady=10)
info_header.pack(fill="x", padx=15)

tk.Button(info_header, text="←", command=uusi_ikkuna.destroy, bd=0, bg="#ffffff", font=("Arial", 14)).pack(side="left")

name_frame = tk.Frame(info_header, bg="#ffffff")
name_frame.pack(side="left", padx=10)
tk.Label(name_frame,text="Patient Name", font=("Arial", 14, "bold"), bg="#ffffff").pack(anchor="w")
tk.Label(name_frame, text="Patient ID", font=("Arial", 10), fg="gray", bg="#ffffff").pack(anchor="w")

# Kriittinen tila
alert_badge = tk.Label(uusi_ikkuna, text="☹ critical condition", bg="#e53935", fg="white", font=("Arial", 11, "bold"), pady=5)
alert_badge.pack(fill="x", padx=40, pady=10)

# Graafi (matplotlib)
tk.Label(uusi_ikkuna, text="Tracking history", bg="#ffffff", font=("Arial", 10, "bold")).pack()

# Simuloitu graafi
fig, ax = plt.subplots(figsize=(4, 3), dpi=80)
dates = ["Apr 1", "Apr 3", "Apr 5", "Apr 7", "Apr 9"]
systolic = [120, 135, 125, 140, 155]
diastolic = [80, 85, 82, 90, 105]

ax.plot(dates, systolic, 'kv-', label="Sys")
ax.plot(dates, diastolic, 'k^-', label="Dia")
ax.set_ylim(40, 200)
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

canvas = FigureCanvasTkAgg(fig, master=uusi_ikkuna)
canvas.draw()
canvas.get_tk_widget().pack(fill="x", padx=20)

# Riski-ilmoitus
# jos yli 65v, ja/tai BMI > 27, lähde:WHO, ja https://doi.org/10.1161/CIRCULATIONAHA.112.117333
#määrittele muuttujat age ja BMI
if age>64 or BMI > 26:
    risk_label = tk.Label(uusi_ikkuna, text="elevated hypertension risk", bg="#ffa726", fg="black", font=("Arial", 10), padx=10)
    risk_label.pack(anchor="w", padx=20, pady=10)
else:
    pass

#Potilastiedot, taulukkomainen näkymä
detail_frame=tk.Frame(uusi_ikkuna, bg="#ffffff", highlightbackground="black", highlightthickness=1)
detail_frame.pack(fill="x", padx=20, pady=10)

stats = [("Gender", "gender_from_FHIR"), ("Age", f"age_from_FHIR years"),("Weight", "weight_from_FHIR"), ("BMI", "BMI_from_FHIR") ]
for label, value in stats:
    f=tk.Frame(detail_frame, bg="#ffffff")
    f.pack(fill="x", padx=10, pady=2)
    tk.Label(f, text=label,bg="#ffffff", font=("Arial", 11,"bold")).pack(side="left")
    tk.Label(f, text=value, bg="#ffffff", font=("Arial", 11,"bold")).pack(side="right")

# Alapalkki
footer=tk.Frame(uusi_ikkuna, bg="#d9d9d9", height=50)
footer.pack(fill="x", side="bottom")
tk.Label(footer, text="👤 Dr. John Doe", bg="#d9d9d9", font=("Arial", 10)).pack(side="left", padx=15, pady=10)

uusi_ikkuna.mainloop()
# Pääikkunan koodista pitää etsiä koodi 'button' ja muuttaa sen näin(?):
# button=tk.Button(root, text="Patient Name", font=("Arial", 14), command=avaa_potilasikkuna)