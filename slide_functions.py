import tkinter as tk

import pygame

from animations import animate_text


def cutesy_func_01(window):
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
    reason_1_label.place(relx=0.5, rely=0.5, anchor='center')

    animate_text(
        window,
        reason_1_label,
        reason_1,
        100
    )