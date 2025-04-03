import tkinter as tk
from tkinter import messagebox

class MovieTicketBookingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Ticket Booking System")
        self.root.geometry("500x500")
        
        self.movies = {
            "Avengers: Endgame": [1] * 10,  # 10 seats available
            "Interstellar": [1] * 8,  # 8 seats available
            "Inception": [1] * 5  # 5 seats available
        }
        
        self.selected_movie = tk.StringVar()
        self.selected_movie.set("Avengers: Endgame")

        tk.Label(root, text="Select Movie:", font=("Arial", 12, "bold")).pack(pady=10)
        self.movie_dropdown = tk.OptionMenu(root, self.selected_movie, *self.movies.keys(), command=self.show_seats)
        self.movie_dropdown.pack()

        self.canvas = tk.Canvas(root, width=400, height=200, bg="white")
        self.canvas.pack(pady=20)

        self.show_seats(self.selected_movie.get())

        self.book_btn = tk.Button(root, text="Book Selected Seats", command=self.book_tickets, bg="green", fg="white")
        self.book_btn.pack(pady=10)

        self.cancel_btn = tk.Button(root, text="Cancel Selected Seats", command=self.cancel_tickets, bg="red", fg="white")
        self.cancel_btn.pack(pady=5)

    def show_seats(self, movie):
        self.canvas.delete("all")
        self.buttons = []
        
        seats = self.movies[movie]
        for i in range(len(seats)):
            x, y = 50 + (i % 5) * 60, 50 + (i // 5) * 50
            color = "green" if seats[i] == 1 else "red"
            
            btn = self.canvas.create_rectangle(x, y, x + 40, y + 40, fill=color, outline="black", tags=f"seat_{i}")
            self.buttons.append(btn)
            self.canvas.tag_bind(f"seat_{i}", "<Button-1>", lambda event, idx=i: self.toggle_seat(idx))

    def toggle_seat(self, idx):
        movie = self.selected_movie.get()
        seats = self.movies[movie]

        if seats[idx] == 1:
            self.movies[movie][idx] = 2  # Selected
            self.canvas.itemconfig(self.buttons[idx], fill="blue")
        elif seats[idx] == 2:
            self.movies[movie][idx] = 1  # Unselected
            self.canvas.itemconfig(self.buttons[idx], fill="green")

    def book_tickets(self):
        movie = self.selected_movie.get()
        seats = self.movies[movie]
        booked = 0

        for i in range(len(seats)):
            if seats[i] == 2:
                self.movies[movie][i] = 0  # Booked
                self.canvas.itemconfig(self.buttons[i], fill="red")
                booked += 1

        if booked > 0:
            messagebox.showinfo("Success", f"{booked} tickets booked for {movie}")
        else:
            messagebox.showwarning("No Selection", "Please select a seat to book.")

    def cancel_tickets(self):
        movie = self.selected_movie.get()
        seats = self.movies[movie]
        canceled = 0

        for i in range(len(seats)):
            if seats[i] == 0:  # Booked
                self.movies[movie][i] = 1  # Available
                self.canvas.itemconfig(self.buttons[i], fill="green")
                canceled += 1

        if canceled > 0:
            messagebox.showinfo("Success", f"Canceled {canceled} tickets for {movie}")
        else:
            messagebox.showwarning("No Booking", "No booked tickets to cancel.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MovieTicketBookingGUI(root)
    root.mainloop()
