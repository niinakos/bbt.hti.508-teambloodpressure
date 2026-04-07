import tkinter as tk
from tkinter import ttk
from app.gui.patient_detail_view import PatientDetailView

class MainWindow:
    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Tk()
        self.root.geometry("360x640")
        self.root.title("GUI App")
        self.root.configure(bg="#e5e5e5")

        header = tk.Frame(self.root, bg="#d9d9d9", height=60)
        header.pack(fill="x")

        title = tk.Label(
            header,
            text="Blood Pressure Tracker",
            bg="#d9d9d9",
            font=("Arial", 14, "bold"),
        )
        title.pack(padx=20, pady=20)

        search_frame = tk.Frame(self.root, bg="#e5e5e5", pady=10)
        search_frame.pack(fill="x")

        search_icon = tk.Label(search_frame, text="🔍", bg="#e5e5e5", font=("Arial", 12))
        search_icon.pack(side="left", padx=(15, 5))

        self.search_entry = tk.Entry(search_frame, font=("Arial", 12))
        self.search_entry.pack(side="left", expand=True, padx=(0, 15), fill="x")
        self.search_entry.bind("<KeyRelease>", self.on_search_entry_changed)

        self.search_entry.focus()

        self.search_button = tk.Button(search_frame, text="Search", command=self.on_search_clicked)
        self.search_button.pack(side="right", padx=15)

        info_frame = tk.Frame(self.root, bg="#e5e5e5")
        info_frame.pack(fill="x", padx=15, pady=5)

        self.patient_ids = self.controller.get_patient_ids()

        self.patients_label = tk.Label(
            info_frame,
            text= f"{len(self.patient_ids)} Patients",
            bg="#e5e5e5",
            font=("Arial", 11, "bold"),
            justify="left",
        )
        self.patients_label.pack(side="left")

        badge = tk.Label(
            info_frame,
            text="☹ critical condition ",
            bg="#e53935",
            fg="white",
            font=("Arial", 10),
        )
        badge.pack(side="right")

        list_container = tk.Frame(self.root)
        list_container.pack(fill="both", expand=True, padx=10)

        self.canvas = tk.Canvas(list_container, bg="#e5e5e5", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(list_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="#e5e5e5")

        self.scrollable_frame.bind("<Configure>", self._on_content_configure)

        self.window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.bind("<Configure>", self.resize_canvas)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

        self.show_all_patients()

        bottom = tk.Frame(self.root, bg="#d9d9d9", height=60)
        bottom.pack(fill="x")

        user_label = tk.Label(bottom, text="Dr. JohnDoe", bg="#d9d9d9", font=("Arial", 11))
        user_label.pack(side="left", padx=15, pady=15)

        logout_btn = tk.Button(bottom, text="Logout")
        logout_btn.pack(side="right", padx=15)

    def resize_canvas(self, event):
        self.canvas.itemconfig(self.window, width=event.width)
        self._update_scroll_state()

    def create_patient(self, name, patient_id):
        card = tk.Frame(
            self.scrollable_frame,
            bg="white",
            highlightbackground="#cccccc",
            highlightthickness=1,
        )
        card.pack(fill="x", padx=10, pady=8)
        card.bind("<Button-1>", lambda e: PatientDetailView(self.controller, patient_id))
        def on_enter(e):
            card.configure(bg="#f0f0f0")
        def on_leave(e):
            card.configure(bg="white")

        card.bind("<Enter>", on_enter)
        card.bind("<Leave>", on_leave)

        name_label = tk.Label(
            card,
            text=name,
            font=("Calibri", 11, "bold"),
            bg="white",
        )
        name_label.pack(anchor="w", padx=10, pady=(8, 0))

        id_label = tk.Label(
            card,
            text=patient_id,
            font=("Arial", 9),
            bg="white",
        )
        id_label.pack(anchor="w", padx=10, pady=(0, 8))

        if self.controller.is_patient_critical(patient_id):
            critical_mark = tk.Label(
                card,
                text="●",
                bg="white",
                fg="red",
                font=("Arial", 14, "bold"),
            )
            critical_mark.pack(side="right")

    def show_all_patients(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        #for patient_id in self.patient_ids:
            #systolic, diastolic = self.controller.get_patient_blood_pressure(patient_id)
            #critical = self.controller.is_patient_critical(patient_id)
            #print(patient_id, systolic, diastolic, critical)
        # TODO: Check for duplicate patient IDs
        for patient_id in self.patient_ids:
            self.create_patient(self.controller.get_patient_name(patient_id), patient_id)

        self.root.update_idletasks()
        self.canvas.yview_moveto(0.0)
        self._update_scroll_state()

    def update_patients(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        patient_id = self.search_entry.get().strip()


        for p_id in self.patient_ids:
            if p_id == patient_id:
                self.create_patient(self.controller.get_patient_name(patient_id), patient_id)

                self.root.update_idletasks()
                self.canvas.yview_moveto(0.0)
                self._update_scroll_state()

                self.patients_label.config(text=f"1 Patient")
                return

        error = tk.Label(
            self.scrollable_frame,
            text="No patient found with given ID.",
            font=("Arial", 11),
            bg="#e5e5e5",
        )
        error.pack(pady=20)


    def on_click(self, event):
        print("Clicked koira")

    def on_search_clicked(self):
        query = self.search_entry.get().strip()
        if query == "":
            self.show_all_patients()
        else:
            self.update_patients()

    def on_search_entry_changed(self, event):
        query = self.search_entry.get().strip()
        if query == "":
            self.show_all_patients()
        else:
            return

        # TODO: Implement real-time search filtering here if desired

    def _on_content_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self._update_scroll_state()

    def _update_scroll_state(self):
        self.root.update_idletasks()

        content_h = self.scrollable_frame.winfo_reqheight()
        viewport_h = self.canvas.winfo_height()
        self.scroll_enabled = content_h > viewport_h + 1

        if not self.scroll_enabled:
            self.canvas.yview_moveto(0.0)
            self.scrollbar.set(0.0, 1.0)

    def _on_mousewheel(self, event):
        if not self.scroll_enabled:
            return
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def run(self):
        self.root.mainloop()
