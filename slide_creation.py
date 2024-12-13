import tkinter as tk

import pygame

from animations import animate_text, animate_gif, create_intelligence_graph
from helper_funcs import create_gift_button


def cutesy_func(song, window, clear_window_func, reason_text, size, click_sound_func, memory_text, graph_func, gib_gif, callback):
    clear_window_func()
    pygame.mixer.init()
    pygame.mixer.stop()
    pygame.mixer.music.load(song)
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play()

    reason_text_delay = len(reason_text) * 100

    reason_label = tk.Label(
        window,
        text="",
        font=('Segoe Script', size),
        fg="#F5D3EC",
        bg="#DB3559"
    )
    reason_label.place(relx=0.5, rely=0.3, anchor='center')

    animate_text(
        window,
        reason_label,
        reason_text,
        100
    )

    def slide_special():
        clear_window_func()
        memory_text_label = tk.Label(
            window,
            text="",
            font=('Segoe Script', 20),
            fg="#F5D3EC",
            bg="#DB3559"
        )
        memory_text_label.place(relx=0.5, rely=0.3, anchor='center')
        memory_text_length = len(memory_text)
        memory_text_display_time = memory_text_length * 300


        animate_text(
            window,
            memory_text_label,
            memory_text,
            300
        )

        animate_gif(
            window,
            gib_gif,
            (900, 400),
            None,
            60
        )

        window.after(memory_text_display_time + 3000, callback)

    def show_graph_and_return():
        graph_frame = tk.Frame(window)
        graph_frame.place(relx=0.5, rely=0.5, anchor='center')

        def after_graph():
            clear_window_func()
            create_gift_button(window, lambda: [click_sound_func(), slide_special()])

        graph_func(graph_frame, callback=after_graph)

    window.after(reason_text_delay + 2000, show_graph_and_return)


if __name__ == "__main__":
    window = tk.Tk()
    window.title("testing")
    window.configure(bg="#DB3559")
    window.state('zoomed')


    def clear_window():
        for widget in window.winfo_children():
            widget.destroy()


    def play_click_sound():
        pass


    reason_text = """ Reason #2: Intellectual Superiority (a.k.a. "The Smart Cookie Factor")\n   1. Problem-Solving Prowess: - Consistently provides solutions to my wildest ideas\n - Success rate: ~99.9% (margin of error: my stubbornnes)\n   2. First Impression:   - Initial thought: "Wow, this guy's brain is on another level\n   - Impression has only strengthened over time\n   3. Comparative Analysis:   - Subject (Mr meow) vs. Control Group (rest of humanity)\n   - Result: Subject's intelligence far exceeds control group (Note: Analysis may be influenced by high affection level)\n     4. Objective* Conclusion: Mr. Fluffball's intelligence > Universe's smartest person's intelligence
         * Objectivity may be compromised due to overwhelming bias\n    Further research ongoing, but results suggest strong correlation 
         between Mr. Fluffball's intelligence and my increasing adoration.\n "Don't believe me? Check out this graph!"""

    memory_text = "This song gotta be meh when I noticed I won't stop yapping with yo,\n I remember finding excuses ahem learning roadblocks\n and ofc I need yo to solve my doubt 👉👈\n As they wrote 'All I know since yesterday, everything has changed'~\n (me in a morning months ago UwU) "

    cutesy_func("Everything has changed.mp3", window, clear_window, reason_text, 14, play_click_sound, memory_text, lambda frame, callback: create_intelligence_graph(frame, callback=callback, animate=True), "dunno.gif", None)
    window.mainloop()
