import tkinter as tk
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk

# --- Item Classes ---

class MenuItem:
    def __init__(self, name, price, image_path=None):
        self.name = name
        self.price = price
        self.image_path = image_path 

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
                HotDrink("Latte", 4.40, f"./Latte.jpg"),
                HotDrink("Drip", 3.00,f"./Drip.jpg" ),
                HotDrink("Macchiato", 3.75, f"./Macchiato.jpg"),
                HotDrink("Red Eye", 4.00, f"./RedEye.jpg"),
                HotDrink("Traditional Espresso", 2.85, f"./TraditionalEspresso.jpg"),
                HotDrink("Cappuccino", 4.40, f"./Cappuccino.jpg" ),
                HotDrink("Cafe Americano", 3.45, f"./CafeAmericano.jpg"),
                HotDrink("Cafe Con Leche", 4.65,f"./CafeConLeche.jpg" ),
                HotDrink("Cafe Au Lait", 4.00, f"./CafeAuLait.jpg"),
                HotDrink("Espresso Con Panna", 3.10,f"./EspressoConPanna.jpg" ),
                HotDrink("Cuban Espresso", 3.10,f"./CubanEspresso.jpg" ),
                HotDrink("Cortado", 3.50,f"./Cortado.jpg" )
            ]),
            ("Signature Lattes", [
                SignatureLattes("Cookie Dough", 5.75,f"./CookieDough.jpg" ),
                SignatureLattes("Almond Joy", 5.75,f"./AlmondJoy.jpg" ),
                SignatureLattes("Lucky Goat", 5.75, f"./LuckyGoat.jpg"),
                SignatureLattes("Chunky Monkey", 5.75, f"./ChunkyMonkey.jpg"),
               SignatureLattes("S'mores", 5.75, f"./S'more.jpg"),
                SignatureLattes("Banana Foster", 5.75, f"./BananaFoster.jpg"),
                SignatureLattes("Turtle", 5.75, f"./Turtle.jpg"),
                SignatureLattes("Nutella", 5.75, f"./Nutella.jpg"),
                SignatureLattes("Mexican Mocha", 5.75, f"./MexicanMocha.jpg"),
                SignatureLattes("Honey Bee", 5.75, f"./HoneyBee.jpg"),
                SignatureLattes("Zebra", 5.75, f"./Zebra.jpg"),
                SignatureLattes("Fight Club", 5.75, f"./FightClub.jpg")
            ]),
        
            ("Food", [
                Food("Quiche of the Day", 10.35, f"./Quiche.jpg"),
                Food("French Toast Sticks", 6.95, f"./SipCoffeeHouseAndArtisanCafeFrenchToastSticks.jpg"),
                Food("Breakfast Grilled Cheese", 8.25, f"./SipCoffeeHouseAndArtisanBreakfastGrilledCheese.jpg"),
                Food("Old-Fashioned Oatmeal", 5.65, f"./OldFashionOats.jpg"),
                Food("The Hipster", 5.65, f"./SipCoffeeAndArtisanCafeHipster.jpg"),
                Food("Avocado Toast", 9.95, f"./SipCoffeeHouseAvocadoToast.jpg")
            ]),
        ]

        for idx, (label, items) in enumerate(categories):
            frame = tk.LabelFrame(parent, text=label, padx=10, pady=5)
            frame.grid(row=0, column=idx, padx=10)
            for item in items:
                b = tk.Button(frame, text=f"{item.name} - ${item.price:.2f}", 
                             command=lambda i=item: self.handle_item_click(i))
                b.pack(anchor='w', pady=2)

    def handle_item_click(self, item):
        # Add the item to the order
        self.add_to_order(item)
        
        # Also show the popup with image
        self.show_item_popup(item)
    
    def show_item_popup(self, item):
        # Create popup window
        popup = Toplevel(self.root)
        popup.title(item.name)
        popup.geometry("300x350")  # Size of popup window
        
        # Try to display the image
        if hasattr(item, 'image_path') and item.image_path:
            try:
                # Load and resize the image
                img = Image.open(item.image_path)
                img = img.resize((250, 250), Image.LANCZOS)  # Resize for display
                photo = ImageTk.PhotoImage(img)
                
                # Display image
                img_label = tk.Label(popup, image=photo)
                img_label.image = photo  # Keep a reference to prevent garbage collection
                img_label.pack(pady=10)
            except Exception as e:
                print(f"Error loading image {item.image_path}: {e}")
                tk.Label(popup, text="Image not available").pack(pady=10)
        
        # Display item name and price
        tk.Label(popup, text=item.name, font=("Helvetica", 16, "bold")).pack()
        tk.Label(popup, text=f"Price: ${item.price:.2f}", font=("Helvetica", 14)).pack()
        
        # Add button to close popup
        tk.Button(popup, text="Close", command=popup.destroy).pack(pady=10)

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