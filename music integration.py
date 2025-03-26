import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize pygame mixer
pygame.mixer.init()

def load_music():
    """Opens a file dialog and loads the selected music file."""
    global music_file
    music_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    
    if music_file:
        label_file.config(text="Loaded: " + music_file.split("/")[-1])  # Show file name
        pygame.mixer.music.load(music_file)

def play_music():
    """Plays the loaded music file."""
    if music_file:
        pygame.mixer.music.play()

def stop_music():
    """Stops the currently playing music."""
    pygame.mixer.music.stop()

# GUI Setup
root = tk.Tk()
root.title("Music Integration")
root.geometry("400x300")

# Heading
label_title = tk.Label(root, text="Music Integration", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

# Load Button
btn_load = tk.Button(root, text="Load Music File", command=load_music, bg="blue", fg="white")
btn_load.pack(pady=5)

# Play Button
btn_play = tk.Button(root, text="▶ Play", command=play_music, bg="green", fg="white")
btn_play.pack(pady=5)

# Stop Button
btn_stop = tk.Button(root, text="⏹ Stop", command=stop_music, bg="red", fg="white")
btn_stop.pack(pady=5)

# Label to Show Loaded File
label_file = tk.Label(root, text="No file loaded", font=("Arial", 10))
label_file.pack(pady=10)

root.mainloop()
