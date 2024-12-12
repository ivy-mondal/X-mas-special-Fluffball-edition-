import tkinter as tk

import pygame

from animations import animate_text, animate_gif, create_adorableness_graph
from helper_funcs import create_gift_button


def cutesy_func(song, window, clear_window_func, reason_text, click_sound_func, memory_text, graph_func, gib_gif, callback):
    clear_window_func()
    pygame.mixer.init()
    pygame.mixer.stop()
    pygame.mixer.music.load(song)
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play()

    reason_label = tk.Label(
        window,
        text="",
        font=('Segoe Script', 20),
        fg="#F5D3EC",
        bg="#DB3559"
    )
    reason_label.place(relx=0.5, rely=0.3, anchor='center')

    text_length = len(reason_text)
    text_display_time = text_length * 100
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

        animate_text(
            window,
            memory_text_label,
            memory_text,
            300
        )

        animate_gif(
            window,
            gib_gif,
            (1000, 500),
            callback,
            60
        )

    def show_graph_and_return():
        graph_frame = tk.Frame(window)
        graph_frame.place(relx=0.5, rely=0.7, anchor='center')
        graph_func(graph_frame)
        window.after(20000, lambda: (
            clear_window_func(),
            create_gift_button(window, lambda: [click_sound_func(), slide_special()])
        ))

    window.after(text_display_time + 500, show_graph_and_return)


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


    reason_text = "Reason 1: The adorableness UwU\n ==============================\n ohh shi...where do I even start?!\n My mr meow is like da most adorable fluffball everrr\n You're so charmingly awkward at times, my heart be exploding from cuteness overload :p\n On my personal Adoooorableeeness Scale, you're right up there with my mom and my cats.\n That's right,yo achieved legendary status!\n Even my beloved anime husbandos, Tartaglia and Aventurine, can't compete.\n Don't believe me? Check out this graph!"

    memory_text = "So this song was like me back when I met(texted if yo will 😛)\n a certain 3 cats in a trenchcoat person\n To borrow the writer's word\n 'I was lost within the darkness, but then I found you'~\n look at me not being sad and  miserable and hopeless anymore UwU"

    cutesy_func("Until I found you.mp3", window, clear_window, reason_text, play_click_sound, memory_text, lambda frame: create_adorableness_graph(frame, animate=True), "shake.gif", None)
    window.mainloop()
