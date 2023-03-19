import socket
import os

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

PORT = 6541

s.bind(('192.168.29.19',PORT))

cut = 0

while True:
    if cut == 0:
        s.listen(10)
        conn,addr = s.accept()
    else:
        break
    
    while True:
        file = conn.recv(64).decode()
        print(file)
        if file == "power off server":
            conn.send("turning off\n".encode())
            cut = 1
            break
        
        elif file == "ls":
            os.system("ls -a > serv_cache")
            fp = open("serv_cache","r")
            conn.send(fp.read().encode())
            os.system("rm serv_cache")
            continue
            
        
        elif file == "cd":
            file = conn.recv(128).decode()
            try:
                os.chdir(file)
                continue
            except:
                continue
            
        elif file == "EXIT":
            os.chdir("/Users/<your username>")
            break
        
        flag = 1
        try:
            flag = 1
            f = open(file,"r")
        except:
            flag = 0
        
        if flag == 1:
            conn.send(f.read().encode())
        
        else:
            conn.send("wrong command or file is not readable\n".encode())


