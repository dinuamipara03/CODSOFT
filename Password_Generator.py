import tkinter as tk
from tkinter import ttk
import random
import string


def generate_password():
    try:
        # Get the desired length of the password from the user input
        length = int(length_entry.get())

        # Check if the length is valid
        if length <= 0:
            result_label.config(text="Please enter a valid length greater than 0.")
            return

        # Define the character set for generating passwords
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate the password using random characters
        password = "".join(random.choice(characters) for i in range(length))

        # Create a pop-up window for displaying the generated password
        password_window = tk.Toplevel(root)
        password_window.title("Generated Password")

        # Customize the appearance of the pop-up window
        password_window.geometry("300x100")
        password_window.configure(bg="#f0f0f0")

        window_width = 300
        window_height = 100
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coordinate = int((screen_width - window_width) / 2)
        y_coordinate = int((screen_height - window_height) / 2)
        password_window.geometry(
            f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}"
        )

        # Create and place widgets in the pop-up window
        password_label = ttk.Label(
            password_window,
            text="Generated Password:",
            background="#f0f0f0",
            font=("Helvetica", 12),
        )
        password_label.pack(pady=5)
        password_entry = ttk.Entry(password_window, width=30, font=("Helvetica", 12))
        password_entry.insert(0, password)
        password_entry.pack(pady=5)

    except ValueError:
        result_label.config(
            text="Invalid input. Please enter a valid integer for the length."
        )


# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Customize the appearance of the main window
root.geometry("300x150")
root.configure(bg="#f0f0f0")

window_width = 300
window_height = 100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width - window_width) / 2)
y_coordinate = int((screen_height - window_height) / 3.5)
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Create and place widgets in the main window
length_label = ttk.Label(
    root,
    text="Enter the desired length of the password:",
    background="#f0f0f0",
    font=("Helvetica", 12),
)
length_label.pack(pady=5)

length_entry = ttk.Entry(root, font=("Helvetica", 12))
length_entry.pack(pady=5)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

result_label = ttk.Label(root, text="", background="#f0f0f0", font=("Helvetica", 12))
result_label.pack(pady=5)


# Run the GUI
root.mainloop()
