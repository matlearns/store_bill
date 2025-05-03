from tkinter import ttk, messagebox
import mysql.connector as mc
import tkinter as tk #Leave as default for convinient

window = tk.Tk()

#Title bar text
window.title("Learners' Village: Account Management.")

# Customized default icon to my desire
window.iconbitmap('learners_village.ico')  # Replace with your icon path

# Window size
window.geometry("400x500") #geometry sets the height and width

class Service:
    def __init__(self):
        self.mydb = mc.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "store_bill"
            )
        self.mycursor = self.mydb.cursor()
    
    def insert_service(self):
        #Labels and entries
        
        #Label for service code
        tk.Label(window, text="Input 2 letters service code. It must be unique.").pack()
        service_code_entry = tk.Entry(window)
        service_code_entry.pack()

        #Label for service code
        tk.Label(window, text="Input service").pack()
        service_entry = tk.Entry(window)
        service_entry.pack()

        #Label for service code
        tk.Label(window, text="Input cost prices").pack()
        cost_price_entry = tk.Entry(window)
        cost_price_entry.pack()

        #Label for service code
        tk.Label(window, text="Input maintenance cost:").pack()
        maintenance_cost_entry = tk.Entry(window)
        maintenance_cost_entry.pack()

        def submit_entry():
            try:
                service_code = service_code_entry.get().strip()
                if not service_code and len(service_code) != 2:
                    raise ValueError("Service code length must be 2 letters.")
                
                service = service_entry.get().strip()
                if not service:
                    raise ValueError("Service must be filled.")
                
                cost_price = cost_price_entry.get().strip()
                if not cost_price:
                    raise ValueError("Cost price must be filled.")
                
                maintenance_cost = maintenance_cost_entry.get().strip()
                if not maintenance_cost:
                    raise ValueError("Maintenance cost price must be filled.")
                
                sql = "INSERT INTO cost_calculation (service_code, service, cost_price, maintenance_cost) VALUES (%s, %s, %s, %s);"
                values = (service_code, service, cost_price, maintenance_cost)
                self.mycursor.execute(sql, values)
                self.mydb.commit()
                tk.messagebox.showinfo(f"Successfully added {service}.")

            except Exception as e:
                tk.messagebox.showerror("Error", f"Fix the error: {e}")
                self.mydb.rollback() 
        
        # Submit button
        tk.Button(window, text="Add Service", command=submit_entry).pack(pady=10)   
    def view_service(self):
        # Fetch data
        self.mycursor.execute("SELECT service_code FROM cost_calculation")
        result = self.mycursor.fetchall()
        options = [row[0] for row in result]

        # Dropdown
        combo = ttk.Combobox(window, values=options)
        combo.pack(pady=20)
        
        #Message in screen
        message = tk.Label(window, text="Hello, Bipin! This is my first application to build in real life.")

        #Message shows in screen
        message.pack()

service = Service()
service.insert_service()


#This is also default. It handles continous clicks and other interactions
window.mainloop()