import json
import os


class FruitManager:
    def __init__(self, log_file='transactions.log'):
        """Initialize the FruitManager with an empty inventory and log file."""
        self.fruits = {}  # Dictionary to store fruit information
        self.log_file = log_file
        self.load_fruits()  # Load fruits from file if available

    def load_fruits(self):
        """Load fruit data from a JSON file if it exists."""
        if os.path.exists('fruits.json'):
            with open('fruits.json', 'r') as file:
                self.fruits = json.load(file)

    def save_fruits(self):
        """Save the current fruit inventory to a JSON file."""
        with open('fruits.json', 'w') as file:
            json.dump(self.fruits, file)

    def log_transaction(self, message):
        """Log transaction details to a log file."""
        with open(self.log_file, 'a') as log:
            log.write(f"{message}\n")

    def add_fruit(self, fruit_name, KG, price_per_unit):
        """Add a new fruit to the inventory or update an existing fruit's stock."""
        if fruit_name in self.fruits:
            self.fruits[fruit_name]['KG'] += KG
            self.fruits[fruit_name]['price'] = price_per_unit
            action = "Updated"
        else:
            self.fruits[fruit_name] = {'KG': KG, 'price': price_per_unit}
            action = "Added"

        self.save_fruits()
        self.log_transaction(f"{action} {fruit_name}: {KG} at {price_per_unit:.2f} each.")
        print(f"Successfully {action.lower()} {fruit_name}: {KG} at {price_per_unit:.2f} each.")

    def view_fruits(self):
        """Display all available fruits in the inventory."""
        if not self.fruits:
            print("No fruits available in stock.")
            return

        print("Available Fruits:")
        for fruit, details in self.fruits.items():
            print(f"{fruit}: KG = {details['KG']}, Price = {details['price']:.2f}")

    def update_fruit_stock(self, fruit_name, KG):
        """Update the stock of an existing fruit."""
        if fruit_name in self.fruits:
            self.fruits[fruit_name]['KG'] += KG
            self.save_fruits()
            self.log_transaction(f"Updated {fruit_name}: New KG = {self.fruits[fruit_name]['KG']}.")
            print(f"Successfully updated {fruit_name}: New KG = {self.fruits[fruit_name]['KG']}.")
        else:
            print("Fruit not found in inventory.")
