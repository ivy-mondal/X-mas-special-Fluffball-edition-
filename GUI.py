import tkinter as tk

import pygame

from animations import animate_gif


class pwettyUI:
    def __init__(self):
        self.canvas = None
        pygame.mixer.init()
        self.window = tk.Tk()
        self.window.title("CRINGE  ATTAAAAACCKKKKKKKKKK😜")
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.configure(bg="#DB3559")
        self.window.state('zoomed')

        self.show_welcome_screen()

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
            None,
            20
        )
    def welcome_screen_pt_2(self):
        pass
    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def on_closing(self):
        self.window.destroy()


if __name__ == "__main__":
    dunno = pwettyUI()
    dunno.window.mainloop()
