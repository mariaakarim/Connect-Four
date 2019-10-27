from tkinter import *
# I used the tkinter library to create the window

# Variables that store player 1 and player 2 names
player1_name = ""
player2_name = ""
window = Tk()
window.geometry("300x300")
window.title('player menu')
text_box = Entry(textvariable=player1_name).pack(side=RIGHT)
text_box = player2_name
window.mainloop()

#returns player names for the player class

def get_p1_name():
    return player1_name

def get_p2_name():
    return player2_name






