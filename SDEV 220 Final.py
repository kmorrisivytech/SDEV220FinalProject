import tkinter as tk
from tkinter import messagebox

# --- Item Classes ---

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class HotDrink(MenuItem): pass
class SignatureLattes(MenuItem): pass
class Food(MenuItem): pass

# --- Main Application ---

class SipCoffeeHousePOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Sip Coffee House POS")
        self.order = []
        self.total = 0.0

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Sip Coffee House", font=("Helvetica", 18, "bold")).pack(pady=10)

        # Frames for menu and order
        menu_frame = tk.Frame(self.root)
        menu_frame.pack(pady=10)

        order_frame = tk.Frame(self.root)
        order_frame.pack(pady=10)

        # Menu buttons
        self.create_menu_buttons(menu_frame)

        # Order display
        self.order_listbox = tk.Listbox(order_frame, width=50)
        self.order_listbox.pack()

        self.total_label = tk.Label(self.root, text="Total: $0.00", font=("Helvetica", 14))
        self.total_label.pack(pady=5)

        # Clear and Checkout buttons
        tk.Button(self.root, text="Clear Order", command=self.clear_order).pack(pady=5)
        tk.Button(self.root, text="Checkout", command=self.checkout).pack(pady=5)

    def create_menu_buttons(self, parent):
        categories = [
            ("Hot Drinks", [
                HotDrink("Latte", 4.40),
                HotDrink("Drip", 3.00),
                HotDrink("Macchiato", 3.75),
                HotDrink("Red Eye", 4.00),
                HotDrink("Traditional Espresso", 2.85),
                HotDrink("Cappuccino", 4.40),
                HotDrink("Cafe Americano", 3.45),
                HotDrink("Cafe Con Leche", 4.65),
                HotDrink("Cafe Au Lait", 4.00),
                HotDrink("Espresso Con Panna", 3.10),
                HotDrink("Cuban Espresso", 3.10),
                HotDrink("Cortado", 3.50)
            ]),
            ("Signature Lattes", [
                SignatureLattes("Cookie Dough", 5.75),
                SignatureLattes("Almond Joy", 5.75),
                SignatureLattes("Lucky Goat", 5.75),
                SignatureLattes("Chunky Monkey", 5.75),
                SignatureLattes("S'mores", 5.75),
                SignatureLattes("Banana Foster", 5.75),
                SignatureLattes("Turtle", 5.75),
                SignatureLattes("Nutella", 5.75),
                SignatureLattes("Mexican Mocha", 5.75),
                SignatureLattes("Honey Bee", 5.75),
                SignatureLattes("Zebra", 5.75),
                SignatureLattes("Fight Club", 5.75)
            ]),
            ("Food", [
                Food("Quiche of the Day", 10.35),
                Food("French Toast Sticks", 6.95),
                Food("Breakfast Grilled Cheese", 8.25),
                Food("Old-Fashioned Oatmeal", 5.65),
                Food("The Hipster", 5.65),
                Food("Avocado Toast", 9.95)
            ]),
        ]

        for idx, (label, items) in enumerate(categories):
            frame = tk.LabelFrame(parent, text=label, padx=10, pady=5)
            frame.grid(row=0, column=idx, padx=10)
            for item in items:
                b = tk.Button(frame, text=f"{item.name} - ${item.price:.2f}", command=lambda i=item: self.add_to_order(i))
                b.pack(anchor='w', pady=2)

    def add_to_order(self, item):
        self.order.append(item)
        self.total += item.price
        self.order_listbox.insert(tk.END, f"{item.name} - ${item.price:.2f}")
        self.total_label.config(text=f"Total: ${self.total:.2f}")

    def clear_order(self):
        self.order.clear()
        self.total = 0.0
        self.order_listbox.delete(0, tk.END)
        self.total_label.config(text="Total: $0.00")
        messagebox.showinfo("Order Cleared", "The order has been cleared.")

    def checkout(self):
        messagebox.showinfo("Checkout", f"Total amount due: ${self.total:.2f}")

# --- Run the app ---

if __name__ == "__main__":
    root = tk.Tk()
    app = SipCoffeeHousePOS(root)
    root.mainloop()
