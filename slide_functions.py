import tkinter as tk

import pygame
from PIL import ImageTk, Image

from animations import animate_text, create_adorableness_graph


def create_gift_button(window, callback):
    button_frame = tk.Frame(window, bg="#DB3559")
    button_frame.pack(expand=True)
    pil_image = Image.open("giftbox.png")
    resized_image = pil_image.resize((200, 200), Image.LANCZOS)
    gift_button_photo = ImageTk.PhotoImage(resized_image)
    gift_button = tk.Button(
        button_frame,
        image=gift_button_photo,
        borderwidth=0,
        bg='#DB3559',
        activebackground='#DB3559',
        command=callback
    )
    gift_button.image = gift_button_photo

    gift_button_label = tk.Label(
        button_frame,
        text="tap da box to know some ✨special moments in mah mind UwU✨",
        font=('Segoe Script', 16),
        bg='#DB3559',
        fg='#FF9494'
    )
    gift_button_label.pack(pady=5)
    gift_button.pack()

    return button_frame, gift_button, gift_button_label


def cutesy_func_01(window, callback, clear_window_func, click_sound_func):
    pygame.mixer.init()
    pygame.mixer.stop()
    pygame.mixer.music.load("Until I found you.mp3")
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play()

    reason_1 = "Reason 1: The adorableness UwU\n ==============================\n ohh shi...where do I even start?!\n My mr meow is like da most adorable fluffball everrr\n You're so charmingly awkward at times, my heart be exploding from cuteness overload :p\n On my personal Adoooorableeeness Scale, you're right up there with my mom and my cats.\n That's right,yo achieved legendary status!\n Even my beloved anime husbandos, Tartaglia and Aventurine, can't compete.\n Don't believe me? Check out this graph!"
    reason_1_label = tk.Label(
        window,
        text="",
        font=('Segoe Script', 20),
        fg="#F5D3EC",
        bg="#DB3559"
    )
    reason_1_label.place(relx=0.5, rely=0.3, anchor='center')

    def slide_1_special():
        pass

    def show_graph_and_return():
        graph_frame = tk.Frame(window)
        graph_frame.place(relx=0.5, rely=0.7, anchor='center')
        create_adorableness_graph(graph_frame)
        window.after(20000, lambda: (
            clear_window_func(),
            create_gift_button(window, lambda: [click_sound_func(), slide_1_special()])
        ))

    text_length = len(reason_1)
    text_display_time = text_length * 100
    animate_text(
        window,
        reason_1_label,
        reason_1,
        100
    )
    window.after(text_display_time + 500, show_graph_and_return)
