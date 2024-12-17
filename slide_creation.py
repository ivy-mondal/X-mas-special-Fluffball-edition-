import tkinter as tk

import pygame

from animations import animate_text, animate_gif, create_intelligence_graph, create_listening_graph
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


    reason_text = """ Reason #3: The Superhuman Listener (a.k.a. The 'Wait, You Actually Heard That?' Factor)\n 1. Attention Span:
           - Longer than a giraffe's neck  - Can focus on my ramblings for hours without dozing off\n
           2. Memory Bank: - Recalls I stored my project in which freaking directory in my computer\n
            when I'm crying about how I can't find my project\n
           - Remembers all project ideas & whatever shite I'm supposed to learn while I'm busy being a lazy arse\n
           3. Reaction Time: - Responds to my messages faster than a cat to a laser pointer\n
           - May have developed telepathic abilities\n  4. Scientific* Conclusion:\n
           Mr. Attentive's listening skills > World's most advanced AI + all moms combined(except my mom ofc)\n
           * Science conducted by yours truly while ugly crying from happiness\n 
           Behold, the graph of  listening prowess!"""

    memory_text = """Remembah we once had a discussion about is it wong calling  people as thing?\n Then I asked yo if this song is  offensive\n and yo said nah it's probably just cultural difference,\n dat was kinda funny 🤣\n we be  discussing about all sorts of weird things hehe\n B...but....do yo know\n "You  are the best thing that's ever been mine"(still applicable UwU) """

    cutesy_func("mine.mp3", window, clear_window, reason_text, 14, play_click_sound, memory_text, lambda frame, callback: create_listening_graph(frame, callback=callback, animate=True), "pat.gif", None)
    window.mainloop()
