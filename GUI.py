import tkinter as tk

import pygame

from animations import animate_gif, animate_text, create_adorableness_graph
from helper_funcs import throwback
from slide_creation import cutesy_func


class pwettyUI:
    def __init__(self):
        self.canvas = None
        pygame.mixer.init()
        self.click_sound = pygame.mixer.Sound("heartbeat.mp3")
        self.window = tk.Tk()
        self.window.title("CRINGE  ATTAAAAACCKKKKKKKKKK😜")
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.configure(bg="#DB3559")
        self.window.state('zoomed')

        self.show_welcome_screen()

    def play_click_sound(self):
        pygame.mixer.music.set_volume(0.8)
        self.click_sound.play()

    def show_welcome_screen(self):
        self.clear_window()
        try:
            pygame.mixer.music.load("Lovers' Oath.mp3")
            pygame.mixer.music.set_volume(0.8)
            pygame.mixer.music.play(-1)
        except (pygame.error, FileNotFoundError):
            print("something went wong")

        self.canvas = tk.Canvas(
            self.window,
            bg="#DB3559",
            highlightthickness=0,
        )
        self.canvas.pack(expand=True, fill='both')
        self.window.update()

        loading_label = tk.Label(
            self.window,
            text="Brace yourself for the attaaaaaaaaaccccckkkkk 👻",
            font=('Segoe Script', 20),
            fg="#F5D3EC",
            bg="#DB3559"
        )
        loading_label.place(relx=0.5, rely=0.1, anchor='center')
        screen_height = self.window.winfo_height()

        animate_gif(
            self.window,
            "cherry-blossom.gif",
            (400, 200),
            self.welcome_screen_pt_2,
            20
        )

    def welcome_screen_pt_2(self):
        self.clear_window()

        welcome_text = "Welcome to - OUR Story (my version UwU)🤗 \n and ✨ da presentation ✨ is here too "
        welcome_label = tk.Label(
            self.window,
            text="",
            font=('Segoe Script', 20),
            fg="#F5D3EC",
            bg="#DB3559"
        )
        welcome_label.place(relx=0.3, rely=0.5, anchor='center')

        animate_text(
            self.window,
            welcome_label,
            welcome_text,
            100
        )
        animate_gif(
            self.window,
            "flowerss.gif",
            (1000, 200),
            lambda: throwback(self.window, self.clear_window, self.slide_01),
            20
        )

    def slide_01(self):
        reason_text = "Reason 1: The adorableness UwU\n ==============================\n ohh shi...where do I even start?!\n My mr meow is like da most adorable fluffball everrr\n You're so charmingly awkward at times, my heart be exploding from cuteness overload :p\n On my personal Adoooorableeeness Scale, you're right up there with my mom and my cats.\n That's right,yo achieved legendary status!\n Even my beloved anime husbandos, Tartaglia and Aventurine, can't compete.\n Don't believe me? Check out this graph!"

        memory_text = "So this song was like me back when I met(texted if yo will 😛)\n a certain 3 cats in a trenchcoat person\n To borrow the writer's word\n 'I was lost within the darkness, but then I found you'~\n look at me not being sad and  miserable and hopeless anymore UwU\n homework ;p Are yo happier than before or nwo?"

        cutesy_func("Until I found you.mp3", self.window, self.clear_window, reason_text, self.play_click_sound, memory_text, lambda frame: create_adorableness_graph(frame, animate=True), "shake.gif", self.slide_02)

    def slide_02(self):
        pass

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def on_closing(self):
        self.window.destroy()


if __name__ == "__main__":
    dunno = pwettyUI()
    dunno.window.mainloop()
