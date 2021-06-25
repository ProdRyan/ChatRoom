import socket
import os

os.system('color a')
print('''

     ▄▄·  ▄ .▄ ▄▄▄· ▄▄▄▄▄    ▄▄▄              • ▌ ▄ ·. 
    ▐█ ▌▪██▪▐█▐█ ▀█ •██      ▀▄ █·▪     ▪     ·██ ▐███▪
    ██ ▄▄██▀▐█▄█▀▀█  ▐█.▪    ▐▀▀▄  ▄█▀▄  ▄█▀▄ ▐█ ▌▐▌▐█·
    ▐███▌██▌▐▀▐█ ▪▐▌ ▐█▌·    ▐█•█▌▐█▌.▐▌▐█▌.▐▌██ ██▌▐█▌
    ·▀▀▀ ▀▀▀ · ▀  ▀  ▀▀▀     .▀  ▀ ▀█▄▀▪ ▀█▄▀▪▀▀  █▪▀▀▀

        Dev: xNetting & Dino / Grupo: Craka Squad
                Free Edition / Cliente
    ''')
 
socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
server_port = 2222
 
print('Tu direccion IP es: ', ip)
server_host = input('Ingrese el IP del host o la de su amigo: ')
nombre = input('Ingrese su nombre: ')
 
 
socket_server.connect((server_host, server_port))
 
socket_server.send(nombre.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()
 
print(server_name,' se ha unido')
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name,":", message)
    message = input("Tu: ")
    socket_server.send(message.encode())  
