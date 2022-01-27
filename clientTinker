
import socket
 
from tkinter import * 

import tkinter.messagebox as box


def dialog1():
    username=entry1.get()
    socket.send(bytes(username,'utf8'))
    box.showinfo('info','Msg envoye')
    
window = Tk()
window.title('Message à envoyer')

frame = Frame(window)

Label1 = Label(window,text = 'Message:')
Label1.pack(padx=15,pady= 5)

entry1 = Entry(window,bd =5)
entry1.pack(padx=15, pady=5)

btn = Button(frame, text = 'Envoyer message',command = dialog1)


btn.pack(side = RIGHT , padx =5)
frame.pack(padx=100,pady = 19)

hote = "192.168.43.67"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))

window.mainloop()


socket.close()
