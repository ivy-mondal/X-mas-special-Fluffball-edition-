import tkinter as tk
from datetime import datetime

from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


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
        try:
            if start_time is None:
                start_time = datetime.now()
            if (datetime.now() - start_time).seconds >= duration:
                if callback:
                    callback()
                return
            gif_label.config(image=frames[frame_number])
            next_frame = (frame_number + 1) % len(frames)
            window.after(100, update_frame, next_frame, start_time)
        except tk.TclError:
            return

    update_frame()
    return gif_label


def animate_text(window, label, full_text, delay):
    def type_text(index=0):
        if index < len(full_text):
            current_text = full_text[:index + 1]
            label.config(text=current_text)
            window.after(delay, type_text, index + 1)

    type_text()


def create_adorableness_graph(frame, animate=True):
    fig = Figure(figsize=(8, 4))
    ax = fig.add_subplot(111)

    characters = ['mr fluffy', 'mom', 'disco & company', 'Tartaglia', 'Aventurine']
    adorableness = [10, 10, 10, 9.5, 9.5]

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()

    if animate:
        canvas_widget.pack_forget()

        def animate_bars():
            bars = ax.bar(characters, [0] * len(adorableness), color=['red', 'pink', 'yellow', 'blue', 'green'])
            canvas_widget.pack()

            def update_heights(current_height=0):
                still_animating = False
                for i, (bar, target) in enumerate(zip(bars, adorableness)):
                    new_height = min(current_height, target)
                    bar.set_height(new_height)
                    if new_height < target:
                        still_animating = True

                ax.set_xlabel('Characters')
                ax.set_ylabel('Adorableness Level')
                ax.set_title("Ivy's Adorableness Scale")
                canvas.draw()

                if still_animating:
                    frame.after(50, update_heights, current_height + 0.5)
                else:
                    for bar in bars:
                        height = bar.get_height()
                        ax.text(bar.get_x() + bar.get_width() / 2., height,
                                f'{height}', ha='center', va='bottom')
                    canvas.draw()

            update_heights()

        frame.after(1000, animate_bars)

    else:
        bars = ax.bar(characters, adorableness,
                      color=['red', 'pink', 'yellow', 'blue', 'green'])
        canvas_widget.pack()
