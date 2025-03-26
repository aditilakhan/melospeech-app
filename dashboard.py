import tkinter as tk
import subprocess

def open_module(module_name):
    subprocess.Popen(["python", module_name])  # Runs module as a separate script

dashboard = tk.Tk()
dashboard.title("MeloSpeech - Dashboard")
dashboard.geometry("700x500")
dashboard.configure(bg="#f8f9fa")

# Navigation Buttons
modules = {
    "Speech Analysis": "speech_analysis.py",
    "Music Integration": "music integration.py",
    "Progress Tracker": "progress tracking.py",
    "Settings": "settings.py"
}

for name, script in modules.items():
    btn = tk.Button(dashboard, text=name, command=lambda s=script: open_module(s), font=("Arial", 14), bg="#28a745", fg="white", width=18, height=2)
    btn.pack(pady=10)

dashboard.mainloop()
