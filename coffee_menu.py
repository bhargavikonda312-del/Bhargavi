class Coffee:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items =[]
    def add_items(self,coffee):
        self.items.append(coffee)
        print(f"{coffee.name}added to your order.")
    def total(self):
        return sum (item.price for item in self.items)
    def show_order(self):
        if not self.items:
            print("No items in order.")
            return
        print("\n your order:")
        for i, item  in enumerate (self.items, 1):
             print(f"{i}.{item.name} - ${item.price}")
        print(f"Total:${self.total()}\n")
    def checkout(self):
        if not self.items:
            print("your cart is empty.")
            return
        self.show_order()
        confirm = input("Procced to checkout?(yes/no):").strip().lower()
        if confirm == 'yes':
            print("Order confirmed! Thank you.")
            self.items.clear()
        else:
            print("Checkout cancelled.")

def main():
    menu = [
        Coffee("Espresso", 2.5),
        Coffee("Latte", 3.5),
        Coffee("cappuccino", 3.0),
        Coffee("Americano", 3.0)
    ]
    order = Order()
    while True:
        print("\n-----Coffee Menu-----")
        for i ,coffee in enumerate(menu,1):
            print(f"{i}.{coffee.name} - ${coffee.price}")
        print("5.view Order")
        print("6.Checkout")
        print("7.Exit")
        choice = input("Choose an option:").strip()

        if choice in['1','2','3','4']:
            order.add_item
        elif choice == '5':
            order.show_order()
        elif choice == '6':
            order.checkout()
        elif choice == '7':
            print("Thanks for Visting.Goodbye!")
            break
        else:
            print("Invalid choice . try again.")

