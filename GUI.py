import tkinter as tk

import pygame

from animations import animate_gif, animate_text, create_adorableness_graph, create_intelligence_graph, create_listening_graph, create_meow_o_meter, create_lighthouse_plot, create_moms_love_plot, create_hug_o_meter, create_skills_chart, create_uwu_display, create_love_efficiency_gui
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

        cutesy_func("song_1.mp3", self.window, self.clear_window, reason_text, 20, self.play_click_sound, memory_text, lambda frame, callback: create_adorableness_graph(frame, callback=callback, animate=True), "no_1.gif", lambda: transition_screen(self.window, self.clear_window, self.slide_02))

    def slide_02(self):
        reason_text = """ Reason #2: Intellectual Superiority (a.k.a. "The Smart Cookie Factor")\n   1. Problem-Solving Prowess: - Consistently provides solutions to my wildest ideas\n - Success rate: ~99.9% (margin of error: my stubbornnes)\n   2. First Impression:   - Initial thought: "Wow, this guy's brain is on another level\n   - Impression has only strengthened over time\n   3. Comparative Analysis:   - Subject (Mr meow) vs. Control Group (rest of humanity)\n   - Result: Subject's intelligence far exceeds control group (Note: Analysis may be influenced by high affection level)\n     4. Objective* Conclusion: Mr. Fluffball's intelligence > Universe's smartest person's intelligence
         * Objectivity may be compromised due to overwhelming bias\n    Further research ongoing, but results suggest strong correlation 
         between Mr. Fluffball's intelligence and my increasing adoration.\n "Don't believe me? Check out this graph!"""

        memory_text = "This song gotta be meh when I noticed I won't stop yapping with yo,\n I remember finding excuses ahem learning roadblocks\n and ofc I need yo to solve my doubt 👉👈\n As they wrote 'All I know since yesterday, everything has changed'~\n (me in a morning months ago UwU) "

        cutesy_func("song_2.mp3", self.window, self.clear_window, reason_text, 14, self.play_click_sound, memory_text, lambda frame, callback: create_intelligence_graph(frame, callback=callback, animate=True), "no_2.gif", lambda: transition_screen(self.window, self.clear_window, self.slide_03))

    def slide_03(self):
        reason_text = """  Reason #3: The Superhuman Listener (a.k.a. The 'Wait, You Actually Heard That?' Factor)\n 1. Attention Span:
           - Longer than a giraffe's neck  - Can focus on my ramblings for hours without dozing off\n
           2. Memory Bank: - Recalls I stored my project in which freaking directory in my computer\n
            when I'm crying about how I can't find my project\n
           - Remembers all project ideas & whatever shite I'm supposed to learn while I'm busy being a lazy arse\n
           3. Reaction Time: - Responds to my messages faster than a cat to a laser pointer\n
           - May have developed telepathic abilities\n  4. Scientific* Conclusion:\n
           Mr. Attentive's listening skills > World's most advanced AI + all moms combined(except my mom ofc)\n
           * Science conducted by yours truly while ugly crying from happiness\n 
           Behold, the graph of  listening prowess!"""

        memory_text = """ Remembah we once had a discussion about is it wong calling  people as thing?\n Then I asked yo if this song is  offensive\n and yo said nah it's probably just cultural difference,\n dat was kinda funny 🤣\n we be  discussing about all sorts of weird things hehe\n B...but....do yo know\n "You  are the best thing that's ever been mine"(still applicable UwU) """

        cutesy_func("song_3.mp3", self.window, self.clear_window, reason_text, 15, self.play_click_sound, memory_text, lambda frame, callback: create_listening_graph(frame, callback=callback, animate=True), "no_3.gif", lambda: transition_screen(self.window, self.clear_window, self.slide_04))

    def slide_04(self):
        reason_text = """ Reason #4: The Human Cat (a.k.a. The 'Did You Just Meow?' Phenomenon)\n 1. Meow Responsiveness: - Faster than I can say "pweeasee"\n - May actually be part feline (DNA test pending)\n 2. Meow Quality: - Better than my cats because they don't give a shi about me unless they hunggy\n - Has been known to make real cats jealous(because I said so)\n  3. Meow Variety:\n  - Can produce different meows on demand , normal-> Russian, they sound same though :)\n - Might secretly be voice actor for cat food commercials(definitely true)\n 4. Scientific* Conclusion: \n Mr meow's meowing abilities > Actual cats + All cat videos on the internet combined\n * Science conducted by yours truly while giggling uncontrollably\n Prepare yourself for the Meow-O-Meter!"""

        memory_text = """ AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n YO REMEMBAH YO MADE A MEOW GENERATING CODE FOR ME!!!!!! \n
        Also yo can speak  cat language!!! 😱\n like "Mrrrowl prrrbit nyaaa mweeeep mrrrp-mrrrp purraww kittykittyssssp\n prrrrrrup nyaaaaaow mlemlemlem mrrowp pspspspsp mew-mew-prrrbt\n mraaaaaaaw mrrrffle nyanyanya prrrup-prrrup.🐈"\n and "Mriow nyaak purrul miawën fssskt nyanya~" \n 🤣 Pweeese nevah change >_< cause yo know\n "The world may change my whole life through but nothing's gonna change my love for you"\n(yea me know that's a bold statement UwU)"""

        cutesy_func("song_4.mp3", self.window, self.clear_window, reason_text, 14, self.play_click_sound, memory_text, lambda frame, callback: create_meow_o_meter(frame, callback=callback, animate=True), "no_4.gif", lambda: transition_screen(self.window, self.clear_window, self.slide_05))

    def slide_05(self):
        reason_text = """ Reason #5: My Personal Human Lighthouse in the Storm of Life\n 1. Comfort Level: - Warmer than blanket in cold winter night\n - Cozier than hugging a sleeping cat\n 2. Patience Meter: - Higher than Mt. Everest\n - Longer than the Trans-Siberian Railway\n 3. Reliability Rating:  - More dependable than gravity\n  - Steadier than a cat's judgmental stare\n  4. Project Support:  - From "I want to make spinning globe" to "Let's move to Mars"\n - Always says "it's fine :)" (even when it's not)\n 5. Life Event Companion: \n - There for both "give name to my cat" and "whoops me almost died, teehee"\n - Brings fluffiness to all occasions\n Here comes meow chart      
             """

        memory_text = """ Zamn yo remembah I used to be confused if yo are ai or something >.<\n You would talk so less back then and neow yo are a cuddly cat UwU\n now that's called character developement ;p \n As the writer said,\n 'It took us a while\n With every breath a new day\n With Love on the line\n We had our share of mistakes\n But all your flaws and scars are mineeeeeeee\n Still falling for you'\n(the audacity of yo to be so awesome QwQ)"""

        cutesy_func("song_5.mp3", self.window, self.clear_window, reason_text, 14, self.play_click_sound, memory_text, lambda frame, callback: create_lighthouse_plot(frame, callback=callback, animate=True), "no_5.gif", lambda: transition_screen(self.window, self.clear_window, self.slide_06))

    def slide_06(self):
        reason_text = """ Reason #6: The Guy Who Became My Mom's Honorary Son (What Sorcery Is This?)\n 1. Mom's Approval Rating: - - Higher than her standards for India's prime minister\n - More positive than her reaction to my A+ report card\n 2. Suspicious Activity: - All guys are baaaadd, except mr fluffball\n 
        - If guy in 10m radius of her precious daughter:
                                                      if mr fluffy:                                
                                                                  gentle smile
                                                      else:
                                                           mama bear mode activated: death stare!
       \n 3. Shared Brain Cell Count: - You two are more in sync than our Wi-Fi connection\n  - Howwwwww do you two always arrive at same conclusion?!\n  4. Ganging Up Frequency:  - More often than I eat chocolate (I want chocolate waaaah!)\n - More consistent than my sleep schedule\n 5. Lost Son Probability: \n - Higher than the chances of me understanding quantum physics\n - She won't shut up about how you must be her long lost son or something....\n Legit got adopted by mom on  children's day lmao      
         """
        memory_text = """ Everytime we have disagreement.........\nafterwards there's this constant thought comes in ma mind.......\nthe way yo handle my catastrophic wrath UwU...\nme know there's no such thing as perfect partner in this world but trust meh ,\n yo with all yo imperfections is perfectly imperfect for mhe :P \n(neow try saying that 5 times quickly ehe)\n ahem so as the writer says \n "I never knew you were the someone waitin' for me (nevah QwQ)"\n  aaaaaand bonus line here UwU\n "Now I know I've met an angel in person(why yo so good QwQ) """

        cutesy_func("song_6.mp3", self.window, self.clear_window, reason_text, 14, self.play_click_sound, memory_text, lambda frame, callback: create_moms_love_plot(frame, callback=callback, animate=True), "no_6.gif", lambda: transition_screen(self.window, self.clear_window, self.slide_07))

    def slide_07(self):
        reason_text = """ Reason #7: Hugs on Demand - The Hooman Snuggle Machine 🤗\n 1. Hug Availability: 24/7, rain or shine, zombie apocalypse or alien invasion\n 2. Hug Quality: From "warm fuzzy" to "OMG I can't breathe but I love it"\n 3. Hug Speed: Faster than you can say "gib hugg noww"\n 4. Hug Variety: Bear hugs, koala hugs, octopus hugs, you name it!\n 5. Hug Duration: As long as you need, even if his arms fall asleep (such dedication!)\n [I can only imagine for now, but we gonna makeeeeeeeeee it sooooner pweeeeeseeee , rightttttttttttt?!]   """
        memory_text = """ prof goof said to me,"Aww, are not you just the sweetest little koala bear hanging onto your human tree? 🐨 "\n Also definitely not meh every hour ," Mr Fluffball!!! Gib huggies!!" :p\n UwU\n Yp know "And if you hurt me\n Well, that's okay , baby, only words bleed\n Inside these  pages, you just hold me\n And I won't ever let you go\n (urm akshually, I would still prefer if yo don't :)\n  Waaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n I'M SO SICK OF BEING SO FAR QwQ \nAnd this probably gonna go on for so long too :(\n Why can't we stay together like other people do QwQ """

        cutesy_func("song_7.mp3", self.window, self.clear_window, reason_text, 14, self.play_click_sound, memory_text, lambda frame, callback: create_hug_o_meter(frame, callback=callback), "no_7.gif", lambda: transition_screen(self.window, self.clear_window, self.slide_08))

    def slide_08(self):
        reason_text = """Reason #8: My Personal Code Wizard and Debugger Extraordinaire 🧙‍♂️💻\n  1. Encouragement Level: Over 9000! Thanks to yoo I can code some crappy cringey shi like this\n 2. Patience: Infinite (unlike my loops)! How come you never get anggy\n  3. Debugging Skills: Can spot a missing semicolon from a mile away,\n you be casually flexing 14 years of experience powah\n  4. Motivational Quotes: "Everything is fixable in programming" (except maybe my smol brain)\n 5. Expert Mode: Activated when I'm about to throw my laptop out the window\n From 'Hello World' to 'Hello, I'm a coding wizard' in no time flat!\n (I know I'm not but let's just pretend UwU)\n Remember: Behind every great coder is an even greater motivator...\n or in my case, a fluffy debugger! 🐾💕\n Without you I never would have found out the thing I enjoy doing most\n and can literally work on hours 
        without getting tired\n Can't evah thank yooo enough!"""

        memory_text = """When we first met,\n yo were like oh you should try programming it's interesting,\n and I was like nah me too stoopid for that QwQ...........................\n BBUTT yo were like your teachers can't teach,\n I was going through lots of my college bullying at that time\n and your jab at my teachers made me feeel so good I swear QwQ\n lebuuuuuuu\n Neow da song for yo, "In silent screams\n In wildest dreams \n I never dreamed of this (nevahh, but it's soo gooof though >.<)"""
        cutesy_func("song_8.mp3", self.window, self.clear_window, reason_text, 14, self.play_click_sound, memory_text, lambda frame, callback: create_skills_chart(frame, callback=callback), "no_8.gif", lambda: transition_screen(self.window, self.clear_window, self.slide_09))

    def slide_09(self):
        reason_text = """Reason #9: My Safe Space for Ultimate Goofiness 🤪🎉\n You never judge my:\n 1. Random UwU outbursts\n 2. Terrible puns\n 3. Not so funny jokes\n 4. Dramatic coding sessions\n 5. Coming up with absolutely absurd ideas\n 6. Belief that programmers do magic!\n Remember: In the grand code of life, you're my favorite function! Keep being adorkable!\n btw I absolutely love your Language Dove too,\n imma learn Russian one day for sure, promiseee!\n Definitely just waiting for the zero to hero course ;p\n "I know there is no graph here\n but I neva said there is gonna be graph everywhere , ehe"""
        memory_text = """I love how yo have just accepted me gonna be dramatic once in a while\n and just  go along with it lmao\n And don't even get anggy\n SOO LADIES AND GENTLEMEN BESTO BOYFRIENDO AND FLUFFY KOT AWARD GOES TO-----\n Mr Fluffball ofc duh <3 \n yo know how da song says ,"Can we always be this close forever and ever?(QwQ)"\n Say yoshhh UwU"""
        cutesy_func("song_9.mp3", self.window, self.clear_window, reason_text, 14, self.play_click_sound, memory_text, lambda frame, callback: create_uwu_display(frame, callback=callback), "no_9.gif", lambda: transition_screen(self.window, self.clear_window, self.slide_10))

    def slide_10(self):
        reason_text = """Final Reason: Because You Make My Heart Sing! 🎵❤️\n Soooo ahem we'll let ms. Taylor Swift speakon behalf of me\n, we present to you 'Daylight'\n lyrics = "
        My love was as cruel as the cities I lived in\n
        Everyone looked worse in the light\n
        There are so many lines that I've crossed unforgiven\n
        I'll tell you the truth, but never goodbye\n
        I don't wanna look at anything else now that I saw you\n
        I don't wanna think of anything else now that I thought of you\n
        I've been sleeping so long in a 20-year dark night\n
        And now I see daylight, I only see daylight\n 
        I've created a spreadsheet to prove this. Want to review it together?"""
        memory_text = """Translation for non-musical people (INTJ edition):\n 1. Past relationships = Inefficient urban planning\n 2. Emotional growth = Optimizing life algorithms\n 3. New love = Discovering a more efficient energy source\n 4. Daylight = Clarity in decision-making processes\n In conclusion: You've improved my life's efficiency by 273.5%!\n Yo know ""I don't wanna look at anything else now that I saw you\n I don't wanna think of anything else now that I thought of you\n I've been sleeping so long in a 20-year old dark night\n and now I see daylight, I only see daylight\n(thank yoo for existin mr fluffball huggies)"\n"""
        cutesy_func("song_10.mp3", self.window, self.clear_window, reason_text, 14, self.play_click_sound, memory_text, lambda frame, callback: create_love_efficiency_gui(frame, callback=callback), "no_10.gif", self.the_end)

    def the_end(self):
        self.clear_window()
        text = "Sooooooooo which song yo liked most? UwU\n Sowwy if the last few slides weren't dat goof :( \n Mew was running out of ideas and had low enegy and felt sweepy too 😓🥺🤗"
        label = tk.Label(
            self.window,
            text="",
            font=('Segoe Script', 20),
            fg="#F5D3EC",
            bg="#DB3559"
        )
        label.place(relx=0.3, rely=0.5, anchor='center')
        animate_text(
            self.window,
            label,
            text,
            100
        )


if __name__ == "__main__":
    dunno = pwettyUI()
    dunno.window.mainloop()
