import tkinter as tk

# Function to open Dashboard
def open_dashboard():
    print("Opening Dashboard...")  # Replace with actual logic

# Initialize main window
root = tk.Tk()
root.title("MeloSpeech")
root.geometry("600x400")
root.configure(bg="#f0f0f0")  # Light Gray Background

# Title Label
title = tk.Label(root, text="MeloSpeech", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#333")
title.pack(pady=20)

# Short Description
desc = tk.Label(root, text="An interactive way to enhance speech with music.", font=("Arial", 12), bg="#f0f0f0", fg="#555")
desc.pack(pady=5)

# Styling for Button
button_style = {
    "font": ("Arial", 14, "bold"), "bg": "#007BFF", "fg": "white",
    "width": 15, "height": 2, "bd": 2, "relief": "raised", "cursor": "hand2"
}

# Dashboard Button
dashboard_btn = tk.Button(root, text="Go to Dashboard", command=open_dashboard, **button_style)
dashboard_btn.pack(pady=20)

# Run Application
root.mainloop()
