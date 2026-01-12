import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys
import threading
import signal
import platform
from src.hotkey_combination import HOTKEY_COMBINATION
from pynput import keyboard
from src.constants import AUDIO_FILE
import os

# Define colors
BACKGROUND_COLOR = "black"  # Black
FOREGROUND_COLOR = "white"  # White

# Define font
DEFAULT_FONT = ("TkDefaultFont", 20)

# Banner Image
BANNER_IMAGE_PATH = "assets/banner.jpg"

# Logo Image
LOGO_IMAGE_PATH = "assets/logo.png"

# Function to run shell scripts
def run_script(script_name):
    try:
        subprocess.run(["bash", script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")

# Toggle function for the button
def toggle():
    global is_running
    if not is_running:
        toggle_label.config(text="Starting", fg="orange")
        toggle_label.update_idletasks()  # Force update to show "Starting"
        run_script("start.sh")
        toggle_label.config(text="Active, Click to Stop", fg="red")
        is_running = True
    else:
        toggle_label.config(text="Stopping", fg="orange")
        toggle_label.unbind("<Button-1>")  # Disable click
        threading.Thread(target=stop_sequence).start()

def stop_sequence():
    run_script("stop.sh")
    root.after(0, finalize_stop)

def finalize_stop():
    global is_running
    toggle_label.config(text="Click to Activate", fg="green")
    toggle_label.bind("<Button-1>", lambda e: toggle())  # Re-enable click
    is_running = False

def on_exit():
    print("Exiting... Running stop.sh")
    run_script("stop.sh")
    root.destroy()

def handle_sigint(signal_received, frame):
    on_exit()
    sys.exit(0)

# Setup signal handler for Ctrl+C
signal.signal(signal.SIGINT, handle_sigint)

# Initialize main window
root = tk.Tk()
root.title("Open WhisperScribe")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg=BACKGROUND_COLOR)
root.protocol("WM_DELETE_WINDOW", on_exit)  # Handle window close

icon = tk.PhotoImage(file=LOGO_IMAGE_PATH)
root.iconphoto(False, icon)

# Load banner image using PIL
try:
    # Load image
    image = Image.open(BANNER_IMAGE_PATH)

    # Get window width (match your root.geometry width)
    target_width = 600  # or use root.winfo_width() after root.update()

    # Calculate height based on aspect ratio
    aspect_ratio = image.height / image.width
    target_height = int(target_width * aspect_ratio)

    # Resize image
    image = image.resize((target_width, target_height), Image.Resampling.LANCZOS)
    banner = ImageTk.PhotoImage(image)

    # Display image
    banner_label = tk.Label(root, image=banner, bg=BACKGROUND_COLOR)
    banner_label.pack(side="top", anchor="n", pady=0)
except Exception as e:
    print(f"Could not load banner image: {e}")
    banner_label = tk.Label(root, text="Banner Image Not Found", bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR, font=DEFAULT_FONT)
    banner_label.pack(side="top", anchor="n", pady=0)

# Create the clickable label
is_running = False
toggle_label = tk.Label(
    root,
    text="Click to Activate",
    fg="green",
    bg=BACKGROUND_COLOR,
    font=DEFAULT_FONT,
    cursor="hand2"
)
toggle_label.pack(pady=20)
toggle_label.bind("<Button-1>", lambda e: toggle())

# Update key mapping to use pynput.keyboard.Key
def format_hotkey_combination(hotkey_combination):
    key_mapping = {
        keyboard.Key.alt: "⌥ Option" if platform.system() == "Darwin" else "Alt",
        keyboard.Key.shift_l: "⇧ Shift",
        keyboard.Key.ctrl: "⌃ Ctrl",
        keyboard.Key.cmd: "⌘ Command",
        keyboard.Key.space: "Space",
        keyboard.Key.enter: "Enter",
    }
    return " + ".join(key_mapping.get(key, key.name if hasattr(key, 'name') else str(key)) for key in hotkey_combination)

# Split the hotkey text into parts with different background colors
hotkey_frame = tk.Frame(root, bg=BACKGROUND_COLOR)
hotkey_frame.pack(pady=(5, 5), padx=20)  # Reduced vertical padding

# Add the sentence part with black background
sentence_label = tk.Label(hotkey_frame, text="Press ", bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR, font=("TkDefaultFont", 14))
sentence_label.pack(side="left")

# Add the hotkey part with magenta background
hotkey_label = tk.Label(hotkey_frame, text=format_hotkey_combination(HOTKEY_COMBINATION), bg="magenta", fg=FOREGROUND_COLOR, font=("TkDefaultFont", 14))
hotkey_label.pack(side="left")

# Add the rest of the sentence with black background
rest_label = tk.Label(hotkey_frame, text=", release to copy and paste.", bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR, font=("TkDefaultFont", 14))
rest_label.pack(side="left")

log_file_label = tk.Label(
    root,
    text="Log File: nohup.out",
    bg=BACKGROUND_COLOR,
    fg="lightgray",
    font=("TkDefaultFont", 12),
    cursor="hand2"
)
log_file_label.pack(side="bottom", pady=(5, 5), padx=20)
log_file_label.bind("<Button-1>", lambda e: subprocess.run(["open", "-R", "nohup.out"]))


# Add labels for file paths
output_file_label = tk.Label(
    root,
    text=f"Temp Output File: {AUDIO_FILE}",
    bg=BACKGROUND_COLOR,
    fg="lightblue",
    font=("TkDefaultFont", 12),
    cursor="hand2"
)
output_file_label.pack(side="bottom", pady=(5, 5), padx=20)
output_file_label.bind("<Button-1>", lambda e: subprocess.run(["open", "-R", os.path.abspath(AUDIO_FILE)]))


# Ensure consistent vertical padding for all labels
sentence_label.pack_configure(pady=5)
hotkey_label.pack_configure(pady=5)
rest_label.pack_configure(pady=5)
log_file_label.pack_configure(pady=5)
output_file_label.pack_configure(pady=5)

# Run the application
root.mainloop()
