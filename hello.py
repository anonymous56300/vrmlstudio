import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Simple GUI")
root.geometry("400x300")

# Add a label
label = tk.Label(root, text="Welcome to My GUI!", font=("Arial", 16))
label.pack(pady=10)

# Add a text entry field
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Add a button with a callback
def on_button_click():
    user_text = entry.get()
    label.config(text=f"You entered: {user_text}")

button = tk.Button(root, text="Submit", command=on_button_click)
button.pack(pady=10)

# Run the main loop
root.mainloop()
