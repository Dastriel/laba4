from tkinter import *

array = [2, 5, 6, 10, 0, 0, 0, 0, 3, 0, 45]

def insert_text():
    s = array
    text.insert(1.0, s)

 
def get_text():
    i=0
    for i in range(len(array)-1): 
        for index in range(len(array)-1): 
            if array[index]==0: 
                array[index+1], array[index]=array[index] ,array[index+1] 
    s = text.get(1.0, END)
    label['text'] = array

root = Tk()
 
text = Text(width=25, height=5)
text.pack()
 
frame = Frame()
frame.pack()
Button(frame, text="Заданный массив",
       command=insert_text).pack(side=LEFT)
Button(frame, text="Преобразовать",
       command=get_text).pack(side=LEFT)

 
label = Label()
label.pack()
 
root.mainloop()
 