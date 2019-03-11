import socket 
from threading import Thread 

class ClientThread(Thread): 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print("New server socket thread started for " + ip + ":" + str(port)) 
 
    def run(self): 
        while 1:  
            print("Server received data:", conn.recv(2048))
            MESSAGE = input("Server: Enter Response from Server or Enter 'exit' :")
            if MESSAGE == 'exit':
                break
            conn.send(MESSAGE.encode('utf-8'))
print("This is a secured Encrypted communication using ceaser cipher")
print("Allokik Pranshu: 17BCI0036")
TCP_IP = '0.0.0.0' 
TCP_PORT = 2004 
BUFFER_SIZE = 20 

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 
 
while True: 
    tcpServer.listen(4) 
    print("Server: Waiting for connections...") 
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip, port) 
    newthread.start() 
    threads.append(newthread) 

for t in threads: 
    t.join()
