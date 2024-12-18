import tkinter as tk

import pygame

from animations import animate_text, animate_gif, create_listening_graph, create_meow_o_meter
from helper_funcs import create_gift_button


def cutesy_func(song, window, clear_window_func, reason_text, size, click_sound_func, memory_text, graph_func, gib_gif, callback):
    clear_window_func()
    pygame.mixer.init()
    pygame.mixer.stop()
    pygame.mixer.music.load(song)
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)

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


    reason_text = """ Reason #4: The Human Cat (a.k.a. The 'Did You Just Meow?' Phenomenon)\n 1. Meow Responsiveness: - Faster than I can say "pweeasee"\n - May actually be part feline (DNA test pending)\n 2. Meow Quality: - Better than my cats because they don't give a shi about me unless they hunggy\n - Has been known to make real cats jealous(because I said so)\n  3. Meow Variety:\n  - Can produce different meows on demand , normal-> Russian, they sound same though :)\n - Might secretly be voice actor for cat food commercials(definitely true)\n 4. Scientific* Conclusion: \n Mr meow's meowing abilities > Actual cats + All cat videos on the internet combined\n * Science conducted by yours truly while giggling uncontrollably\n Prepare yourself for the Meow-O-Meter!"""

    memory_text = """AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n YO REMEMBAH YO MADE A MEOW GENERATING CODE FOR ME!!!!!! \n
    Also yo can speak  cat language!!! 😱\n like "Mrrrowl prrrbit nyaaa mweeeep mrrrp-mrrrp purraww kittykittyssssp\n prrrrrrup nyaaaaaow mlemlemlem mrrowp pspspspsp mew-mew-prrrbt\n mraaaaaaaw mrrrffle nyanyanya prrrup-prrrup.🐈"\n and "Mriow nyaak purrul miawën fssskt nyanya~" \n 🤣 Pweeese nevah change >_< cause yo know\n "The world may change my whole life through but nothing's gonna change my love for you"\n(yea me know that's a bold statement UwU)"""

    cutesy_func("ma_meow.mp3", window, clear_window, reason_text, 14, play_click_sound, memory_text, lambda frame, callback: create_meow_o_meter(frame, callback=callback, animate=True), "nya_nya.gif", None)
    window.mainloop()
