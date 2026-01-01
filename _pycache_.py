import tkinter as tk
window = tk.Tk()  # Create window
window.title("My first app")
window.geometry("400x300")  # Set window size
label = tk.Label(window, text="Hello, Tkinter!")  # Create label widget
label.pack()
window.mainloop()  # Display window
