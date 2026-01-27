import time
import pygame
import customtkinter as ck
from PIL import Image, ImageTk
from tkinter import messagebox as m
from customtkinter import CTkButton as b,CTkLabel as l

class board:

    def __init__(self,player1,player2):
        pygame.init()

        ck.set_appearance_mode("dark")  
        self.interface = ck.CTk()
        self.interface.title("Tic Tac Toe")
        self.interface.geometry("390x460")
        self.interface.iconbitmap("Images/logo.ico")

        self.player1 = player1
        self.player2 = player2

        self.current_player = self.player1 if self.player1.identity == "x" else self.player2
        self.state = {"Cur_player": self.current_player.identity,"board_value":['' for _ in range(9)]}
        self.history = ""
    
        self.bg_img    = ImageTk.PhotoImage(Image.open("Images/bg.jpg").convert("RGBA").resize((120,120), Image.LANCZOS), master=self.interface)
        self.x_img     = ImageTk.PhotoImage(Image.open("Images/xt0.jpg").convert("RGBA").resize((120,120), Image.LANCZOS), master=self.interface)
        self.o_img     = ImageTk.PhotoImage(Image.open("Images/ot0.jpg").convert("RGBA").resize((120,120), Image.LANCZOS), master=self.interface)

        self.reset_img = ImageTk.PhotoImage(Image.open("Images/reset_2.png").convert("RGBA"), master=self.interface)
        self.undo_img  = ImageTk.PhotoImage(Image.open("Images/undo_2.png").convert("RGBA"), master=self.interface)

        self.sounds = {
            "click": pygame.mixer.Sound("sounds/click.mp3"),
            "wrong": pygame.mixer.Sound("sounds/wrong click.mp3"),
            "reset":   pygame.mixer.Sound("sounds/reset.wav"),
            "draw":   pygame.mixer.Sound("sounds/win.wav")
        }

        self.build()

    def build(self):

        self.b1 = button(self.interface,board_ref= self, height=120, width=120, text='', command=lambda: self.update_data(self.b1),fg_color = 'transparent',image = self.bg_img,hover_color= "black",index = 1)
        self.b2 = button(self.interface,board_ref= self, height=120, width=120, text='', command=lambda: self.update_data(self.b2),fg_color = 'transparent',image = self.bg_img,hover_color= "black",index = 2)
        self.b3 = button(self.interface,board_ref= self, height=120, width=120, text='', command=lambda: self.update_data(self.b3),fg_color = 'transparent',image = self.bg_img,hover_color= "black",index = 3)
        self.b4 = button(self.interface,board_ref= self, height=120, width=120, text='', command=lambda: self.update_data(self.b4),fg_color = 'transparent',image = self.bg_img,hover_color= "black",index = 4)
        self.b5 = button(self.interface,board_ref= self, height=120, width=120, text='', command=lambda: self.update_data(self.b5),fg_color = 'transparent',image = self.bg_img,hover_color= "black",index = 5)
        self.b6 = button(self.interface,board_ref= self, height=120, width=120, text='', command=lambda: self.update_data(self.b6),fg_color = 'transparent',image = self.bg_img,hover_color= "black",index = 6)
        self.b7 = button(self.interface,board_ref= self, height=120, width=120, text='', command=lambda: self.update_data(self.b7),fg_color = 'transparent',image = self.bg_img,hover_color= "black",index = 7)
        self.b8 = button(self.interface,board_ref= self, height=120, width=120, text='', command=lambda: self.update_data(self.b8),fg_color = 'transparent',image = self.bg_img,hover_color= "black",index = 8)
        self.b9 = button(self.interface,board_ref= self, height=120, width=120, text='', command=lambda: self.update_data(self.b9),fg_color = 'transparent',image = self.bg_img,hover_color= "black",index = 9)
        
        self.reset_button = button(self.interface,board_ref= self,text = '',height=24,width=24,image = self.reset_img,hover_color= "black",command = self.reset,index = -1)
        self.undo_button = button(self.interface,board_ref= self,text = '',height=24,width=24,image = self.undo_img,fg_color="transparent",hover_color=  "grey",command = self.undo,index = -2)

        self.b1.grid(c=0, r=1, padx=5, pady=5)
        self.b2.grid(c=1, r=1, padx=5, pady=5)
        self.b3.grid(c=2, r=1, padx=5, pady=5)
        self.b4.grid(c=0, r=2, padx=5, pady=5)
        self.b5.grid(c=1, r=2, padx=5, pady=5)
        self.b6.grid(c=2, r=2, padx=5, pady=5)
        self.b7.grid(c=0, r=3, padx=5, pady=5)
        self.b8.grid(c=1, r=3, padx=5, pady=5)
        self.b9.grid(c=2, r=3, padx=5, pady=5) 

        self.reset_button.grid(c=0, r=0, pady=5)
        self.undo_button.grid(c=2, r=0, pady=5)

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
            self.place(button.index)
            button.update_image()
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

    def __init__(self,root ,image,board_ref,index, height=120, width=120, text='',fg_color = 'transparent',hover_color= "black",command = lambda: None):
        self.board = board_ref
        self.button = b(root, height = height, width=width, text=text, command=command,fg_color = fg_color,image = image,hover_color=hover_color)
        self.initial_image = image
        self.index = index
        self.state = "Not Clicked"

    def grid(self,c,r,pady = 0,padx = 0):
        self.button.grid(column=c, row=r, pady=pady,padx = padx)
        
    def update_image(self): 
        print(f"Button {self.index} clicked!")  
        if self.state == "Not Clicked":
            self.button.configure(image=self.board.x_img if self.board.state["Cur_player"] == "x" else self.board.o_img)
            self.button.update()
            self.update_button_data()

        else:
            pass

    def update_button_data(self):
        self.state = "Clicked"

    def reset_button(self):
        self.state = "Not Clicked"
        self.button.configure(image = self.initial_image)
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

if __name__ == "__main__":
    player_1 = player("x","ikki",True)
    player_2 = player("o",'iniyan',False)

    board_ = board(player_1,player_2)
    board_.run()