import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sample Progress Data
sessions = ["Session 1", "Session 2", "Session 3"]
scores = [60, 75, 85]

def show_progress():
    fig, ax = plt.subplots()
    ax.plot(sessions, scores, marker="o", linestyle="-", color="green")
    ax.set_title("Speech Improvement Progress")
    ax.set_xlabel("Sessions")
    ax.set_ylabel("Score (%)")

    canvas = FigureCanvasTkAgg(fig, progress_window)
    canvas.get_tk_widget().pack()

# Initialize Window
progress_window = tk.Tk()
progress_window.title("Progress Tracker")
progress_window.geometry("500x400")
progress_window.configure(bg="#f0f0f0")

# UI Elements
tk.Label(progress_window, text="Progress Tracker", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=10)
tk.Button(progress_window, text="Show Progress", command=show_progress, font=("Arial", 12), bg="#FF9800", fg="white").pack(pady=10)

progress_window.mainloop()
