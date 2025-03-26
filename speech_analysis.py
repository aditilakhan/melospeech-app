import tkinter as tk
import threading
import speech_recognition as sr

# Initialize Recognizer
recognizer = sr.Recognizer()
is_listening = False  # Track Microphone state

def start_listening():
    """Start recognizing speech in a separate thread to avoid UI freezing."""
    global is_listening
    if not is_listening:
        is_listening = True
        status_label.config(text="Listening... Speak Now")
        threading.Thread(target=recognize_speech, daemon=True).start()

def stop_listening():
    """Stop recognizing speech."""
    global is_listening
    is_listening = False
    status_label.config(text="Microphone Stopped")

def recognize_speech():
    """Capture and process speech input."""
    global is_listening
    with sr.Microphone() as source:
        while is_listening:
            try:
                status_label.config(text="Listening...")
                audio = recognizer.listen(source, timeout=5)  # Capture audio
                text = recognizer.recognize_google(audio)  # Convert speech to text
                text_box.insert(tk.END, text + "\n")  # Display in Textbox
                status_label.config(text="Speech Recognized!")
            except sr.UnknownValueError:
                status_label.config(text="Couldn't understand speech!")
            except sr.RequestError:
                status_label.config(text="Speech Recognition Service Error!")
            except Exception as e:
                status_label.config(text=f"Error: {e}")

# Initialize Tkinter Window
speech_window = tk.Tk()
speech_window.title("Speech Analysis")
speech_window.geometry("600x400")
speech_window.configure(bg="#f0f0f0")

# UI Elements
tk.Label(speech_window, text="Speech Analysis", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=10)
status_label = tk.Label(speech_window, text="Press 'Start' and Speak", font=("Arial", 12), bg="#f0f0f0")
status_label.pack(pady=5)

# Buttons
tk.Button(speech_window, text="Start Microphone 🎤", command=start_listening, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(speech_window, text="Stop Microphone ❌", command=stop_listening, font=("Arial", 12), bg="#FF5733", fg="white").pack(pady=5)

# Textbox for Recognized Speech
text_box = tk.Text(speech_window, height=10, width=50, font=("Arial", 12))
text_box.pack(pady=10)

speech_window.mainloop()
