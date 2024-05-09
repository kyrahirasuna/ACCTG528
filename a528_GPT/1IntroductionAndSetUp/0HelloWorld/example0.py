import tkinter as tk
from tkinter import ttk

# Dictionary mapping languages to their respective greetings
greetings = {
    "English": "Hello World",
    "Spanish": "¡Hola Mundo!",
    "French": "Bonjour le monde",
    "German": "Hallo Welt",
    "Chinese": "你好，世界",
    "Japanese": "こんにちは世界",
    "Russian": "Привет мир",
    "Arabic": "مرحبا بالعالم",
    "Portuguese": "Olá Mundo",
    "Hindi": "नमस्ते दुनिया"
}

def greet(language):
    """Function to update the greeting based on selected language"""
    message = greetings[language]
    display_label.config(text=message)

# Creating the main window
root = tk.Tk()
root.title("Multilingual Hello World")
root.geometry("400x200")
root.resizable(True, True)  # Allow resizing in both directions

# Adding a frame to hold the buttons
button_frame = ttk.Frame(root)
button_frame.pack(expand=True, fill=tk.BOTH)

# Adding buttons for each language
languages = list(greetings.keys())
for language in languages:
    ttk.Button(button_frame, text=language, command=lambda l=language: greet(l)).pack(side=tk.LEFT, padx=5, pady=5)

# Adding label to display the greeting
display_label = ttk.Label(root, text="Hello World", font=("Arial", 20))
display_label.pack(expand=True)

root.mainloop()
