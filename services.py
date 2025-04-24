import mysql.connector as mc

class Service:
    def __init__(self):
        self.mydb = mc.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "store_bill"
            )
        self.mycursor = self.mydb.cursor()

    def insert_service(self): #Inserting new service
        try:
            service_code = input("Item code in two letter: ").strip()
            if not service_code and service_code.length() ==2: #Ensures two letters for service code 
                raise ValueError("Item code must be filled with alphabet.")
            service = input("Item name: ").strip()
            if not service:
                raise ValueError("Name field must be filled with alphabet.")
            cost_price = input("Cost Price: ")
            if not cost_price:
                raise ValueError("Cost price is mandatory.")
            maintenance_price = input("Mainteneance price in two letter: ")
            if not maintenance_price:
                raise ValueError("Maintenance price is mandatory.")
            sql = "INSERT INTO cost_calculation (`service_code`, `service`, `cost_price`, `maintenance_cost`) VALUES (%s, %s, %s, %s)"
            values = (service_code, service, cost_price, maintenance_price)
            self.mycursor.execute(sql, values)
            self.mydb.commit()
            print(f"Successfully '{service}' added.")
        
        except Exception as e:
            print(f"Fix the error {e}")
            self.mydb.rollback()
    

    def update_service(self): #Remain to work to reduce security risks.
        try:
            query = input("Type 'service_code' or 'service' to update: ")
            selection = input(f"Which {query} do you want to update: ")
            """Start your work from here..."""
            
            change_column = input("Type name or address or contact or sex to update Name, Address, Contact, and Sex: ")
            change_value = input(f"Type the {change_column} of account number {account_number} to change: ")
            sql = f"UPDATE customer_info SET {change_column} = %s WHERE account_no = %s"
            values = (change_value, account_number)
            self.mycursor.execute(sql, values)
            self.mydb.commit()
            print(f"Successfully {change_column} updated to {change_value} of account number {account_number}.") 

        except Exception as e:
            print(f"Fix the error {e}")
            self.mydb.rollback()


    def close_connection(self):
        self.mycursor.close()
        self.mydb.close()

command = int(input("Press 1 to add item: "))

service = Service()
if command == 1:
    service.insert_service()
else:
    raise ValueError("Enter proper command in number.")