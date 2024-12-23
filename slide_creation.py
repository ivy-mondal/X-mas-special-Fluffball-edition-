import tkinter as tk

import pygame

from animations import animate_text, animate_gif, create_lighthouse_plot, create_moms_love_plot
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


    reason_text = """ Reason #6: The Guy Who Became My Mom's Honorary Son (What Sorcery Is This?)\n 1. Mom's Approval Rating: - - Higher than her standards for India's prime minister\n - More positive than her reaction to my A+ report card\n 2. Suspicious Activity: - All guys are baaaadd, except mr fluffball\n 
        - If guy in 10m radius of her precious daughter:
                                                      if mr fluffy:                                
                                                                  gentle smile
                                                      else:
                                                           mama bear mode activated: death stare!
    \n 3. Shared Brain Cell Count: - You two are more in sync than our Wi-Fi connection\n  - Howwwwww do you two always arrive at same conclusion?!\n  4. Ganging Up Frequency:  - More often than I eat chocolate (I want chocolate waaaah!)\n - More consistent than my sleep schedule\n 5. Lost Son Probability: \n - Higher than the chances of me understanding quantum physics\n - She won't shut up about how you must be her long lost son or something....\n Legit got adopted by mom on  children's day lmao      
    """

    memory_text = """ Zamn yo remembah I used to be confused if yo are ai or something >.<\n You would talk so less back then and neow yo are a cuddly cat UwU\n now that's called character developement ;p \n As the writer said,\n 'It took us a while\n With every breath a new day\n With Love on the line\n We had our share of mistakes\n But all your flaws and scars are mineeeeeeee\n Still falling for you'\n(the audacity of yo to be so awesome QwQ)"""

    cutesy_func("song_6.mp3", window, clear_window, reason_text, 14, play_click_sound, memory_text, lambda frame, callback: create_moms_love_plot(frame, callback=callback, animate=True), "no_6.gif", None)
    window.mainloop()
