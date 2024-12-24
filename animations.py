import random
from datetime import datetime

import numpy as np
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
        except tk.TclError:
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


def create_lighthouse_plot(frame, callback=None, animate=True):
    # print("Function started!")
    fig = Figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='polar')

    categories = ['Comfort', 'Patience', 'Reliability', 'Support', 'Companionship']
    values = [10, 10, 10, 10, 9]

    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False)
    values_plot = np.concatenate((values, [values[0]]))
    angles_plot = np.concatenate((angles, [angles[0]]))

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    if animate:
        # print("Starting animation sequence!")
        current_values = [0] * len(values)

        def update_values(step=0.0):
            # print(f"Animation step: {step}")

            nonlocal current_values
            ax.clear()
            current_values_plot = np.concatenate((current_values, [current_values[0]]))

            still_animating = False
            for i in range(len(current_values)):
                if current_values[i] < values[i]:
                    current_values[i] = (min(values[i], int(step)))
                    still_animating = True

            plot_color = '#FF69B4'
            fill_color = '#FFB6C1'
            ax.plot(angles_plot, current_values_plot, linewidth=2,
                    color=plot_color, marker='o', markersize=8)
            ax.fill(angles_plot, current_values_plot, alpha=0.3,
                    color=fill_color)
            ax.set_thetagrids(angles * 180 / np.pi, categories)
            ax.set_ylim(0, 10)
            ax.set_title("Lighthouse of Wuv: UwU")

            if step >= 9.0:
                angle_value = float(angles_plot[-2])
                value_value = float(values_plot[-2])
                ax.annotate("1 point deducted\nbecause you miss calls 😛",
                            xy=(angle_value, value_value),
                            xytext=(angle_value, 12),
                            ha='center', va='bottom',
                            bbox=dict(boxstyle="round,pad=0.3",
                                      fc="#FFE1E9", ec="#FF69B4", lw=2),
                            arrowprops=dict(arrowstyle="->,head_length=0.7",
                                            fc="#FF69B4", ec="#FF69B4"))

            canvas.draw()

            if still_animating:
                # print(f"Scheduling next frame... Next step will be {step + 0.5}")
                frame.after(100, lambda: update_values(float(step + 0.5)))
            else:
                # print("Animation complete!")
                if callback:
                    callback()

        frame.after(0, lambda: update_values(0.0))
    # print("Setup complete!")


def create_moms_love_plot(frame, callback=None, animate=True):
    fig = Figure(figsize=(12, 6))
    ax = fig.add_subplot(111)

    categories = ['Mom\'s Approval', 'Suspicion Immunity', 'Shared Brain Cells',
                  'Ganging Up Power', 'Honorary Son Status']
    yo_values = [9.9, 9.8, 9.5, 9.7, 9.9]
    average_guy_values = [2.0, 0.5, 1.0, 0.1, 0.0]

    x = np.arange(len(categories))
    width = 0.35

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    if animate:
        current_yo_values = [0] * len(yo_values)
        current_avg_values = [0] * len(average_guy_values)

        def update_values(step=0.0):
            ax.clear()
            still_animating = False

            # Update current values
            for i in range(len(current_yo_values)):
                if current_yo_values[i] < yo_values[i]:
                    current_yo_values[i] = min(yo_values[i], float(step))
                    still_animating = True
                if current_avg_values[i] < average_guy_values[i]:
                    current_avg_values[i] = min(average_guy_values[i], float(step))
                    still_animating = True

            # Create bars
            rects1 = ax.bar(x - width / 2, current_yo_values, width,
                            label='Mr Fluffy', color='lightblue')
            rects2 = ax.bar(x + width / 2, current_avg_values, width,
                            label='Average Guy', color='lightgrey')

            # Customize the plot
            ax.set_ylabel('Mom\'s Love-o-meter')
            ax.set_title('You vs Average Guy in Mom\'s Eyes')
            ax.set_xticks(x)
            ax.set_xticklabels(categories, rotation=45, ha='right')
            ax.legend()

            # Add value labels on bars
            ax.bar_label(rects1, padding=3)
            ax.bar_label(rects2, padding=3)

            # Add annotation when animation is nearly complete
            if step >= 9.5:
                ax.annotate("Mom's new favorite child? 😱",
                            xy=(4, 9.9),
                            xytext=(3, 7),
                            ha='center', va='bottom',
                            bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="b", lw=2),
                            arrowprops=dict(arrowstyle="->"))

            fig.tight_layout()
            canvas.draw()

            if still_animating:
                frame.after(100, lambda: update_values(step + 0.5))
            else:
                if callback:
                    callback()

        frame.after(0, lambda: update_values(0.0))


def create_hug_o_meter(frame, callback=None):
    fig = Figure(figsize=(10, 6))
    ax = fig.add_subplot(111)

    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    hugs = [random.randint(15, 20) for _ in range(7)]

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    def animate_plot():
        line, = ax.plot(days, [0] * len(hugs), marker='o', linestyle='-',
                        linewidth=2, markersize=12)

        def update_heights(current_height=0):
            ax.clear()  # Clear the entire axis instead of removing fill
            still_animating = False
            current_values = []

            for target in hugs:
                # Slow down the increment rate
                new_height = min(current_height * 0.2, target)  # Added multiplier to slow down
                current_values.append(new_height)
                if new_height < target:
                    still_animating = True

            # Redraw everything
            ax.plot(days, current_values, marker='o', linestyle='-',
                    linewidth=2, markersize=12)
            ax.fill_between(days, current_values, alpha=0.2)

            ax.set_xlabel("Day of Week", fontsize=12)
            ax.set_ylabel("Number of Hugs", fontsize=12)
            ax.set_title("Weekly Hug-o-meter: Embrace the Love!", fontsize=16)
            ax.grid(True, linestyle='--', alpha=0.7)

            canvas.draw()

            if still_animating:
                # Increased delay from 30 to 50 milliseconds
                frame.after(50, update_heights, current_height + 1)
            else:
                # Add annotations when animation is complete
                for i, hug in enumerate(hugs):
                    ax.annotate(f"{hug} hugs", (days[i], hug),
                                textcoords="offset points",
                                xytext=(0, 10), ha='center')

                ax.text(0.5, 0.05,
                        "Warning: Excessive hugging may cause extreme happiness!",
                        ha='center', va='center', transform=ax.transAxes,
                        bbox=dict(facecolor='pink', alpha=0.5,
                                  edgecolor='red', boxstyle='round,pad=0.5'))

                canvas.draw()

                if callback:
                    callback()

        update_heights()

    frame.after(0, animate_plot)


def create_skills_chart(frame, callback=None):
    fig = Figure(figsize=(10, 8))
    ax = fig.add_subplot(111)

    skills = ['Python Basics', 'Debugging', 'Not Smashing Computer',
              'Making Silly Programs', 'Impressing My mr Fluffball']
    sizes = [30, 25, 20, 15, 10]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    def animate_pie():
        current_sizes = [0] * len(sizes)

        def update_pie(step=0):
            ax.clear()
            still_animating = False

            for i, target in enumerate(sizes):
                current_sizes[i] = min(step * target / 30, target)
                if current_sizes[i] < target:
                    still_animating = True

            if sum(current_sizes) > 0:
                patches, texts, autotexts = ax.pie(current_sizes,
                                                   labels=skills,
                                                   colors=colors,
                                                   autopct='%1.1f%%' if not still_animating else '',
                                                   startangle=90)

            ax.axis('equal')
            # Using stars instead of sparkles
            ax.set_title("Things I've Learned Thanks to My Code Guru\n" +
                         "* * * Now with extra magic! * * *", pad=20)

            if not still_animating:
                ax.text(1.2, -1.2,
                        "Warning: Side effects may include\nrandom bursts of coding joy!",
                        ha='center', va='center',
                        bbox=dict(facecolor='pink', alpha=0.5,
                                  edgecolor='red', boxstyle='round,pad=0.5'))

                # Add some decorative stars around the pie
                for angle in range(0, 360, 60):
                    radius = 1.3
                    x = radius * np.cos(np.radians(angle))
                    y = radius * np.sin(np.radians(angle))
                    ax.text(x, y, '*',
                            ha='center', va='center',
                            fontsize=20, color='gold')

                if callback:
                    callback()

            canvas.draw()

            if still_animating:
                frame.after(50, update_pie, step + 1)

        update_pie()

    frame.after(0, animate_pie)


def create_uwu_display(frame, callback=None):
    container = tk.Frame(frame)
    container.pack(pady=10)

    text_widget = tk.Text(container, height=3, width=30,
                          font=('Comic Sans MS', 14), bg='pink')
    text_widget.pack(pady=5)

    def show_uwu():
        uwu_phrases = ["UwU", "OwO", "^w^", ":3", "nya~"]
        text_widget.delete(1.0, tk.END)
        uwu_string = " ".join(random.choice(uwu_phrases) for _ in range(5))
        text_widget.insert(tk.END, uwu_string)

        # Clear after 10 seconds
        frame.after(10000, lambda: text_widget.delete(1.0, tk.END))

        # Execute callback after 5 seconds
        if callback:
            frame.after(20000, callback)  # Now callback runs after 5 seconds! UwU

    generate_button = tk.Button(
        container,
        text="Generate More UwU!",
        command=show_uwu,
        font=('Comic Sans MS', 12),
        bg='lightpink'
    )
    generate_button.pack(pady=5)

    show_uwu()
    return container


def create_love_efficiency_gui(frame, callback=None):
    text_area = tk.Text(frame, height=12, width=50, font=('Courier', 10))
    text_area.pack(pady=10)

    def generate_spreadsheet():
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, "----- Love Efficiency Spreadsheet -----\n")
        text_area.insert(tk.END, "| Day | Love Units | Productivity Boost |\n")
        text_area.insert(tk.END, "|-----|------------|-------------------|\n")

        love_data = []
        total_boost = 0

        for day in range(1, 8):
            love_units = random.randint(50, 100)
            productivity = love_units * 1.5
            total_boost += productivity

            love_data.append((day, love_units, productivity))

            line = f"| {day:3} | {love_units:10} | {productivity:19.2f} |\n"
            text_area.insert(tk.END, line)

        text_area.insert(tk.END, "----------------------------------------\n")
        text_area.insert(tk.END, f"Conclusion: Love makes you {(total_boost / 7):0.1f}% more awesome! 🚀\n")

        if callback:
            frame.after(20000, callback)

    generate_btn = tk.Button(
        frame,
        text="Generate Love Data! 💘",
        command=generate_spreadsheet
    )
    generate_btn.pack(pady=5)


if __name__ == "__main__":
    import tkinter as tk

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    create_uwu_display(frame)

    root.mainloop()
