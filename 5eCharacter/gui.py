import tkinter as tk
from tkinter import *

def run_main(root):
    print("running...")
    #call the character creation
    root.destroy


print("running main...")
root = tk.Tk()
root.title('background image')
# pick a .gif image file you have in the working directory
# or give full path
image1 = tk.PhotoImage(file="background.gif")
w = image1.width()
h = image1.height()
root.geometry("%dx%d+0+0" % (800, 457))
# tk.Frame has no image argument
# so use a label as a panel/frame
panel1 = tk.Label(root, image=image1, width=800, height=457)

panel1.place(x=0, y=0)

button2 = tk.Button(panel1, text='Generate a \rDungeons and Dragons Character ', font=("Helvetica", 35, "bold"), height = 2, width = 30, anchor = N, command=run_main(root))

button2.place(x=-30,y=325)
# save the panel's image from 'garbage collection'
panel1.image = image1
# start the event loop
root.mainloop()



if __name__ == "__main__":
    app = AlexaTheBarbarian()
    app.main()
