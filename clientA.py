import socket 

print("Gagan Deep Singh: 17BCI0140")
host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
mes = input("ClientA: Enter message or Enter 'exit':") 
 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

while mes != 'exit':
    tcpClientA.send(mes.encode('utf-8'))     
    data = tcpClientA.recv(BUFFER_SIZE)
    print("ClientA received data:", data)
    mes = input("ClientA: Enter message to continue or Enter 'exit':")

tcpClientA.close()
