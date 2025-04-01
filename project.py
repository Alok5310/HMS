import tkinter as tk
from tkinter import ttk, messagebox

class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = True

class Customer:
    def __init__(self, name, age, contact, room_number, total_bill):
        self.name = name
        self.age = age
        self.contact = contact
        self.room_number = room_number
        self.total_bill = total_bill

class Hotel:
    def __init__(self):
        self.rooms = [
            Room(101, "Single", 1000),
            Room(102, "Double", 2000),
            Room(103, "Suite", 3000),
            Room(104, "Single", 1000),
            Room(105, "Double", 2000)
        ]
        self.customers = {}

    def check_in(self, customer, room_number):
        for room in self.rooms:
            if room.room_number == room_number and room.is_available:
                room.is_available = False
                self.customers[customer.name] = customer
                return True
        return False

    def check_out(self, name):
        if name in self.customers:
            room_number = self.customers[name].room_number
            del self.customers[name]
            for room in self.rooms:
                if room.room_number == room_number:
                    room.is_available = True
                    return True, room_number
        return False, None

    def get_room_price(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.price_per_night, room.room_type
        return 0, "Unknown"

class HotelApp:
    def __init__(self, root, hotel):
        self.root = root
        self.hotel = hotel
        self.create_ui()

    def create_ui(self):
        self.root.title("Hotel Management System")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        for i in range(8):
            self.root.rowconfigure(i, weight=1)
        for i in range(2):
            self.root.columnconfigure(i, weight=1)

        ttk.Label(self.root, text="Select a Room:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.room_var = tk.StringVar()
        self.room_menu = ttk.Combobox(self.root, textvariable=self.room_var, values=[room.room_number for room in self.hotel.rooms])
        self.room_menu.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        self.room_menu.bind("<<ComboboxSelected>>", self.update_price)
        
        ttk.Label(self.root, text="Room Type:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.room_type_label = ttk.Label(self.root, text="Select a room", background="#f0f0f0")
        self.room_type_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.root, text="Room Price:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.price_label = ttk.Label(self.root, text="Select a room", background="#f0f0f0")
        self.price_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(self.root, text="Customer Name:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        ttk.Label(self.root, text="Customer Age:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.age_entry = ttk.Entry(self.root)
        self.age_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        ttk.Label(self.root, text="Contact:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.contact_entry = ttk.Entry(self.root)
        self.contact_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

        self.check_in_button = ttk.Button(self.root, text="Check In", command=self.check_in)
        self.check_in_button.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

        self.check_out_button = ttk.Button(self.root, text="Check Out", command=self.check_out)
        self.check_out_button.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

    def update_price(self, event=None):
        if self.room_var.get():
            room_number = int(self.room_var.get())
            price, room_type = self.hotel.get_room_price(room_number)
            self.price_label.config(text=f"₹{price}")
            self.room_type_label.config(text=f"{room_type}")

    def check_in(self):
        if not self.room_var.get():
            messagebox.showerror("Error", "Please select a room")
            return

        room_number = int(self.room_var.get())
        name = self.name_entry.get()
        age = self.age_entry.get()
        contact = self.contact_entry.get()
        price, room_type = self.hotel.get_room_price(room_number)

        if not name or not age or not contact:
            messagebox.showerror("Error", "Please fill all fields")
            return

        customer = Customer(name, int(age), contact, room_number, price)
        success = self.hotel.check_in(customer, room_number)

        if success:
            messagebox.showinfo("Check In", f"{name} checked into Room {room_number} ({room_type} - ₹{price} per night).")
        else:
            messagebox.showerror("Error", "Room is not available.")

    def check_out(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Error", "Please enter the customer's name to check out.")
            return

        success, room_number = self.hotel.check_out(name)

        if success:
            messagebox.showinfo("Check Out", f"{name} has checked out from Room {room_number}.")
        else:
            messagebox.showerror("Error", "Customer not found.")

if __name__ == "__main__":
    root = tk.Tk()
    hotel = Hotel()
    app = HotelApp(root, hotel)
    root.mainloop()
