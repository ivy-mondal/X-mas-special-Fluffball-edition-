import tkinter as tk

import pygame

from animations import animate_gif, animate_text, create_adorableness_graph, create_intelligence_graph, create_listening_graph
from helper_funcs import throwback, transition_screen
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

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def on_closing(self):
        self.window.destroy()

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

        memory_text = "So this song was like me back when I met(texted if yo will 😛)\n a certain 3 cats in a trenchcoat person\n To borrow the writer's word\n 'I was lost within the darkness, but then I found you'~\n look at me not being sad and  miserable and hopeless anymore UwU\n homework ;p Are yo happier than before too or nwo?"

        cutesy_func("Until I found you.mp3", self.window, self.clear_window, reason_text, 20, self.play_click_sound, memory_text, lambda frame, callback: create_adorableness_graph(frame, callback=callback, animate=True), "shake.gif", lambda: transition_screen(self.window, self.clear_window, self.slide_02))

    def slide_02(self):
        reason_text = """ Reason #2: Intellectual Superiority (a.k.a. "The Smart Cookie Factor")\n   1. Problem-Solving Prowess: - Consistently provides solutions to my wildest ideas\n - Success rate: ~99.9% (margin of error: my stubbornnes)\n   2. First Impression:   - Initial thought: "Wow, this guy's brain is on another level\n   - Impression has only strengthened over time\n   3. Comparative Analysis:   - Subject (Mr meow) vs. Control Group (rest of humanity)\n   - Result: Subject's intelligence far exceeds control group (Note: Analysis may be influenced by high affection level)\n     4. Objective* Conclusion: Mr. Fluffball's intelligence > Universe's smartest person's intelligence
         * Objectivity may be compromised due to overwhelming bias\n    Further research ongoing, but results suggest strong correlation 
         between Mr. Fluffball's intelligence and my increasing adoration.\n "Don't believe me? Check out this graph!"""

        memory_text = "This song gotta be meh when I noticed I won't stop yapping with yo,\n I remember finding excuses ahem learning roadblocks\n and ofc I need yo to solve my doubt 👉👈\n As they wrote 'All I know since yesterday, everything has changed'~\n (me in a morning months ago UwU) "

        cutesy_func("Everything has changed.mp3", self.window, self.clear_window, reason_text, 14, self.play_click_sound, memory_text, lambda frame, callback: create_intelligence_graph(frame, callback=callback, animate=True), "dunno.gif", lambda: transition_screen(self.window, self.clear_window, self.slide_03))

    def slide_03(self):
        reason_text = """ Reason #3: The Superhuman Listener (a.k.a. The 'Wait, You Actually Heard That?' Factor)\n 1. Attention Span:
           - Longer than a giraffe's neck\n
           - Can focus on my ramblings for hours without dozing off\n 2. Memory Bank:\n
           - Recalls I stored my project in which freaking directory in my computer when I'm crying about how I can't find my project\n
           - Remembers all project ideas and whatever shite I'm supposed to learn while I'm busy being a lazy arse\n
           3. Reaction Time:
           - Responds to my messages faster than a cat to a laser pointer\n
           - May have developed telepathic abilities\n  4. Scientific* Conclusion:\n
           Mr. Attentive's listening skills > World's most advanced AI + all moms combined(except my mom ofc)\n
           * Science conducted by yours truly while ugly crying from happiness\n 
           Behold, the graph of  listening prowess!"""

        memory_text = """ Remembah we once had a discussion about is it wong calling  people as thing?\n Then I asked yo if this song is  offensive\n and yo said nah it's probably just cultural difference,\n dat was kinda funny 🤣\n we be  discussing about all sorts of weird things hehe\n B...but....do yo know\n "You  are the best thing that's ever been mine"(still applicable UwU) """

        cutesy_func("mine.mp3", self.window, self.clear_window, reason_text, 15, self.play_click_sound, memory_text, lambda frame, callback: create_listening_graph(frame, callback=callback, animate=True), "pat.gif", lambda: transition_screen(self.window, self.clear_window, self.slide_04))

    def slide_04(self):
        pass


if __name__ == "__main__":
    dunno = pwettyUI()
    dunno.window.mainloop()
