import tkinter as tk

def toggle_mode():
    current_color = settings_window["bg"]
    new_color = "#333" if current_color == "#f0f0f0" else "#f0f0f0"
    settings_window.configure(bg=new_color)
    mode_button.configure(bg="white" if new_color == "#333" else "#333", fg="black" if new_color == "#333" else "white")

# Initialize Window
settings_window = tk.Tk()
settings_window.title("Settings")
settings_window.geometry("400x300")
settings_window.configure(bg="#f0f0f0")

# UI Elements
tk.Label(settings_window, text="Settings", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=10)
mode_button = tk.Button(settings_window, text="Toggle Dark Mode", command=toggle_mode, font=("Arial", 12), bg="#333", fg="white")
mode_button.pack(pady=10)

settings_window.mainloop()
