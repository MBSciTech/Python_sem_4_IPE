import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost',12346)
server_socket.bind(server_address)
server_socket.listen()
print('server is listing on: ', server_address)
connections, client_addr = server_socket.accept()

while True : 
    data = connections.recv(1024).decode()
    print('From client : ',data)
    if data =='exit' : 
        break

    data = int(data) ** 3
    connections.send(str(data).encode())

connections.close()
server_socket.close()