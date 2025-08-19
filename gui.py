import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys
import threading
import signal

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
        run_script("start.sh")
        toggle_button.config(text="Stop")
        status_label.config(text="Status: Running")
        is_running = True
    else:
        status_label.config(text="Status: Stopping...")
        toggle_button.config(state="disabled")
        threading.Thread(target=stop_sequence).start()

def stop_sequence():
    run_script("stop.sh")
    root.after(0, finalize_stop)

def finalize_stop():
    global is_running
    toggle_button.config(text="Start", state="normal")
    status_label.config(text="Status: Stopped")
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
root.geometry("600x480")
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

# Status label
status_label = tk.Label(root, text="Status: Stopped", bg=BACKGROUND_COLOR, fg=FOREGROUND_COLOR, font=DEFAULT_FONT)
status_label.pack(pady=(10, 5))

# Create toggle button
is_running = False
toggle_button = tk.Button(
    root, 
    text="Start", 
    command=toggle,
    font=DEFAULT_FONT,
    bg=FOREGROUND_COLOR,
    fg=BACKGROUND_COLOR,
    relief="raised",
    bd=0)
toggle_button.pack(pady=20)


# Run the application
root.mainloop()
