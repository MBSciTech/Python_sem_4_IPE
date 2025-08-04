import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_addr = ('localhost',12345)
server_socket.bind(server_addr)
print('server is running on ',server_addr)

while True : 
    data,addr = server_socket.recvfrom(1024)
    data = data.decode()
    print(data)
    data = input('Enter data : ')
    if data == 'exit' : 
        break
    server_socket.sendto(data.encode(),addr)

server_socket.close()