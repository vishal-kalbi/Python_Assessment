import logging
from fruit_manager import FruitManager
from customer import Customer
import datetime

# Configure logging
logging.basicConfig(filename='transactions.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def main():
    fruit_manager = FruitManager()
    customer = None

    while True:
        print("\n===== FRUIT STORE MENU =====")
        print("1. Manager")
        print("2. Customer")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':  # Manager
            while True:
                print("\n===== MANAGER MENU =====")
                print("1. Add Fruit Stock")
                print("2. View Fruit Stock")
                print("3. Update Fruit Stock")
                print("4. Back to Main Menu")

                manager_choice = input("Enter your choice: ")

                if manager_choice == '1':  # Add Fruit Stock
                    fruit_name = input("Enter the fruit name: ")
                    quantity = int(input("Enter the quantity: "))
                    price = float(input("Enter the price: "))

                    fruit_manager.add_fruit_stock(fruit_name, quantity, price)
                    print(f"{quantity} {fruit_name}(s) added to the stock.")

                elif manager_choice == '2':  # View Fruit Stock
                    stock = fruit_manager.view_fruit_stock()
                    print("\n=== Available Fruit Stock ===")
                    for fruit_name, details in stock.items():
                        print(f"{fruit_name}: Quantity - {details['quantity']}, Price - {details['price']}")

                elif manager_choice == '3':  # Update Fruit Stock
                    fruit_name = input("Enter the fruit name: ")
                    quantity = int(input("Enter the updated quantity: "))

                    if fruit_manager.update_fruit_stock(fruit_name, quantity):
                        print(f"{fruit_name} stock updated successfully.")
                    else:
                        print(f"{fruit_name} not found in stock.")

                elif manager_choice == '4':  # Back to Main Menu
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == '2':  # Customer
            customer_name = input("Enter your name: ")
            customer = Customer(fruit_manager, customer_name)

            while True:
                print("\n===== CUSTOMER MENU =====")
                print("1. Show Available Fruits")
                print("2. Add to Cart")
                print("3. View Cart")
                print("4. Checkout")
                print("5. Back to Main Menu")

                customer_choice = input("Enter your choice: ")
                
                if customer_choice == '1':  # Show Available Fruits
                    available_fruits = fruit_manager.show_available_fruits()
                    print("\n=== Available Fruits ===")
                    for fruit in available_fruits:
                        print(fruit)

                elif customer_choice == '2':
                    global cart
                    cart = {}  # Add to Cart
                    fruit_name = input("Enter the fruit name: ")
                    quantity = int(input("Enter the quantity: "))
                    cart[fruit_name] = quantity

                    customer.add_to_cart(fruit_name, quantity)

                elif customer_choice == '3':  # View Cart
                    cart = customer.view_cart()
                    print("\n=== Your Cart ===")
                    for fruit_name, quantity in cart.items():
                        print(f"{fruit_name}: {quantity}")

                elif customer_choice == '4':  # Checkout
                    customer.calculate_total()
                    logging.info(f"Customer: {customer_name}, Cart: {cart}")
                    customer.clear_cart()

                    break

                elif customer_choice == '5': 
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif choice == '3':  # Exit
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
 # Back to Main Menu
                   










