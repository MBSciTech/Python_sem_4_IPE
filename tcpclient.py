import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_addr = ('localhost',12346)
client_socket.connect(server_addr)

while True : 
    data = input("Enter msg : ")
    if data == 'exit' : 
        break
    client_socket.send(data.encode())
    
    data = client_socket.recv(1024).decode()
    print('From server : ', data)

    if data == 'exit' :
        break
client_socket.close()
