import socket 

print("Gagan Deep Singh: 17BCI0140")
host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
mes = input("ClientB: Enter message or Enter 'exit':")
 
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientB.connect((host, port))

while mes != 'exit':
    tcpClientB.send(mes.encode('utf-8'))     
    data = tcpClientB.recv(BUFFER_SIZE)
    print("ClientB received data:", data)
    mes = input("ClientB: Enter message to continue or Enter 'exit':")

tcpClientB.close() 
