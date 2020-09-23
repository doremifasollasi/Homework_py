from tkinter import *
 
root = Tk()
 
input_field = Entry(width=20)
button_field = Button(text="Transform")
label_field = Label(bg='yellow', fg='black', width=20)
 
def strToSortlist(event):
    s = input_field.get()
    s = s.split()
    s.sort()
    label_field['text'] = ' '.join(s)
 
button_field.bind('<Button-1>', strToSortlist)
 
input_field.pack()
button_field.pack()
label_field.pack()

root.mainloop()