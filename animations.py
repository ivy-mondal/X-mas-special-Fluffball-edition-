import tkinter as tk
from datetime import datetime

from PIL import Image, ImageTk


def animate_gif(window, gif_path, position=(0, 0), callback=None, duration=5):
    # Load gif frames
    gif_image = Image.open(gif_path)
    frames = []
    try:
        while True:
            frames.append(ImageTk.PhotoImage(gif_image.copy()))
            gif_image.seek(len(frames))
    except EOFError:
        pass
    # Create label for the gif
    gif_label = tk.Label(window)
    gif_label.place(x=position[0], y=position[1])

    # Animate frames
    def update_frame(frame_number=0, start_time=None):
        if start_time is None:
            start_time = datetime.now()
        if (datetime.now() - start_time).seconds >= duration:
            callback()
            return
        gif_label.config(image=frames[frame_number])
        next_frame = (frame_number + 1) % len(frames)
        window.after(100, update_frame, next_frame, start_time)

    update_frame()
    return gif_label
