import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog
from serveur import handle

HOST = '127.0.0.1'
PORT = 1234

import socket
import threading

#création de serveur avec une adresse IP "neutre" et un port non utilisé
HOST = "127.0.0.1"
PORT = 1234

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


clients = []
pseudo = []


class Client:
    def __init__(self, HOST, PORT):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))

        msg = tkinter.Tk()
        msg.withdraw()

        self.pseudo = simpledialog.askstring ("Pseudo", "Choississez un pseudo s'il vous plait", parent=msg)
        self.gui_done = False 
        self.running = True

        interface_graphique = threading.Thread(target=self.interface)
        receive_thread = threading.Thread(target=self.receive)

        interface_graphique.start()
        receive_thread.start()


#une fonction qui va permettre de créer une interface graphique avec tkinter, qui va nous diriger vers le choix de notre pseudo ainsi 
#que l'accès au tchat une fois que nous avons envoyé notre pseudo
    def interface(self):
        self.master = tkinter.Tk()
        self.master.configure(bg="white")

        self.chat_label = tkinter.Label(self.master, text="Envoyer un message:", bg="white")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.master)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(font=("Arial", 12))

        self.msg_label = tkinter.Label(self.master, text="Message", bg="white")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tkinter.Text(self.master, height=3)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = tkinter.Button(self.master, text="Send", command = self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True
        self.master.protocol("WM_DELETE_WINDOW", self.stop)
        self.master.mainloop()

    def write(self):
        message = f"{self.pseudo}: {self.input_area.get('1.0', 'END')}"
        self.sock.send(message.encode('utf-8'))
        self.input_area.delete('1,0', 'END')

    def stop(self):
        self.running = False
        self.master.destroy()
        self.sock.close()
        exit(0)

    def receive(self):
        while self.running:
            try: 
                message = self.sock.recv(1234)
                if message == 'PSEUDO':
                    self.sock.send(self.pseudo.encode('utf-8'))
                else:
                    if self.gui_done: 
                        self.text_area.config(text='normal')
                        self.text_area.insert('END', message)
                        self.text_area.yview('END')
                        self.text_area.config(state='disabled')
            except ConnectionAbortedError:
                break
            except: 
                print("Error")
                self.sock.close()
                break