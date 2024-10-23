import db

def banker_menu():
    while True:
        print("\n--- Banker Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Update Customers")
        print("4. View Customers")
        print("5. Delete Customer")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register_banker()
        elif choice == '2':
            login_banker()
        elif choice == '3':
            update_customers()
        elif choice == '4':
            view_customers()
        elif choice == '5':
            delete_customer()
        elif choice == '6':
            break
        else:
            print("Invalid choice! Please try again.")

def customer_menu():
    while True:
        print("\n--- Customer Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Withdraw Amount")
        print("4. Deposit Amount")
        print("5. View Balance")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register_customer()
        elif choice == '2':
            login_customer()
        elif choice == '3':
            withdraw_amount()
        elif choice == '4':
            deposit_amount()
        elif choice == '5':
            view_balance()
        elif choice == '6':
            break
        else:
            print("Invalid choice! Please try again.")

def register_banker():
    username = input("Enter banker username: ")
    password = input("Enter banker password: ")

    conn = db.create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bankers (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    cursor.close()
    conn.close()
    print("Banker registered successfully.")

def login_banker():
    username = input("Enter banker username: ")
    password = input("Enter banker password: ")

    conn = db.create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bankers WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        print("Login successful.")
        banker_menu()
    else:
        print("Invalid username or password.")

def update_customers():
    conn = db.create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    for customer in customers:
        print(customer)

    customer_id = int(input("Enter the customer ID to update: "))
    new_balance = float(input("Enter new balance: "))
    cursor.execute("UPDATE customers SET balance=%s WHERE id=%s", (new_balance, customer_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Customer updated successfully.")

def view_customers():
    conn = db.create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    for customer in customers:
        print(customer)
    cursor.close()
    conn.close()

def delete_customer():
    customer_id = int(input("Enter the customer ID to delete: "))
    conn = db.create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE id=%s", (customer_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Customer deleted successfully.")

def register_customer():
    username = input("Enter customer username: ")
    password = input("Enter customer password: ")

    conn = db.create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    cursor.close()
    conn.close()
    print("Customer registered successfully.")

def login_customer():
    username = input("Enter customer username: ")
    password = input("Enter customer password: ")

    conn = db.create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        print("Login successful.")
        customer_menu()
    else:
        print("Invalid username or password.")

def withdraw_amount():
    username = input("Enter your username: ")
    amount = float(input("Enter amount to withdraw: "))
    
    conn = db.create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE customers SET balance = balance - %s WHERE username = %s AND balance >= %s", (amount, username, amount))
    if cursor.rowcount > 0:
        conn.commit()
        print("Withdrawal successful.")
    else:
        print("Insufficient funds or user not found.")
    cursor.close()
    conn.close()

def deposit_amount():
    username = input("Enter your username: ")
    amount = float(input("Enter amount to deposit: "))
    
    conn = db.create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE customers SET balance = balance + %s WHERE username = %s", (amount, username))
    conn.commit()
    cursor.close()
    conn.close()
    print("Deposit successful.")

def view_balance():
    username = input("Enter your username: ")
    
    conn = db.create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM customers WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        print(f"Your balance is: {result[0]}")
    else:
        print("User not found.")

if __name__ == "__main__":
    while True:
        print("\n--- Welcome to the Banking Application ---")
        print("1. Banker")
        print("2. Customer")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            banker_menu()
        elif choice == '2':
            customer_menu()
        elif choice == '3':
            break
        else:
            print("Invalid choice! Please try again.")
