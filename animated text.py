import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root,bg='black')
canvas.pack()

canvas_text = canvas.create_text(100, 100, text='', anchor='nw',fill='white' , font="helvetica 20 italic")

test_string = "Hey\nI am Shubham mamgain\nI want to be a\nSoftware engineer"
#Time delay between chars, in milliseconds
delta = 90
delay = 0
for i in range(len(test_string) + 1):
    s = test_string[:i]
    update_text = lambda s=s: canvas.itemconfigure(canvas_text, text=s)
    canvas.after(delay, update_text)
    delay += delta

root.mainloop()