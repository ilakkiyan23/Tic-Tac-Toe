import time
import pygame
import customtkinter as ck
from PIL import Image, ImageTk
from tkinter import messagebox as m
from customtkinter import CTkButton as b,CTkLabel as l,CTkEntry as t,CTkOptionMenu as me

class board:

    def __init__(self,player1,player2):
        pygame.init()

        ck.set_appearance_mode("dark")  
        self.interface = ck.CTk()
        self.interface.title("Tic Tac Toe - Game Board")
        self.interface.geometry("470x570")
        self.interface.resizable(False, False)
        self.interface.iconbitmap("Images/logo.ico")

        self.player1 = player1
        self.player2 = player2

        self.current_player = self.player1 if self.player1.identity == "x" else self.player2
        self.state = {"Cur_player": self.current_player.identity,"board_value":['' for _ in range(9)]}
        self.history = ""
    
        self.bg_img    = ImageTk.PhotoImage(Image.open("Images/bg.jpg").convert("RGBA").resize((110,110), Image.LANCZOS), master=self.interface)
        self.x_img     = ImageTk.PhotoImage(Image.open("Images/xt0.jpg").convert("RGBA").resize((110,110), Image.LANCZOS), master=self.interface)
        self.o_img     = ImageTk.PhotoImage(Image.open("Images/ot0.jpg").convert("RGBA").resize((110,110), Image.LANCZOS), master=self.interface)

        self.reset_img = ImageTk.PhotoImage(Image.open("Images/reset_2.png").convert("RGBA"), master=self.interface)
        self.undo_img  = ImageTk.PhotoImage(Image.open("Images/undo_2.png").convert("RGBA"), master=self.interface)

        self.sounds = {
            "click": pygame.mixer.Sound("sounds/click.mp3"),
            "wrong": pygame.mixer.Sound("sounds/wrong click.mp3"),
            "reset":   pygame.mixer.Sound("sounds/reset.wav"),
            "draw":   pygame.mixer.Sound("sounds/win.wav")
        }

        print(self.state["board_value"])

        self.build()

    def build(self):
        main_frame = ck.CTkFrame(self.interface, fg_color="#0a0e27")
        main_frame.pack(fill="both", expand=True, padx=0, pady=0)

        board_container = ck.CTkFrame(main_frame, fg_color="#1a1a2e", corner_radius=12)
        board_container.pack(fill="both", expand=True, padx=12, pady=12)

        # Scoreboard section with player cards (FIRST)
        scoreboard_frame = ck.CTkFrame(board_container, fg_color="transparent")
        scoreboard_frame.pack(fill="x", padx=0, pady=(0, 10))

        # Player 1 Card
        p1_score_card = ck.CTkFrame(scoreboard_frame, fg_color="#252540", corner_radius=8)
        p1_score_card.pack(side="left", expand=True, padx=6,pady = 1)

        p1_emoji = l(p1_score_card, text="👤", font=("Arial", 22))
        p1_emoji.pack(pady=0)

        p1_name_label = l(p1_score_card, text=f"{self.player1.name}", font=("Arial", 9, "bold"), text_color="#00ffff")
        p1_name_label.pack(pady=0)

        self.player1_score_label = l(p1_score_card, text="0", font=("Arial", 14, "bold"), text_color="#00ffff")
        self.player1_score_label.pack(pady=0)

        # Player 2 Card
        p2_score_card = ck.CTkFrame(scoreboard_frame, fg_color="#252540", corner_radius=8)
        p2_score_card.pack(side="right", expand=True, padx=6,pady = 5)

        p2_emoji = l(p2_score_card, text="👤", font=("Arial", 22))
        p2_emoji.pack(pady=0)

        p2_name_label = l(p2_score_card, text=f"{self.player2.name}", font=("Arial", 9, "bold"), text_color="#ff00ff")
        p2_name_label.pack(pady=0)

        self.player2_score_label = l(p2_score_card, text="0", font=("Arial", 14, "bold"), text_color="#ff00ff")
        self.player2_score_label.pack(pady=0)

        # Game board (SECOND)
        board_inner = ck.CTkFrame(board_container, fg_color="transparent")
        board_inner.pack(pady=10)

        self.b1 = button(board_inner, board_ref=self, height=110, width=110, text='', command=lambda: self.update_data(self.b1), fg_color='#000000', image=self.bg_img, hover_color="#1A1A2E", index=1, corner_radius=8)
        self.b2 = button(board_inner, board_ref=self, height=110, width=110, text='', command=lambda: self.update_data(self.b2), fg_color='#000000', image=self.bg_img, hover_color="#1A1A2E", index=2, corner_radius=8)
        self.b3 = button(board_inner, board_ref=self, height=110, width=110, text='', command=lambda: self.update_data(self.b3), fg_color='#000000', image=self.bg_img, hover_color="#1A1A2E", index=3, corner_radius=8)
        self.b4 = button(board_inner, board_ref=self, height=110, width=110, text='', command=lambda: self.update_data(self.b4), fg_color='#000000', image=self.bg_img, hover_color="#1A1A2E", index=4, corner_radius=8)
        self.b5 = button(board_inner, board_ref=self, height=110, width=110, text='', command=lambda: self.update_data(self.b5), fg_color='#000000', image=self.bg_img, hover_color="#1A1A2E", index=5, corner_radius=8)
        self.b6 = button(board_inner, board_ref=self, height=110, width=110, text='', command=lambda: self.update_data(self.b6), fg_color='#000000', image=self.bg_img, hover_color="#1A1A2E", index=6, corner_radius=8)
        self.b7 = button(board_inner, board_ref=self, height=110, width=110, text='', command=lambda: self.update_data(self.b7), fg_color='#000000', image=self.bg_img, hover_color="#1A1A2E", index=7, corner_radius=8)
        self.b8 = button(board_inner, board_ref=self, height=110, width=110, text='', command=lambda: self.update_data(self.b8), fg_color='#000000', image=self.bg_img, hover_color="#1A1A2E", index=8, corner_radius=8)
        self.b9 = button(board_inner, board_ref=self, height=110, width=110, text='', command=lambda: self.update_data(self.b9), fg_color='#000000', image=self.bg_img, hover_color="#1A1A2E", index=9, corner_radius=8)
        
        self.reset_button = button(board_inner, board_ref=self, text='RESET', height=40, width=100, image=self.reset_img, command=self.reset, index=-1, corner_radius=8, font=("Arial", 10, "bold"))
        self.undo_button = button(board_inner, board_ref=self, text='UNDO', height=40, width=100, image=self.undo_img, command=self.undo, index=-2, corner_radius=8, font=("Arial", 10, "bold"))

        self.b1.grid(c=0, r=1, padx=3, pady=3)
        self.b2.grid(c=1, r=1, padx=3, pady=3)
        self.b3.grid(c=2, r=1, padx=3, pady=3)
        self.b4.grid(c=0, r=2, padx=3, pady=3)
        self.b5.grid(c=1, r=2, padx=3, pady=3)
        self.b6.grid(c=2, r=2, padx=3, pady=3)
        self.b7.grid(c=0, r=3, padx=3, pady=3)
        self.b8.grid(c=1, r=3, padx=3, pady=3)
        self.b9.grid(c=2, r=3, padx=3, pady=3)

        self.reset_button.grid(c=0, r=5, pady=15, padx=3)
        self.undo_button.grid(c=2, r=5, pady=15, padx=3)

    def run(self):
        self.interface.after(1000, self.current_player.move) 
        self.interface.mainloop()

    def reset(self):
        self.sounds["reset"].play()
        for cell in (self.b1, self.b2, self.b3, self.b4, self.b5,self.b6, self.b7, self.b8, self.b9):
            time.sleep(0.03)
            cell.reset_button()
        
        self.history = ''
        self.state["board_value"] = ['' for _ in range(9)]
        self.current_player = self.player1 if self.player1.identity == "x" else self.player2
        self.state["Cur_player"] = self.current_player.identity

    def undo(self):
        try:
            print(self.history,self.state["board_value"])
            for cell in (self.b1, self.b2, self.b3, self.b4, self.b5,self.b6, self.b7, self.b8, self.b9):
                if cell.index == int(self.history[-1]):
                    cell.reset_button()
                    self.switch_player()
                    self.state["board_value"][int(self.history[-1])-1] = ''
                    self.history = self.history[:-1] 
                    break

        except Exception as e:
            print(e)

    def place(self,button_index):
        self.state["board_value"][button_index-1] = self.current_player.name
        self.history += str(button_index)
        print(self.current_player.player_value(self.state["board_value"]))
      
    def switch_player(self):
        self.current_player = (self.player2 if self.current_player is self.player1 else self.player1)
        self.state["Cur_player"] = self.current_player.identity
    
    def update_data(self,button): 

        if button.state == "Not Clicked":
            self.sounds["click"].play()
            button.update_image()
            self.place(button.index)
            self.status = self.checker(self.current_player.player_value(self.state["board_value"]))

            if self.status:
                    return
            else:
                self.switch_player()
                self.current_player.move()

        else:
            self.sounds["wrong"].play()

    def checker(self,value):   
            comb = ('123', '147', '159', '258', '369', '357', '456', '789')
            for combinations in comb:
                for number in combinations:
                    if number not in value:
                        break

                else:
                    m.showinfo('winner',f'The winner is {self.current_player.name}')
                    self.reset()
                    return 1
            else:
                if len(self.player1.player_value(self.state["board_value"]) + self.player2.player_value(self.state["board_value"])) == 9:
                    self.sounds["draw"].play()
                    m.showinfo('OoPs',f'Its a draw')
                    self.reset()
                    return -1
                
                else:
                    return 0

class button:

    def __init__(self, root, image, board_ref, index, height=120, width=120, text='', fg_color='transparent', hover_color="black", command=lambda: None, corner_radius=0, font=None):
        self.board = board_ref
        self.button = b(root, height=height, width=width, text=text, command=command, fg_color=fg_color, image=image, hover_color=hover_color, corner_radius=corner_radius, font=font)
        self.initial_image = image
        self.index = index
        self.state = "Not Clicked"

    def grid(self, c, r, pady=0, padx=0):
        self.button.grid(column=c, row=r, pady=pady, padx=padx)
        
    def update_image(self): 
        print(f"Button {self.index} clicked!")  
        if self.state == "Not Clicked":
            self.state = "Clicked"
            self.button.configure(image=self.board.x_img if self.board.state["Cur_player"] == "x" else self.board.o_img)
            self.button.update()

        else:
            pass

    def reset_button(self):
        self.state = "Not Clicked"
        self.button.configure(image=self.initial_image)
        self.button.update()

class player:
    def __init__(self, identity,name,exists):
        self.identity = identity
        self.name = name 
        self.bot = not(exists)
        self.value = ''

    def move(self):  

        if self.bot:
            print("bot")

        else:
            print("player")

    def player_value(self,board_value):
        temp = ''
        for index,values in enumerate(board_value):
            if values == self.name:
                temp += str(index+1)

        self.value = temp

        return self.value

    def gameon(self): 
              
            self.player_1_det = ("x",self.text_field_1.get() or "player1",(self.menu_1.get() == "Player"))
            self.player_2_det = ("o",self.text_field_2.get() or "player2",(self.menu_2.get() == "Player"))

            self.interface.destroy()

if __name__ == "__main__":
    while True:
            ck.set_appearance_mode("dark")  
            interface = ck.CTk()
            interface.title("Tic Tac Toe")
            interface.geometry("550x650")
            interface.resizable(False, False)
            interface._set_appearance_mode("dark")
            
            main_frame = ck.CTkFrame(interface, fg_color="#0a0e27")
            main_frame.pack(fill="both", expand=True, padx=0, pady=0)

            title_label = l(main_frame, text="🎮 TIC TAC TOE 🎮", font=("Arial", 36, "bold"), text_color="#00ffff")
            title_label.pack(pady=25)

            subtitle = l(main_frame, text="✨ Strategic Gaming Experience ✨", font=("Arial", 11), text_color="#888888")
            subtitle.pack(pady=5)

            sep_label = l(main_frame, text="━" * 50, text_color="#00d4ff")
            sep_label.pack(pady=15)

            players_frame = ck.CTkFrame(main_frame, fg_color="transparent")
            players_frame.pack(fill="x", padx=30, pady=10)

            p1_container = ck.CTkFrame(players_frame, fg_color="#1a1f3a", corner_radius=10)
            p1_container.pack(side="left", fill="both", expand=True, padx=10)

            p1_frame_label = l(p1_container, text="👤 PLAYER 1 (X)", font=("Arial", 13, "bold"), text_color="#00d4ff")
            p1_frame_label.pack(pady=12)
            
            text_field_1 = t(p1_container, placeholder_text="Enter your name...", width=150, font=("Arial", 11))
            text_field_1.pack(padx=15, pady=8)
        
            menu_1 = me(p1_container, values = ["🎮 Player","🤖 Bot"], button_color=("#00d4ff", "#003d5c"), button_hover_color="#0099cc", font=("Arial", 10))
            menu_1.pack(padx=15, pady=12)
        
            p2_container = ck.CTkFrame(players_frame, fg_color="#2a1a3a", corner_radius=10)
            p2_container.pack(side="right", fill="both", expand=True, padx=10)

            p2_frame_label = l(p2_container, text="👤 PLAYER 2 (O)", font=("Arial", 13, "bold"), text_color="#ff6b9d")
            p2_frame_label.pack(pady=12)
            
            text_field_2 = t(p2_container, placeholder_text="Enter your name...", width=150, font=("Arial", 11))
            text_field_2.pack(padx=15, pady=8)
        
            menu_2 = me(p2_container, values = ["🎮 Player","🤖 Bot"], button_color=("#ff6b9d", "#5c003d"), button_hover_color="#dd4477", font=("Arial", 10))
            menu_2.pack(padx=15, pady=12)

            sep_label2 = l(main_frame, text="━" * 50, text_color="#ff6b9d")
            sep_label2.pack(pady=15)

            def start_game():
                player_1 = player("x",text_field_1.get() or "Player 1",(menu_1.get() == "🎮 Player"))
                player_2 = player("o",text_field_2.get() or "Player 2",(menu_2.get() == "🎮 Player"))
                
                interface.destroy()

                board_ = board(player_1, player_2)
                board_.run()

            buttons_frame = ck.CTkFrame(main_frame, fg_color="transparent")
            buttons_frame.pack(fill="x", padx=30, pady=20)

            start_button = b(buttons_frame, text = "▶  START GAME  ▶", command = start_game, width=200, height=50, font=("Arial", 13, "bold"), fg_color="#00d4ff", text_color="#0a0e27", hover_color="#00ffff", corner_radius=8)
            start_button.pack(pady=10)

            quit_button = b(buttons_frame, text = "✕  QUIT  ✕", command = quit, width=200, height=45, font=("Arial", 12, "bold"), fg_color="#ff6b9d", text_color="#0a0e27", hover_color="#ff99b4", corner_radius=8)
            quit_button.pack(pady=5)

            interface.mainloop()

