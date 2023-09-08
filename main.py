from tkinter import *
import random

root = Tk()
root.title("Cashout")
root.geometry("700x500")

queues = [
    [],
    [],
    []
]

# listboxes
lists = [
    Listbox(root),
    Listbox(root),
    Listbox(root)
]

lists[0].place(anchor=CENTER, relx=0.25, rely=0.5 ,relwidth=0.25, relheight=0.7)
lists[1].place(anchor=CENTER, relx=0.5, rely=0.5, relwidth=0.25, relheight=0.7)
lists[2].place(anchor=CENTER, relx=0.75, rely=0.5, relwidth=0.25, relheight=0.7)

# buttons
def queueup():
    queues[random.randint(0, len(queues)-1)].append(random.randint(1, 20))

def dequeue(index):
    if len(queues[index]) > 0:
        del queues[index][0]

buttons = [
    Button(root, width=10, text="Dequeue", command=lambda: dequeue(0)),
    Button(root, width=10, text="Dequeue", command=lambda: dequeue(1)),
    Button(root, width=10, text="Dequeue", command=lambda: dequeue(2))
]

buttons[0].place(anchor=CENTER, relx=0.25, rely=0.9)
buttons[1].place(anchor=CENTER, relx=0.5, rely=0.9)
buttons[2].place(anchor=CENTER, relx=0.75, rely=0.9)

queuebtn = Button(root, width=10, text="Queue up!", font=("", 15), command=queueup)
queuebtn.place(anchor=CENTER, relx=0.8, rely=0.1)

def updatelist():
    for i in lists:
        i.delete(0, END)
    
    for i in range(len(queues)):
        for j in range(len(queues[i])):
            lists[i].insert(END, queues[i][j])

while True:
    updatelist()
    root.update()