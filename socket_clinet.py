import socket

socket_client = socket.socket()

socket_client.connect(("localhost",8888))
print("clint客户端启动")
#客户端不用Conn 直接就好 因为server可以接受多个
while True:
    #发送消息
    msg = input("输入要给server发送的消息")
    if msg == "exit":
        break
    socket_client.send(msg.encode("UTF-8"))

    #接收消息
    recv_data = socket_client.recv(1024)
    #双引号里不能有双引号
    print(f"客户端回复的消息{recv_data.decode('UTF-8')}")

socket_client.close()
print("客户端关闭")


