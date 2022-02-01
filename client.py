
import socket
 
from tkinter import * 

import tkinter.messagebox as box

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def dialog1():
    hote = str(entry2.get())
    port = int(entry3.get())
    socket.connect((hote, port))
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

Label2 = Label(window,text = 'IP:')
Label2.pack(padx=15,pady= 5)

entry2 = Entry(window,bd =5)
entry2.pack(padx=15, pady=5)

Label3 = Label(window,text = 'Port:')
Label3.pack(padx=15,pady= 5)

entry3 = Entry(window,bd =5)
entry3.pack(padx=15, pady=5)


btn = Button(frame, text = 'Envoyer message',command = dialog1)


btn.pack(side = RIGHT , padx =5)
frame.pack(padx=100,pady = 19)




# print("Connection on {}".format(port))
window.mainloop()


socket.close()
