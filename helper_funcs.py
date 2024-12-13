import tkinter as tk

import pygame
from PIL import ImageTk, Image

from animations import animate_text, animate_gif


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


def throwback(window, clear_window_func, callback):
    clear_window_func()
    pygame.mixer.music.load("ocean.mp3")
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play()
    throwback_text = "Time for a little blast from da past UwU"
    throwback_text_label = tk.Label(
        window,
        text="",
        font=('Segoe Script', 40),
        fg="#F5D3EC",
        bg="#DB3559"
    )
    throwback_text_label.place(relx=0.5, rely=0.1, anchor='center')
    window.after(10000, callback)
    animate_text(
        window,
        throwback_text_label,
        throwback_text,
        50
    )
    animate_gif(
        window,
        "throwback.gif",
        (500, 200),
        None,
        30
    )


def transition_screen(window, clear_window_func, callback):
    clear_window_func()
    pygame.mixer.music.load("heartbeat.mp3")
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play()
    transition_text = "Next slide incooooooooming 😸"
    transition_text_label = tk.Label(
        window,
        text="",
        font=('Segoe Script', 40),
        fg="#F5D3EC",
        bg="#DB3559"
    )
    transition_text_label.place(relx=0.5, rely=0.1, anchor='center')
    window.after(20000, callback)
    animate_text(
        window,
        transition_text_label,
        transition_text,
        50
    )
    animate_gif(
        window,
        "transition.gif",
        (500, 200),
        None,
        30
    )


