import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class ImageGallery:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Gallery")
        self.root.geometry("800x600")

        # Initialize an empty list to store images
        self.images = []
        self.current_image_index = 0

        # Create a label to display images
        self.image_label = tk.Label(self.root)
        self.image_label.pack(expand="true")

        # Add buttons for navigation and loading images
        self.prev_button = tk.Button(self.root, text="Previous<-", command=self.prev_image)
        self.prev_button.pack(side="left", padx=10, pady=10)

        self.next_button = tk.Button(self.root, text="Next->", command=self.next_image)
        self.next_button.pack(side="right", padx=10, pady=10)

        self.load_button = tk.Button(self.root, text="Load Images", command=self.load_images)
        self.load_button.pack(side="bottom", pady=10)

    def load_images(self):
        # Open file dialog to select images
        files = filedialog.askopenfilenames(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])

        if files:
            self.images = list(files)  # Save the image paths
            self.current_image_index = 0  # Reset to the first image
            self.show_image()

    def show_image(self):
        if self.images:
            image_path = self.images[self.current_image_index]
            image = Image.open(image_path)
            image.thumbnail((750, 500))  # Resize to fit in the window
            photo = ImageTk.PhotoImage(image)

            self.image_label.config(image=photo)
            self.image_label.image = photo  # Keep reference to avoid garbage collection

    def next_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.show_image()

    def prev_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index - 1) % len(self.images)
            self.show_image()

if __name__ == "__main__":
    root = tk.Tk()
    gallery = ImageGallery(root)
    root.mainloop()
