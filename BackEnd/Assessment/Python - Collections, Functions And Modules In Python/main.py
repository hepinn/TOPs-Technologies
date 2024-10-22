from manager import FruitManager
from customer import Customer


def display_menu():
    """Display the main menu options."""
    print("\n--- Tops Technologies Fruit Store Menu ---")
    print("1. Add Fruit")
    print("2. Customer")
    print("3. Update Fruit Stock")
    print("4. View Fruits")
    print("5. Exit")

def get_integer_input(prompt):
    """Get a valid integer input from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_float_input(prompt):
    """Get a valid float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    fruit_manager = FruitManager()  # Create an instance of FruitManager

    while True:
        display_menu()  # Show the menu options
        choice = input("Select an option (1-5): ")

        if choice == '1':
            fruit_name = input("Enter fruit name: ")
            KG = get_integer_input("Enter KG: ")
            price_per_KG = get_float_input("Enter price per KG: ")
            fruit_manager.add_fruit(fruit_name, KG, price_per_KG)  # Add or update fruit

        elif choice == '2':
            customer_name = input("Enter your name: ")
            customer = Customer(customer_name)  # Create a new customer

            while True:
                fruit_name = input("Enter fruit to add to cart (or type 'exit' to finish): ")
                if fruit_name.lower() == 'exit':
                    break
                KG = get_integer_input(f"Enter KG of {fruit_name} to add: ")
                customer.add_to_cart(fruit_name, KG)  # Add fruit to customer's cart

            customer.view_cart()  # View the cart
            total_cost = customer.checkout(fruit_manager)  # Checkout the cart
            if total_cost > 0:
                print(f"Total cost of purchase: ₹{total_cost:.2f}")
                
        elif choice == '3':
            fruit_name = input("Enter fruit name to update: ")
            KG = get_integer_input("Enter Kg to add: ")
            fruit_manager.update_fruit_stock(fruit_name, KG)
                
        elif choice == '4':
            fruit_manager.view_fruits()  # View all fruits

        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()  # Start the application
