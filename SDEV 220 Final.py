import tkinter as tk
from tkinter import messagebox

# --- Item Classes ---

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class HotDrink(MenuItem): pass
class ColdDrink(MenuItem): pass
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

        tk.Button(self.root, text="Clear Order", command=self.clear_order).pack(pady=5)

    def create_menu_buttons(self, parent):
        categories = [
            ("Hot Drinks", [HotDrink("Latte", 3.50), HotDrink("Espresso", 2.50), HotDrink("Cappuccino", 3.75)]),
            ("Cold Drinks", [ColdDrink("Iced Coffee", 3.00), ColdDrink("Cold Brew", 3.50), ColdDrink("Iced Latte", 4.00)]),
            ("Food", [Food("Bagel", 2.00), Food("Croissant", 2.50), Food("Muffin", 2.25)])
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

# --- Run the app ---

if __name__ == "__main__":
    root = tk.Tk()
    app = SipCoffeeHousePOS(root)
    root.mainloop()