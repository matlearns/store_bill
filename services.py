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
            options = {
                '1': 'service_code',
                '2': 'service',
                '3': 'cost_price', #Update code: If i change the price of one item, all similar prices would change. Fix it in sql with adding an input field to identify which particular column you intended to change
                '4': 'maintenance_cost'
            }

            query = input("Enter 1 to change service code, 2 to service, 3 to cost price, and 4 to maintenance cost: "). strip()
            
            if query not in options:
                print("Value must be 1 to 4 entered.")
                return    
            
            column = options[query]
            old_value = input(f"What do you want to change of {column}: ").strip()
            new_value = input(f"What is your new value of {column}: ").strip()
            sql = f"UPDATE cost_calculation SET {column} = %s WHERE {column} = %s" #this sql cause serious issue by changing all price, where are data are not unique
            values = (new_value, old_value)
            self.mycursor.execute(sql, values)
            self.mydb.commit()
            print(f"Successfully updated {column} from {old_value} to {new_value}.") 

        except Exception as e:
            print(f"Fix the error {e}")
            self.mydb.rollback()


    def close_connection(self):
        self.mycursor.close()
        self.mydb.close()

command = int(input("Press 1 to add item, 2 to update item: "))

service = Service()
if command == 1:
    service.insert_service()
elif command ==2:
    service.update_service()

else:
    raise ValueError("Enter proper command in number.")