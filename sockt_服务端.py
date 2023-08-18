#server端
#创建socket对象
import socket
socket_server = socket.socket()

#绑定server到指定ip和地址
socket_server.bind(("localhost",8888))

#监听端口
socket_server.listen(1)
#listen表示接受的连接数量

#等待客户端连接
# result:tuple = socket_server.accept()
# conn =result[0] #客户端和服务端的链接对象
# address = result[1] #客户端的地址信息
print("程序已启动")
conn, address = socket_server.accept() #等同于上面的写法
#accept是阻塞方法 没有连接就不向下执行了

print(f"连接成功,客户端的信息是:{address}")

while True:
    #接受客户端信息,使用客户端和服务端的本次连接对象，而非socket_server对象
    data = conn.recv(1024).decode("UTF-8")
    #recv的接受的参数是缓冲区大小
    #recv返回值是bytes对象，解码utf-8
    print(f"客户端发来的消息是{data}")

    #发送回复消息
    msg = input("你的消息是：") #encode编码 decode 解码
    if msg == 'exit':
        break
    conn.send(msg.encode("UTF-8"))

print("服务端下线")
conn.close()
socket_server.close()
