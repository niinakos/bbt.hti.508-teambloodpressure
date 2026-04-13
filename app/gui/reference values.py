import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# --- 1. GLOBAALIT ASETUKSET JA OLETUSARVOT ---
sys_limit = 180
dia_limit = 120
age = 65
BMI = 28


def avaa_potilasikkuna():
    # Luodaan ikkuna (Toplevel, jotta se voi auveta pääikkunasta)
    uusi_ikkuna = tk.Toplevel()
    uusi_ikkuna.title("Patient Detail View")
    uusi_ikkuna.geometry("360x780")  # Hieman korkeampi, jotta kaikki mahtuu
    uusi_ikkuna.configure(bg="#ffffff")

    # --- 2. VIITEARVOJEN MUUTTAMINEN ---
    def avaa_viitearvot():
        asetus_ikkuna = tk.Toplevel(uusi_ikkuna)
        asetus_ikkuna.title("Set Reference Values")
        asetus_ikkuna.geometry("250x220")

        tk.Label(asetus_ikkuna, text="Critical Systolic:", font=("Arial", 10)).pack(pady=5)
        sys_entry = tk.Entry(asetus_ikkuna)
        sys_entry.insert(0, str(sys_limit))
        sys_entry.pack()

        tk.Label(asetus_ikkuna, text="Critical Diastolic:", font=("Arial", 10)).pack(pady=5)
        dia_entry = tk.Entry(asetus_ikkuna)
        dia_entry.insert(0, str(dia_limit))
        dia_entry.pack()

        def tallenna_arvot():
            global sys_limit, dia_limit
            try:
                sys_limit = int(sys_entry.get())
                dia_limit = int(dia_entry.get())
                messagebox.showinfo("Saved", f"New reference values: {sys_limit}/{dia_limit}")
                asetus_ikkuna.destroy()
            except ValueError:
                messagebox.showerror("Error", "Give numbers only!")

        tk.Button(asetus_ikkuna, text="Save", command=tallenna_arvot, bg="#d9d9d9").pack(pady=20)

    # --- 3. KÄYTTÖLIITTYMÄN RAKENNE ---

    # Yläpalkki
    header = tk.Frame(uusi_ikkuna, bg="#d9d9d9", height=60)
    header.pack(fill="x")
    tk.Label(header, text="Blood Pressure Tracker", bg="#d9d9d9", font=("Arial", 14, "bold")).pack(pady=15)

    # Potilaan tiedot -alue
    info_header = tk.Frame(uusi_ikkuna, bg="#ffffff", pady=10)
    info_header.pack(fill="x", padx=15)

    tk.Button(info_header, text="←", command=uusi_ikkuna.destroy, bd=0, bg="#ffffff", font=("Arial", 14)).pack(
        side="left")

    name_frame = tk.Frame(info_header, bg="#ffffff")
    name_frame.pack(side="left", padx=10)
    tk.Label(name_frame, text="Patient Name", font=("Arial", 14, "bold"), bg="#ffffff").pack(anchor="w")
    tk.Label(name_frame, text="Patient ID", font=("Arial", 10), fg="gray", bg="#ffffff").pack(anchor="w")

    # REFERENCE VALUES -nappi (Sijoitettu oikealle)
    reference_btn = tk.Button(
        uusi_ikkuna,
        text="Reference\nvalues",
        compound="top",
        font=("Arial", 9),
        fg="black",
        bg="white",
        relief="flat",
        cursor="hand2",
        command=avaa_viitearvot
    )
    reference_btn.place(x=270, y=70)

    # Kriittinen tila -badge
    alert_badge = tk.Label(uusi_ikkuna, text="☹ critical condition", bg="#e53935", fg="white",
                           font=("Arial", 11, "bold"), pady=5)
    alert_badge.pack(fill="x", padx=40, pady=10)

    # Graafi
    tk.Label(uusi_ikkuna, text="Tracking history", bg="#ffffff", font=("Arial", 10, "bold")).pack()

    fig, ax = plt.subplots(figsize=(4, 2.5), dpi=80)
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
    if age > 64 or BMI > 26:
        risk_label = tk.Label(uusi_ikkuna, text="elevated hypertension risk", bg="#ffa726", fg="black",
                              font=("Arial", 10), padx=10)
        risk_label.pack(anchor="w", padx=20, pady=10)

    # Potilastiedot taulukko
    detail_frame = tk.Frame(uusi_ikkuna, bg="#ffffff", highlightbackground="black", highlightthickness=1)
    detail_frame.pack(fill="x", padx=20, pady=10)

    stats = [("Gender", "Female"), ("Age", f"{age} years"), ("Weight", "70 kg"), ("BMI", f"{BMI}")]
    for label, value in stats:
        f = tk.Frame(detail_frame, bg="#ffffff")
        f.pack(fill="x", padx=10, pady=2)
        tk.Label(f, text=label, bg="#ffffff", font=("Arial", 10, "bold")).pack(side="left")
        tk.Label(f, text=value, bg="#ffffff", font=("Arial", 10)).pack(side="right")

    # Alapalkki
    footer = tk.Frame(uusi_ikkuna, bg="#d9d9d9", height=40)
    footer.pack(fill="x", side="bottom")
    tk.Label(footer, text="👤 Dr. John Doe", bg="#d9d9d9", font=("Arial", 9)).pack(side="left", padx=15, pady=5)


# --- 4. PÄÄOHJELMA ---
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("300x200")

    # Esimerkki napista, joka avaa potilasikkunan
    main_btn = tk.Button(root, text="Open Patient Details", command=avaa_potilasikkuna)
    main_btn.pack(expand=True)

    root.mainloop()