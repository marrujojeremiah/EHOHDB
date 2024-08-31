import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from database import (
    get_clients, get_appointments, get_behaviors, get_awol, get_medications, search_clients
)

class MainScreen(tk.Frame):
    def __init__(self, master, role):
        super().__init__(master)
        self.role = role
        self.grid(padx=20, pady=20)

        # Create a Notebook (tabbed interface)
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, padx=10, pady=10)

        # Create the tabs
        self.create_homepage_tab()
        self.create_all_clients_tab()
        self.create_appointments_tab()
        self.create_behaviors_tab()
        self.create_awol_tab()
        self.create_medications_tab()
        self.create_search_tab()

    # Add the homepage tab creation method
    def create_homepage_tab(self):
        self.homepage_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.homepage_tab, text="Home")

        # Welcome and description
        welcome_label = tk.Label(self.homepage_tab, text="Welcome to EHOH Client Management System",
                                 font=("Helvetica", 20, "bold"))
        welcome_label.grid(row=0, column=0, padx=20, pady=20, columnspan=3)

        description_label = tk.Label(self.homepage_tab, text="Manage client information, appointments, behaviors, "
                                                             "and more efficiently with this system.",
                                     font=("Helvetica", 14))
        description_label.grid(row=1, column=0, padx=20, pady=10, columnspan=3)

        # Add buttons with icons (optional)
        clients_button = tk.Button(self.homepage_tab, text="Clients", font=("Helvetica", 14),
                                   command=lambda: self.notebook.select(self.notebook.index(self.all_clients_tab)),
                                   width=15, height=2, bg="lightblue")
        clients_button.grid(row=2, column=0, padx=20, pady=20)

        appointments_button = tk.Button(self.homepage_tab, text="Appointments", font=("Helvetica", 14),
                                        command=lambda: self.notebook.select(self.notebook.index(self.appointments_tab)),
                                        width=15, height=2, bg="lightgreen")
        appointments_button.grid(row=2, column=1, padx=20, pady=20)

        behaviors_button = tk.Button(self.homepage_tab, text="Behaviors", font=("Helvetica", 14),
                                     command=lambda: self.notebook.select(self.notebook.index(self.behaviors_tab)),
                                     width=15, height=2, bg="lightcoral")
        behaviors_button.grid(row=2, column=2, padx=20, pady=20)

        awol_button = tk.Button(self.homepage_tab, text="AWOL", font=("Helvetica", 14),
                                command=lambda: self.notebook.select(self.notebook.index(self.awol_tab)),
                                width=15, height=2, bg="lightyellow")
        awol_button.grid(row=3, column=0, padx=20, pady=20)

        medications_button = tk.Button(self.homepage_tab, text="Medications", font=("Helvetica", 14),
                                       command=lambda: self.notebook.select(self.notebook.index(self.medications_tab)),
                                       width=15, height=2, bg="lightpink")
        medications_button.grid(row=3, column=1, padx=20, pady=20)

        # Adding the DRs button
        drs_button = tk.Button(self.homepage_tab, text="DRs", font=("Helvetica", 14),
                               width=15, height=2, bg="lightcyan")
        drs_button.grid(row=3, column=2, padx=20, pady=20)

        # Adding the Search button
        search_button = tk.Button(self.homepage_tab, text="Search Clients", font=("Helvetica", 14),
                                  command=lambda: self.notebook.select(self.notebook.index(self.search_tab)),
                                  width=32, height=2, bg="lightgray")
        search_button.grid(row=4, column=0, columnspan=3, padx=20, pady=20)

        # Adding the Upload button
        upload_button = tk.Button(self.homepage_tab, text="Upload Document", font=("Helvetica", 14),
                                  command=self.upload_document, width=32, height=2, bg="lightgoldenrod")
        upload_button.grid(row=5, column=0, columnspan=3, padx=20, pady=20)

        # Footer or additional description
        footer_label = tk.Label(self.homepage_tab, text="Powered by EHOH Technology Solutions", font=("Helvetica", 10))
        footer_label.grid(row=6, column=0, padx=20, pady=20, columnspan=3)

    def upload_document(self):
        file_path = filedialog.askopenfilename(title="Select a Document", 
                                               filetypes=[("PDF files", "*.pdf"), 
                                                          ("Image files", "*.jpg *.jpeg *.png"),
                                                          ("Word documents", "*.doc *.docx"),
                                                          ("All files", "*.*")])
        if file_path:
            # Handle the upload process
            # Here you can save the file path to the database or copy the file to a specific location
            messagebox.showinfo("Upload Successful", f"Document '{file_path}' has been uploaded successfully.")
        else:
            messagebox.showwarning("Upload Cancelled", "No document was selected.")

    # Create the AWOL tab with input fields for events
    def create_awol_tab(self):
        self.awol_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.awol_tab, text="AWOL")

        # Form fields for AWOL entry
        tk.Label(self.awol_tab, text="Date:").grid(row=0, column=0, sticky="e")
        self.awol_date_entry = tk.Entry(self.awol_tab)
        self.awol_date_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.awol_tab, text="Time:").grid(row=1, column=0, sticky="e")
        self.awol_time_entry = tk.Entry(self.awol_tab)
        self.awol_time_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.awol_tab, text="Cause:").grid(row=2, column=0, sticky="e")
        self.awol_cause_entry = tk.Entry(self.awol_tab)
        self.awol_cause_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.awol_tab, text="Summary:").grid(row=3, column=0, sticky="ne")
        self.awol_summary_text = tk.Text(self.awol_tab, height=5, width=40)
        self.awol_summary_text.grid(row=3, column=1, padx=10, pady=5)

        # Submit button for AWOL entry
        self.awol_submit_button = tk.Button(self.awol_tab, text="Submit AWOL", command=self.submit_awol)
        self.awol_submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Frame to display AWOL records
        self.awol_frame = ttk.Frame(self.awol_tab)
        self.awol_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.load_awol()

    # Handle AWOL submission
    def submit_awol(self):
        date = self.awol_date_entry.get()
        time = self.awol_time_entry.get()
        cause = self.awol_cause_entry.get()
        summary = self.awol_summary_text.get("1.0", tk.END).strip()

        # Here you would add the code to insert this information into your database
        # For now, we'll just print it to confirm the input
        print(f"AWOL Record Submitted:\nDate: {date}\nTime: {time}\nCause: {cause}\nSummary: {summary}")

        # Clear the input fields after submission
        self.awol_date_entry.delete(0, tk.END)
        self.awol_time_entry.delete(0, tk.END)
        self.awol_cause_entry.delete(0, tk.END)
        self.awol_summary_text.delete("1.0", tk.END)

        # Reload the AWOL data to reflect the new entry
        self.load_awol()

    # Load AWOL records from the database and display them
    def load_awol(self):
        awol_records = get_awol()
        row = 0
        for awol in awol_records:
            tk.Label(self.awol_frame, text=f"Client: {awol[0]}").grid(row=row, column=0, sticky="w")
            tk.Label(self.awol_frame, text=f"Date: {awol[1]}").grid(row=row, column=1, sticky="w")
            tk.Label(self.awol_frame, text=f"Time: {awol[2]}").grid(row=row, column=2, sticky="w")
            tk.Label(self.awol_frame, text=f"Cause: {awol[3]}").grid(row=row, column=3, sticky="w")
            tk.Label(self.awol_frame, text=f"Resolution: {awol[4]}").grid(row=row, column=4, sticky="w")
            row += 1

    # Create the Behaviors tab with input fields for events
    def create_behaviors_tab(self):
        self.behaviors_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.behaviors_tab, text="Behaviors")

        # Form fields for behavior entry
        tk.Label(self.behaviors_tab, text="Date:").grid(row=0, column=0, sticky="e")
        self.behavior_date_entry = tk.Entry(self.behaviors_tab)
        self.behavior_date_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.behaviors_tab, text="Time:").grid(row=1, column=0, sticky="e")
        self.behavior_time_entry = tk.Entry(self.behaviors_tab)
        self.behavior_time_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.behaviors_tab, text="Cause:").grid(row=2, column=0, sticky="e")
        self.behavior_cause_entry = tk.Entry(self.behaviors_tab)
        self.behavior_cause_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.behaviors_tab, text="Summary:").grid(row=3, column=0, sticky="ne")
        self.behavior_summary_text = tk.Text(self.behaviors_tab, height=5, width=40)
        self.behavior_summary_text.grid(row=3, column=1, padx=10, pady=5)

        # Submit button for behavior entry
        self.behavior_submit_button = tk.Button(self.behaviors_tab, text="Submit Behavior", command=self.submit_behavior)
        self.behavior_submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Frame to display behavior records
        self.behaviors_frame = ttk.Frame(self.behaviors_tab)
        self.behaviors_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.load_behaviors()

    # Handle behavior submission
    def submit_behavior(self):
        date = self.behavior_date_entry.get()
        time = self.behavior_time_entry.get()
        cause = self.behavior_cause_entry.get()
        summary = self.behavior_summary_text.get("1.0", tk.END).strip()

        # Here you would add the code to insert this information into your database
        # For now, we'll just print it to confirm the input
        print(f"Behavior Record Submitted:\nDate: {date}\nTime: {time}\nCause: {cause}\nSummary: {summary}")

        # Clear the input fields after submission
        self.behavior_date_entry.delete(0, tk.END)
        self.behavior_time_entry.delete(0, tk.END)
        self.behavior_cause_entry.delete(0, tk.END)
        self.behavior_summary_text.delete("1.0", tk.END)

        # Reload the behavior data to reflect the new entry
        self.load_behaviors()

    # Load behavior records from the database and display them
    def load_behaviors(self):
        behaviors = get_behaviors()
        row = 0
        for behavior in behaviors:
            tk.Label(self.behaviors_frame, text=f"Client: {behavior[0]}").grid(row=row, column=0, sticky="w")
            tk.Label(self.behaviors_frame, text=f"Date: {behavior[1]}").grid(row=row, column=1, sticky="w")
            tk.Label(self.behaviors_frame, text=f"Behavior: {behavior[2]}").grid(row=row, column=2, sticky="w")
            tk.Label(self.behaviors_frame, text=f"Duration: {behavior[3]} mins").grid(row=row, column=3, sticky="w")
            tk.Label(self.behaviors_frame, text=f"Resolution: {behavior[4]}").grid(row=row, column=4, sticky="w")
            row += 1

    def create_all_clients_tab(self):
        self.all_clients_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.all_clients_tab, text="All Clients")

        self.client_list_frame = ttk.Frame(self.all_clients_tab)
        self.client_list_frame.grid(row=0, column=0, padx=10, pady=10)

        self.load_all_clients()

    def load_all_clients(self):
        clients = get_clients()
        row = 0
        for client in clients:
            tk.Label(self.client_list_frame, text=f"Name: {client[1]} {client[2]}").grid(row=row, column=0, sticky="w")
            tk.Label(self.client_list_frame, text=f"DOB: {client[3]}").grid(row=row, column=1, sticky="w")
            tk.Label(self.client_list_frame, text=f"Age: {client[4]}").grid(row=row, column=2, sticky="w")
            tk.Label(self.client_list_frame, text=f"Weight: {client[5]}").grid(row=row, column=3, sticky="w")
            tk.Label(self.client_list_frame, text=f"SSN: {client[6]}").grid(row=row, column=4, sticky="w")
            tk.Label(self.client_list_frame, text=f"Diagnosis: {client[7]}").grid(row=row, column=5, sticky="w")
            row += 1

    def create_appointments_tab(self):
        self.appointments_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.appointments_tab, text="Appointments")

        self.appointments_frame = ttk.Frame(self.appointments_tab)
        self.appointments_frame.grid(row=0, column=0, padx=10, pady=10)

        self.load_appointments()

    def load_appointments(self):
        appointments = get_appointments()
        row = 0
        for appointment in appointments:
            tk.Label(self.appointments_frame, text=f"Client ID: {appointment[0]}").grid(row=row, column=0, sticky="w")
            tk.Label(self.appointments_frame, text=f"Date: {appointment[1]}").grid(row=row, column=1, sticky="w")
            tk.Label(self.appointments_frame, text=f"Purpose: {appointment[2]}").grid(row=row, column=2, sticky="w")
            tk.Label(self.appointments_frame, text=f"Doctor: {appointment[3]}").grid(row=row, column=3, sticky="w")
            row += 1

    def create_medications_tab(self):
        self.medications_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.medications_tab, text="Medications")

        self.medications_frame = ttk.Frame(self.medications_tab)
        self.medications_frame.grid(row=0, column=0, padx=10, pady=10)

        self.load_medications()

    def load_medications(self):
        medications = get_medications()
        row = 0
        for med in medications:
            tk.Label(self.medications_frame, text=f"Client: {med[0]}").grid(row=row, column=0, sticky="w")
            tk.Label(self.medications_frame, text=f"Medication: {med[1]}").grid(row=row, column=1, sticky="w")
            tk.Label(self.medications_frame, text=f"Dosage: {med[2]}").grid(row=row, column=2, sticky="w")
            tk.Label(self.medications_frame, text=f"Time: {med[3]}").grid(row=row, column=3, sticky="w")
            row += 1

    def create_search_tab(self):
        self.search_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.search_tab, text="Search")

        # Search form layout
        search_label = tk.Label(self.search_tab, text="Search Clients", font=("Helvetica", 16))
        search_label.grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.search_tab, text="First Name:").grid(row=1, column=0, sticky="e")
        self.first_name_entry = tk.Entry(self.search_tab)
        self.first_name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.search_tab, text="Last Name:").grid(row=2, column=0, sticky="e")
        self.last_name_entry = tk.Entry(self.search_tab)
        self.last_name_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.search_tab, text="Date of Birth:").grid(row=3, column=0, sticky="e")
        self.dob_entry = tk.Entry(self.search_tab)
        self.dob_entry.grid(row=3, column=1, padx=10, pady=5)

        search_button = tk.Button(self.search_tab, text="Search", command=self.search_clients)
        search_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.search_results_frame = ttk.Frame(self.search_tab)
        self.search_results_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def search_clients(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        dob = self.dob_entry.get()

        results = search_clients(first_name, last_name, dob)

        # Clear previous search results
        for widget in self.search_results_frame.winfo_children():
            widget.destroy()

        if results:
            client_id = results[0][0]
            client_info = f"Name: {results[0][1]} {results[0][2]}\nDOB: {results[0][3]}\nAge: {results[0][4]}\nWeight: {results[0][5]}\nSSN: {results[0][6]}\nDiagnosis: {results[0][7]}"
            
            # Display client info
            tk.Label(self.search_results_frame, text=client_info, font=("Helvetica", 14), justify="left").grid(row=0, column=0, sticky="w", padx=10, pady=5)

            # Fetch and display related data
            self.display_related_data(client_id)
        else:
            tk.Label(self.search_results_frame, text="No results found.", font=("Helvetica", 14)).grid(row=0, column=0, sticky="w")

    def display_related_data(self, client_id):
        # Get and display appointments
        appointments = get_appointments()
        if appointments:
            tk.Label(self.search_results_frame, text="\nAppointments:", font=("Helvetica", 14, "bold")).grid(row=1, column=0, sticky="w", padx=10, pady=5)
            for idx, appointment in enumerate(appointments, start=2):
                tk.Label(self.search_results_frame, text=f"  - Date: {appointment[1]}, Doctor: {appointment[3]}, Purpose: {appointment[2]}", font=("Helvetica", 12)).grid(row=idx, column=0, sticky="w", padx=20)

        # Get and display behaviors
        behaviors = get_behaviors()
        if behaviors:
            tk.Label(self.search_results_frame, text="\nBehaviors:", font=("Helvetica", 14, "bold")).grid(row=len(appointments)+2, column=0, sticky="w", padx=10, pady=5)
            for idx, behavior in enumerate(behaviors, start=len(appointments)+3):
                tk.Label(self.search_results_frame, text=f"  - Date: {behavior[1]}, Behavior: {behavior[2]}, Duration: {behavior[3]} mins, Resolution: {behavior[4]}", font=("Helvetica", 12)).grid(row=idx, column=0, sticky="w", padx=20)

        # Get and display AWOL incidents
        awol_records = get_awol()
        if awol_records:
            tk.Label(self.search_results_frame, text="\nAWOL Incidents:", font=("Helvetica", 14, "bold")).grid(row=len(appointments)+len(behaviors)+3, column=0, sticky="w", padx=10, pady=5)
            for idx, awol in enumerate(awol_records, start=len(appointments)+len(behaviors)+4):
                tk.Label(self.search_results_frame, text=f"  - Date: {awol[1]}, Time: {awol[2]}, Cause: {awol[3]}, Resolution: {awol[4]}", font=("Helvetica", 12)).grid(row=idx, column=0, sticky="w", padx=20)

        # Get and display medications
        medications = get_medications()
        if medications:
            tk.Label(self.search_results_frame, text="\nMedications:", font=("Helvetica", 14, "bold")).grid(row=len(appointments)+len(behaviors)+len(awol_records)+4, column=0, sticky="w", padx=10, pady=5)
            for idx, med in enumerate(medications, start=len(appointments)+len(behaviors)+len(awol_records)+5):
                tk.Label(self.search_results_frame, text=f"  - Medication: {med[1]}, Dosage: {med[2]}, Time: {med[3]}", font=("Helvetica", 12)).grid(row=idx, column=0, sticky="w", padx=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("EHOH Client Database")
    role = "admin"  # Example role, modify as needed
    main_screen = MainScreen(root, role)
    main_screen.pack(fill="both", expand=True)
    root.mainloop()
