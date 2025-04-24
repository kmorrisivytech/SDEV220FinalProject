import tkinter as tk
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk #Allows you to resize image

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
        self.images = {} 
        self.create_widgets()

    def create_widgets(self):
        title_frame = tk.Frame(self.root)
        title_frame.pack(pady=10)

        icon = tk.PhotoImage(file="./coffee.png")
        trash_icon = ImageTk.PhotoImage(Image.open("./trash.png").resize((20, 20)))
        cart_icon = ImageTk.PhotoImage(Image.open("./cart.png").resize((20, 20)))
        self.images["logo"] = icon  # keep reference
        self.images["trash"] = trash_icon
        self.images["cart"] = cart_icon

        tk.Label(title_frame, image=icon ).pack(side="left", padx=(0, 10))

        tk.Label(
            title_frame,
            text="Sip Coffee House",
            font=("Helvetica", 18, "bold")
        ).pack(side="left")

        # Creates menu frame, this holds all three menu categorys: Hot Drinks, Signature Lattes, Food
        menu_frame = tk.Frame(
            self.root,
            bg="#f7f1e3",     # Light coffee-ish background
            bd=3,             # Border width
            relief="groove",  # Border style: ridge, sunken, groove, etc.
            padx=15,          # Internal padding left/right
            pady=15           # Internal padding top/bottom
        )
        menu_frame.pack(pady=10) 

        # Creates order container that holds the order frame
        order_container = tk.Frame(
            self.root, 
            bg="#f7f1e3",
            bd=3,
            relief="groove",
            padx=10,
            pady=10
        )

        order_container.pack(pady=10)

        tk.Label(
            order_container,
            text="Your Order: ",
            font=("Helvetica", 14, "bold"),
            bg="#f7f1e3",
            anchor="w"
        ).pack(anchor="w")

        # Creates order frame
        order_frame = tk.Frame(
            order_container,
            bg="#fbf8f2",       # background of the frame
            bd=2,               # border width
            relief="groove",    # border style: ridge, groove, sunken, etc.
        )

        order_frame.pack(fill="x", pady=5)

        scrollbar = tk.Scrollbar(order_frame)
        scrollbar.pack(side="right", fill="y")

        # Creates the menu items/buttons for each menu category.
        self.create_menu_buttons(menu_frame)

        # Order display
        self.order_listbox = tk.Listbox(
            order_frame,
            width=50,
            height=6,
            bg="#fbf8f2", 
            fg="#3e2f2f",
            font=("Helvetica", 10),
            relief="flat",
        )

        self.order_listbox.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=self.order_listbox.yview)




        order_info_frame = tk.Frame(
            order_container,
            bg="#fbf8f2", 
            bd=0,      # background of the frame
        )

        order_info_frame.pack(side="left", padx=0, pady=0)

        # Created buttons for clearing order and checking out order
        tk.Button(
            order_info_frame,
            text=" Checkout",
            image=self.images["cart"],
            compound="left",
            command=self.checkout
        ).pack(side="left", padx=5)

        tk.Button(
            order_info_frame,
            text=" Clear Order", 
            image=self.images["trash"],
            compound="left",
            command=self.clear_order
        ).pack(side="left", padx=5)

        self.total_label = tk.Label(order_info_frame, text="Total: $0.00", bg="#f7f1e3", font=("Helvetica", 14))
        self.total_label.pack(padx=5)

    def create_menu_buttons(self, parent):
        categories = categories = [
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
            #Creates each menu
            frame = tk.Frame(
                parent,
                bg="#f7f1e3",
                height=1   
            )
            frame.grid(row=0, column=idx, padx=20, sticky="n") # Formats each menu to display the buttons vertically, have a left/right padding, and align to the top
            
            #Creates the title for each menu ex: Hot Drinks
            title = tk.Label(
                frame,
                text=label,
                font=("Helvetica", 12, "bold"),
                anchor="w", 
                bg="#f7f1e3",
                pady=5
            )

            title.pack(anchor="w")

            divider = tk.Frame(frame, height=2, bg="#000", bd=0)
            divider.pack(fill="x", pady=(0, 5))

            for item in items: #For loop that creates the items in each menu
                item_frame = tk.Frame(frame, bg="#faf3e0", bd=1, relief="raised", cursor="hand2")
                item_frame.pack(fill="x", padx=0, pady=2)

                # Item Label
                name_label = tk.Label(item_frame, text=item.name, bg="#faf3e0", anchor="w", font=("Helvetica", 10), width=20)
                name_label.pack(side="left", fill="x", expand=True, padx=(5, 0))

                # Item Price
                price_label = tk.Label(item_frame, text=f"${item.price:.2f}", bg="#faf3e0", anchor="e", font=("Helvetica", 10, "bold"), width=5)
                price_label.pack(side="right", padx=(0, 5))

                # Hacky fix to make sure clicking any part of the button opens the menu
                item_frame.bind("<Button-1>", lambda e, i=item: self.handle_item_click(i))
                name_label.bind("<Button-1>", lambda e, i=item: self.handle_item_click(i))
                price_label.bind("<Button-1>", lambda e, i=item: self.handle_item_click(i))



    def handle_item_click(self, item):
        self.show_item_popup(item)
    
    def show_item_popup(self, item):
        # Create popup window
        popup = Toplevel(self.root)
        popup.title(item.name)
        popup.geometry("300x340")  # Size of popup window
        
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
                img_label.pack()
            except Exception as e:
                print(f"Error loading image {item.image_path}: {e}")
                tk.Label(popup, text="Image not available").pack(pady=10)

        popup_buttons_frame = tk.Frame(
            popup,
            bd=0,      # background of the frame
        )

        popup_buttons_frame.pack(padx=20)

        # Display item name and price
        tk.Label(popup_buttons_frame, text=f"{item.name} - ${item.price:.2f}", font=("Helvetica", 16, "bold")).pack()
        
        # Button to add order (with padding-right)
        tk.Button(
            popup_buttons_frame,
            width=15,
            text="Order",
            command=lambda i=item: self.add_to_order(i)
        ).pack(side="left", padx=(0, 10), pady=8)  # ← padding only on right

        # Button to close (with padding-left)
        tk.Button(
            popup_buttons_frame,
            width=15,
            text="Close",
            command=popup.destroy
        ).pack(side="left", padx=(10, 0), pady=8)  # ← padding only on left

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
