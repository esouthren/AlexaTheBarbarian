import tkinter as tk
from tkinter import *
import time
from user_character import CharacterGen
from populate_pdf import *
from tkinter import simpledialog



class AlexaTheBarbarian:



    def __init__(self):
        print("running main...")
        self.root = tk.Tk()
        self.root.title('background image')
        # pick a .gif image file you have in the working directory
        # or give full path
        image1 = tk.PhotoImage(file="background.gif")
        w = image1.width()
        h = image1.height()
        self.root.geometry("%dx%d+0+0" % (800, 457))
        # tk.Frame has no image argument
        # so use a label as a panel/frame
        panel1 = tk.Label(self.root, image=image1, width=800, height=457)
        panel1.place(x=0, y=0)
        button2 = tk.Button(panel1, text='You walk into a tavern...\nRoll for Initiative! ', font=("Courier", 35, "bold"), height = 2, width = 30, anchor = N, command=lambda: self.run_main() )
        button2.place(x=-30,y=325)
        # save the panel's image from 'garbage collection'
        panel1.image = image1
        # start the event loop
        self.root.mainloop()

    def run_main(self):
        print("generating character...")
        username = simpledialog.askstring("Input", "What's your Earth-person name?",parent=self.root)
        rando_char = CharacterGen().generate_character(username)
        print("Creating PDF file...")
        generate_pdf(rando_char)
        time.sleep(10)
        self.root.destroy()


if __name__ == "__main__":
    app = AlexaTheBarbarian()
