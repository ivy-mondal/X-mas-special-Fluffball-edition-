import tkinter as tk

import pygame

from animations import animate_text, animate_gif, create_lighthouse_plot
from helper_funcs import create_gift_button


def cutesy_func(song, window, clear_window_func, reason_text, size, click_sound_func, memory_text, graph_func, gib_gif, callback):
    clear_window_func()
    pygame.mixer.init()
    pygame.mixer.stop()
    pygame.mixer.music.load(song)
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)

    reason_text_delay = len(reason_text) * 110

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

    window.after(reason_text_delay, show_graph_and_return)


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


    reason_text = """ Reason #5: My Personal Human Lighthouse in the Storm of Life\n 1. Comfort Level: - Warmer than blanket in cold winter night\n - Cozier than hugging a sleeping cat\n 2. Patience Meter: - Higher than Mt. Everest\n - Longer than the Trans-Siberian Railway\n 3. Reliability Rating:  - More dependable than gravity\n  - Steadier than a cat's judgmental stare\n  4. Project Support:  - From "I want to make spinning globe" to "Let's move to Mars"\n - Always says "it's fine :)" (even when it's not)\n 5. Life Event Companion: \n - There for both "give name to my cat" and "whoops me almost died, teehee"\n - Brings fluffiness to all occasions\n Here comes meow chart      
     """

    memory_text = """ Zamn yo remembah I used to be confused if yo are ai or something >.<\n You would talk so less back then and neow yo are a cuddly cat UwU\n now that's called character developement ;p \n As the writer said,\n 'It took us a while\n With every breath a new day\n With Love on the line\n We had our share of mistakes\n But all your flaws and scars are mineeeeeeee\n Still falling for you'\n(the audacity of yo to be so awesome QwQ)"""

    cutesy_func("falling.mp3", window, clear_window, reason_text, 14, play_click_sound, memory_text, lambda frame, callback: create_lighthouse_plot(frame, callback=callback, animate=True), "UwU.gif", None)
    window.mainloop()
