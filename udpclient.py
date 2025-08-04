import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_addr = ('localhost',12345)

while True : 
    data = input('Enter data : ')
    if data == 'exit' : 
        break
    server_socket.sendto(data.encode(),server_addr)
    data,addr = server_socket.recvfrom(1024)
    data = data.decode()
    print(data)
    

server_socket.close()