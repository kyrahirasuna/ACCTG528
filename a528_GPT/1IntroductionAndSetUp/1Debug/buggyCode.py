import tkinter as tk
from tkinter import ttk
from time import sleep

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

def fade_out(label):
    """Function to fade out the label"""
    for i in range(10, -1, -1):
        label.config(fg='#{:02x}{:02x}{:02x}'.format(155 + i, 89 + i, 182 + i))
        label.update()
        sleep(0.05)

def fade_in(label):
    """Function to fade in the label"""
    for i in range(11):
        label.config(fg='#{:02x}{:02x}{:02x}'.format(155 + i, 89 + i, 182 + i))
        label.update()
        sleep(0.05)

def greet(language):
    """Function to update the greeting based on selected language"""
    message = greetings[language]
    fade_out(display_label)
    display_label.config(text=message)
    fade_in(display_label)

# Creating the main window
root = tk.Tk()
root.title("Multilingual Hello World")
root.geometry("400x200")
root.resizable(True, True)

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
