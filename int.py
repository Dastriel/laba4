from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Сортировка массива")
root.geometry("300x250")
 
message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")

def masssort():
    mass = message.get()
    M = mass.split()
    i = 0
    for i in range(len(M)):
        if M[i] == 0:
            M = M.append(i)
            i = i + 1
        else:
            i = i + 1
    messagebox.showinfo("GUI Python", M)
message_button = Button(text="Измененный массив", command=masssort)
message_button.place(relx=.5, rely=.5, anchor="c")

root.mainloop()