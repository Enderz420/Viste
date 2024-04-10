from tkinter import *

root = Tk()
root.title("Viste")
root.configure(background="")
root.minsize(200,200)
root.maxsize(1080,1080)
root.geometry("300x300+50+50")

# Create Label in our window
text = Label(root, text="Nothing will work unless you do.")
text.pack()
text2 = Label(root, text="- Maya Angelou")
text2.pack()

left_frame = Frame(root, width="200", height="400")
left_frame.grid(row=0, column=0, padx=10, pady=5)
root.mainloop()