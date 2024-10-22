class Customer:
    def __init__(self, name):
        """Initialize the customer with a name and an empty cart."""
        self.name = name
        self.cart = {}  # Dictionary to store fruits added to the cart

    def add_to_cart(self, fruit_name, KG):
        """Add fruit to the customer's cart."""
        if fruit_name in self.cart:
            self.cart[fruit_name] += KG
        else:
            self.cart[fruit_name] = KG

        print(f"Added {KG} of {fruit_name} to cart.")

    def view_cart(self):
        """Display the contents of the customer's cart."""
        if not self.cart:
            print("Your cart is empty.")
            return

        print(f"{self.name}'s Cart:")
        for fruit, KG in self.cart.items():
            print(f"{fruit}: KG = {KG}")

    def checkout(self, fruit_manager):
        """Checkout the items in the cart and update fruit inventory."""
        total_cost = 0
        for fruit, KG in self.cart.items():
            if fruit in fruit_manager.fruits and fruit_manager.fruits[fruit]['KG'] >= KG:
                fruit_manager.update_fruit_stock(fruit, -KG)
                total_cost += fruit_manager.fruits[fruit]['price'] * KG
            else:
                print(f"Not enough {fruit} available to sell.")

        return total_cost
