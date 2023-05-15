class Customer:
    def __init__(self, fruit_manager, customer_name):
        self.fruit_manager = fruit_manager
        self.customer_name = customer_name
        self.cart = {}

    def add_to_cart(self, fruit_name, quantity):
        if fruit_name in self.fruit_manager.view_fruit_stock() and self.fruit_manager.view_fruit_stock()[fruit_name]['quantity'] >= quantity:
            if fruit_name in self.cart:
                self.cart[fruit_name] += quantity
            else:
                self.cart[fruit_name] = quantity
            print(f"{quantity} {fruit_name}(s) added to the cart.")
        else:
            print("Invalid fruit or insufficient quantity.")

    def view_cart(self):
        return self.cart

    def calculate_total(self):
        total = 0.0
        for fruit_name, quantity in self.cart.items():
            price = self.fruit_manager.get_fruit_price(fruit_name)
            total += price * quantity
        print(f"Total amount: {total}")

    def clear_cart(self):
        self.cart.clear()





   






