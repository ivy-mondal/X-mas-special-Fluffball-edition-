import random
import tkinter
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
        try:
            if index < len(full_text):
                current_text = full_text[:index + 1]
                label.config(text=current_text)
                window.after(delay, type_text, index + 1)
        except tkinter.TclError:
            return

    type_text()


def create_adorableness_graph(frame, callback=None, animate=True):
    fig = Figure(figsize=(8, 4))
    ax = fig.add_subplot(111)
    ax.set_ylim(0, 10)

    characters = ['mr fluffy', 'mom', 'disco & company', 'Tartaglia', 'Aventurine']
    adorableness = [10, 10, 10, 9.5, 9.5]

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()

    if animate:
        canvas_widget.pack()

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
                    frame.after(30, update_heights, current_height + 0.07)
                else:
                    for bar in bars:
                        height = bar.get_height()
                        ax.text(bar.get_x() + bar.get_width() / 2, height,
                                f'{height}', ha='center', va='bottom')
                    canvas.draw()

                    if callback:  # Add this part!
                        callback()

            update_heights()

        frame.after(0, animate_bars)
    else:
        bars = ax.bar(characters, adorableness,
                      color=['red', 'pink', 'yellow', 'blue', 'green'])
        canvas_widget.pack()


def create_intelligence_graph(frame, callback=None, animate=True):
    fig = Figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.set_ylim(-10, 1100)

    categories = ['Mr. Fluffball', 'Einstein', 'Stephen Hawking', 'Me trying to code']
    intelligence = [1000, 160, 160, -5]  # IQ scores (totally accurate, trust me)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()

    if animate:
        canvas_widget.pack()

        def animate_bars():
            bars = ax.bar(categories, [0] * len(intelligence), color=['red', 'blue', 'green', 'yellow'])
            canvas_widget.pack()

            def update_heights(current_height=0):
                still_animating = False
                for i, (bar, target) in enumerate(zip(bars, intelligence)):
                    new_height = min(current_height, target)
                    bar.set_height(new_height)
                    if new_height < target:
                        still_animating = True

                ax.set_xlabel('Characters')
                ax.set_ylabel("Intelligence Level (Fluffball Units)")
                ax.set_title("Totally Unbiased Intelligence Comparison")
                canvas.draw()

                if still_animating:
                    frame.after(30, update_heights, current_height + 10)
                else:
                    for bar in bars:
                        height = bar.get_height()
                        ax.text(bar.get_x() + bar.get_width() / 2, height,
                                f'{height}', ha='center', va='bottom')
                    canvas.draw()

                    if callback:  # Call the callback when animation is done
                        callback()

            update_heights()

        frame.after(0, animate_bars)

    else:
        bars = ax.bar(categories, intelligence,
                      color=['red', 'blue', 'green', 'yellow'])
        canvas_widget.pack()


def create_listening_graph(frame, callback=None, animate=True):
    fig = Figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.set_ylim(-0.5, 4.5)
    ax.set_xlim(-10, 110)

    categories = ['Mr. Attentive', 'My Mom', 'Average Joe', 'A Wall', 'My Ex']
    listening_levels = [100, 100, 30, 10, -5]  # Still as scientific as ever!

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()

    if animate:
        canvas_widget.pack()

        def animate_bars():
            bars = ax.barh(categories, [0] * len(listening_levels), color=['green', 'purple', 'blue', 'gray', 'red'])
            canvas_widget.pack()

            def update_heights(current_width=0):
                still_animating = False
                for i, (bar, target) in enumerate(zip(bars, listening_levels)):
                    new_width = min(current_width, target)
                    bar.set_width(new_width)
                    if new_width < target:
                        still_animating = True

                ax.set_xlabel("Listening Level (in 'Actually Cares' Units)")
                ax.set_ylabel('Characters')
                ax.set_title("Listening Level Comparison (Now Horizontal for Extra Pizzazz!)")
                canvas.draw()

                if still_animating:
                    frame.after(30, update_heights, current_width + 1)
                else:
                    for bar in bars:
                        width = float(bar.get_width())
                        ax.text(x=width, y=bar.get_y() + bar.get_height() / 2,
                                s=f"{int(width)}", ha='left', va='center')
                    canvas.draw()

                    if callback:  # Call the callback when animation is done
                        callback()

            update_heights()

        frame.after(0, animate_bars)

    else:
        bars = ax.barh(categories, listening_levels,
                      color=['green', 'purple', 'blue', 'gray', 'red'])
        canvas_widget.pack()

def create_meow_o_meter(frame, callback=None, animate=True):
    fig = Figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.set_ylim(0, 110)

    meow_types = ['Cute', 'Demanding', 'Sleepy', 'Hungry', 'Playful']
    meow_ratings = [random.randint(80, 110) for _ in range(5)]

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()

    if animate:
        canvas_widget.pack()

        def animate_bars():
            bars = ax.bar(meow_types, [0] * len(meow_ratings), color='orange')
            canvas_widget.pack()

            def update_heights(current_height=0):
                still_animating = False
                for i, (bar, target) in enumerate(zip(bars, meow_ratings)):
                    new_height = min(current_height, target)
                    bar.set_height(new_height)
                    if new_height < target:
                        still_animating = True

                ax.set_xlabel("meow types")
                ax.set_ylabel("Meow Cuteness Level")
                ax.set_title("mr meow's Meow-O-Meter")
                canvas.draw()

                if still_animating:
                    frame.after(30, update_heights, current_height + 1)
                else:
                    for bar in bars:
                        height = bar.get_height()
                        ax.text(bar.get_x() + bar.get_width() / 2., height,
                     f'{height}%', ha='center', va='bottom')
                    canvas.draw()

                    if callback:  # Call the callback when animation is done
                        callback()

            update_heights()

        frame.after(0, animate_bars)

    else:
        bars = ax.bar(meow_types, meow_ratings,
                      color='orange')
        canvas_widget.pack()
