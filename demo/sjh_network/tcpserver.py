# -*- encoding: utf-8 -*-
from socket import *

# 地址和端口号：元组(目标地址,端口号)
sendAddress = ('172.22.184.144', 8888)

print('服务器启动……')
# 基于TCP的流式socket通信
server = socket(AF_INET, SOCK_STREAM)
# bind
server.bind(sendAddress)
# 侦听
print('进入侦听……')
server.listen()
# 控制客户端连接数量：满了，其它客户端等待
# server.listen(10)
# 接收客户端的连接请求：阻塞，返回值socket就是与某个客户端建立连接的通道对象，此对象负责和客户端通信
# 也可以循环接收N个客户端的连接请求：此时，建议使用线程
print('进入连接等待……')
client_server_socket, address = server.accept()
print('和客户端连接成功')
print(address)
# 接收客户端的数据
message = client_server_socket.recv(1024).decode('utf-8')
print('客户端消息：{0}'.format(message))
# 关闭
client_server_socket.close()
server.close()
