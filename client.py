import socket
import os

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

PORT = 6541

s.connect(('192.168.29.119',PORT))

while True:
    
    file = str(input("ENTER FILE NAME : "))
    if file == "ls":
        s.send(file.encode())
        file = s.recv(1024).decode()
        print(file)
        continue
    if file == "cd":
        s.send(file.encode())
        file = str(input("TO > "))
        try:
            s.send(file.encode())
            os.chdir(file)
            continue
        except:
            continue
            
    if file == "EXIT":
        s.send(file.encode())
        break
    if file == "power off server":
        s.send(file.encode())
        data = s.recv(64).decode()
        print(data)
        print("\n")
        break
        
    else:
        s.send(file.encode())

        data = s.recv(4096).decode()

        print("\n")
        print(data)
        print("\n")
