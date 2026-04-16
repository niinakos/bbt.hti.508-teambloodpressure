import tkinter as tk
from tkinter import messagebox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class PatientDetailView:
     def __init__(self, controller, patient_id):
        self.patient_id = patient_id
        self.controller = controller


        # Lisätty potilasnäkymä ja graafin pohja
        #laita def avaa_potilasikkuna(patient_id)
        #def avaa_potilasikkuna():
        self.toplevel = tk.Toplevel()
        self.toplevel.title("Patient Detail View")
        self.toplevel.geometry("360x640")
        self.toplevel.configure(bg="#ffffff")

        # Yläpalkki
        header=tk.Frame(self.toplevel, bg="#d9d9d9", height=60)
        header.pack(fill="x")
        tk.Label(header, text="Blood Pressure Tracker", bg="#d9d9d9", font=("Arial", 14, "bold")).pack(pady=15)

        # Potilaan perustiedot ja Back-nappi
        info_header=tk.Frame(self.toplevel, bg="#ffffff", pady=10)
        info_header.pack(fill="x", padx=15)

        tk.Button(info_header, text="←", command=self.toplevel.destroy, bd=0, bg="#ffffff", font=("Arial", 14)).pack(side="left")

        name_frame = tk.Frame(info_header, bg="#ffffff")
        name_frame.pack(side="left", padx=10)
        tk.Label(name_frame,text=self.controller.get_patient_name(self.patient_id), font=("Arial", 14, "bold"), bg="#ffffff").pack(anchor="w")
        tk.Label(name_frame, text=self.patient_id, font=("Arial", 10), fg="gray", bg="#ffffff").pack(anchor="w")

        # REFERENCE VALUES -nappi
        reference_btn = tk.Button(
           self.toplevel,
           text="Reference\nvalues",
           compound="top",
           font=("Arial", 9),
           fg="black",
           bg="white",
           relief="flat",
           cursor="hand2",
           command=self.avaa_viitearvot)
        reference_btn.place(x=270, y=70)

        # Kriittinen tila
        if self.controller.is_patient_critical(patient_id):
            alert_badge = tk.Label(self.toplevel, text="☹ critical condition", bg="#e53935", fg="white", font=("Arial", 11, "bold"), pady=5)
            alert_badge.pack(fill="x", padx=40, pady=10)

        # Graafi (matplotlib)
        tk.Label(self.toplevel, text="Tracking history", bg="#ffffff", font=("Arial", 10, "bold")).pack()

        # Simuloitu graafi
        fig, ax = plt.subplots(figsize=(4, 3), dpi=80)

        history = self.controller.get_patient_blood_pressure_history(self.patient_id)
        history = history[-7:]
        print("PATIENT:", self.patient_id)
        print("HISTORY:", history)
        fig, ax = plt.subplots(figsize=(4, 3), dpi=80)

        if history:
            dates = [item["date"] for item in history]
            systolic = [item["systolic"] for item in history]
            diastolic = [item["diastolic"] for item in history]

            ax.plot(dates, systolic, 'kv-', label="Sys")
            ax.plot(dates, diastolic, 'k^-', label="Dia")
            ax.set_ylim(10, 200)
            ax.grid(True, axis='y', linestyle='--', alpha=0.7)
            ax.legend()
            ax.set_ylabel("mmHg")
            ax.set_xlabel("Date")

            # jos päivämääriä paljon, käännä tekstit
            plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
        else:
            ax.text(0.5, 0.5, "No blood pressure data", ha="center", va="center")
            ax.set_axis_off()

        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self.toplevel)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="x", padx=20)



        # Riski-ilmoitus
        # jos yli 65v, ja/tai BMI > 27, lähde:WHO, ja https://doi.org/10.1161/CIRCULATIONAHA.112.117333
        if self.controller.is_hypertension_risk(patient_id):
            risk_label = tk.Label(self.toplevel, text="elevated hypertension risk", bg="#ffa726", fg="black", font=("Arial", 10), padx=10)
            risk_label.pack(anchor="w", padx=20, pady=10)
        else:
            pass

        #Potilastiedot, taulukkomainen näkymä
        detail_frame=tk.Frame(self.toplevel, bg="#ffffff", highlightbackground="black", highlightthickness=1)
        detail_frame.pack(fill="x", padx=20, pady=10)


        age= self.controller.get_age(self.patient_id)
        bmi=self.controller.get_bmi(self.patient_id)
        gender= self.controller.get_gender(self.patient_id)
        stats = [
            ("Age", f"{age} years"),
            ("BMI", bmi),
            ("Gender", gender),
        ]
        for label, value in stats:
            f=tk.Frame(detail_frame, bg="#ffffff")
            f.pack(fill="x", padx=10, pady=2)
            tk.Label(f, text=label,bg="#ffffff", font=("Arial", 11,"bold")).pack(side="left")
            tk.Label(f, text=value, bg="#ffffff", font=("Arial", 11,"bold")).pack(side="right")

        # Alapalkki
        footer=tk.Frame(self.toplevel, bg="#d9d9d9", height=50)
        footer.pack(fill="x", side="bottom")
        tk.Label(footer, text="👤 Dr. John Doe", bg="#d9d9d9", font=("Arial", 10)).pack(side="left", padx=15, pady=10)

     def avaa_viitearvot(self):
        asetus_ikkuna = tk.Toplevel(self.toplevel)
        asetus_ikkuna.title("Set Reference Values")
        asetus_ikkuna.geometry("250x220")

        tk.Label(asetus_ikkuna, text="Critical Systolic:", font=("Arial", 10)).pack(pady=5)
        sys_entry = tk.Entry(asetus_ikkuna)
        sys_entry.pack()

        tk.Label(asetus_ikkuna, text="Critical Diastolic:", font=("Arial", 10)).pack(pady=5)
        dia_entry = tk.Entry(asetus_ikkuna)
        dia_entry.pack()

        tk.Button(asetus_ikkuna, text="Save", command=lambda: self.tallenna_arvot(sys_entry, dia_entry), bg="#d9d9d9").pack(pady=20)

     def tallenna_arvot(self, sys_entry, dia_entry):
        try:
           sys_limit = int(sys_entry.get())
           dia_limit = int(dia_entry.get())
           messagebox.showinfo("Saved", f"New reference values: {sys_limit}/{dia_limit}")
           self.toplevel.destroy()
        except ValueError:
           messagebox.showerror("Error", "Give numbers only!")

     def run(self):
        self.toplevel.mainloop()