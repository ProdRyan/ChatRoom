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
                  Free Edition / Host
    ''')


new_socket = socket.socket()
host_name = socket.gethostname()
server_ip = socket.gethostbyname(host_name)
 
port = 2222
 
new_socket.bind((host_name, port))
print("Conexion exitosa")
print("Tu direccion IP es: ", server_ip)
 
nombre = input('Ingrese su nombre: ')
 
new_socket.listen(1) 
 
 
conn, add = new_socket.accept()
 
print("Conexion recibida de ", add[0])
print('Conexion establecida. Conectado con: ', add[0])
 
client = (conn.recv(1024)).decode()
print(client + ' se ha conectado.')
 
conn.send(nombre.encode())
while True:
    message = input('Tu: ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client,':', message)
