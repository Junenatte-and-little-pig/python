# -*- encoding: utf-8 -*-
from socket import *

# 地址和端口号：元组(目标地址,端口号)
sendAddress = ('172.22.184.144', 8888)

print('客户端启动……')
# 基于TCP的流式socket通信
client = socket(AF_INET, SOCK_STREAM)
# 向服务器端发出连接请求
print('向服务器端发出连接请求')
client.connect(sendAddress)
print('与服务器连接成功……')
# 向服务器发送数据
message = input('请输入发送的消息：')
client.sendall(bytes(message, encoding='utf-8'))
# 关闭
client.close()