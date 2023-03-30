import socket

HOST = "127.0.0.1"
PORT = 1234

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((HOST, PORT))

serveur.listen()

clients = []
pseudo = []

def affichage(message):
    for client in clients:
        client.send(message)

def handle(client):
    try:
        message = client.receive(1024)
        print(f"{pseudo[clients.index(client)]} says {message}")
        affichage(message)
    except:
        index = clients.index(client)
        clients.remove(client)
        client.close()
        pseudo1 =  pseudo[index]
        pseudo.remove(pseudo1)