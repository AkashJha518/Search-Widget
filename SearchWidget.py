#pip install customrkinter
import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import webbrowser
import os

# Placeholder text
PLACEHOLDER = "Search..."

# Function to perform search
def search(event=None):
    query = entry_var.get().strip()
    if query and query != PLACEHOLDER:
        #webbrowser.open(f"https://www.bing.com/search?q={query}")   # Open Bing search
        webbrowser.open(f"https://www.google.com/search?q={query}")  # Open Google search
    entry_var.set("")  # Clear the input using StringVar()
    restore_placeholder()  # Restore placeholder if empty

# Show search bar when hovered or clicked
def show_search_bar(event=None):
    frame.config(bg="black")  # Slightly lighter gray to make it visible
    entry.config(bg="black", fg="gray")  # Darker background but placeholder still visible
    search_icon_label.config(bg="black")  # Sync background with entry

# Hide search bar when mouse leaves (only if empty)
def hide_search_bar(event=None):
    if not entry_var.get().strip():  # Hide only if no text is entered
        frame.config(bg="black")  # Keep slightly visible instead of full black
        entry.config(bg="black", fg="gray")  # Keep placeholder background slightly visible
        search_icon_label.config(bg="black")  # Adjust icon background
        restore_placeholder()  # Restore placeholder

# Restore placeholder if entry is empty
def restore_placeholder(event=None):
    if not entry_var.get().strip():  # If the entry is empty, restore placeholder
        entry_var.set(PLACEHOLDER)
        entry.config(fg="gray")  # Make placeholder text gray

# Detect keypress to remove placeholder when the user starts typing
def on_typing(event=None):
    if entry_var.get() == PLACEHOLDER:  # Remove placeholder only on first keypress
        entry_var.set("")  # Clear text
        entry.config(fg="white")  # Set actual text color

# Create main window
root = tk.Tk()
root.title("Transparent Search Bar")
root.geometry("900x50+300+50")  # Width x Height + X Position + Y Position
root.attributes("-topmost", True)  # Keep on top
root.overrideredirect(True)  # Hide window decorations
root.wm_attributes("-transparentcolor", "black")  # True transparency
root.lower()

# Load search icon
icon_path = "search_icon.png"  # Ensure file exists
if os.path.exists(icon_path):
    icon_image = Image.open(icon_path).resize((30, 30))
    icon = ImageTk.PhotoImage(icon_image)
else:
    icon = None  # If no image found, fallback emoji

# Use StringVar to manage input text
entry_var = tk.StringVar()
entry_var.set(PLACEHOLDER)  # Set initial placeholder

# Transparent frame with NO border
frame = tk.Frame(root, bg="black", highlightthickness=0, bd=0)  # Slightly visible background
frame.pack(fill="both", expand=True, padx=0, pady=0)

# Search icon inside the frame
search_icon_label = tk.Label(frame, image=icon, bg="black") if icon else tk.Label(frame, font=("Arial", 20),text="🔍", bg="black", fg="white")
search_icon_label.pack(side="left", padx=5)

# Search entry (Initially transparent with placeholder)
entry = tk.Entry(frame, font=("Arial", 20), width=30, textvariable=entry_var, 
                 bg="black", fg="gray", insertbackground="white", borderwidth=0)
entry.pack(side="left", fill="both", expand=True, padx=5)
entry.bind("<Return>", search)  # Press Enter to search
entry.bind("<FocusIn>", show_search_bar)  # Keep placeholder on focus
entry.bind("<FocusOut>", restore_placeholder)  # Restore placeholder when lost
entry.bind("<Key>", on_typing)  # Detect keypress to remove placeholder

# Bind events
frame.bind("<Enter>", show_search_bar)  # Show on hover
entry.bind("<Enter>", show_search_bar)  # Show when input is hovered
entry.bind("<FocusOut>", hide_search_bar)  # Hide when focus is lost (if empty)
frame.bind("<Leave>", hide_search_bar)  # Hide when leaving (if empty)

root.mainloop()
