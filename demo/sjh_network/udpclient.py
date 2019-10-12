# -*- encoding: utf-8 -*-
from socket import *

# 地址和端口号：元组(目标地址或组播地址,端口号)
sendAddress = ('172.22.184.144', 8888)


def client():
    print('启动客户端，等待服务器消息……')
    # 实例化socket对象：family = AF_INET是IPV4 ，type=SOCK_DGRAM是UDP协议
    udp_client = socket(AF_INET, SOCK_DGRAM)
    # 绑定目标地址和端口号
    udp_client.bind(sendAddress)
    # 阻塞方法：等待服务器消息，如果没有消息过来，一直等待
    message, address = udp_client.recvfrom(1024)
    # 打印接收到的消息：
    print('服务器发送的消息：{0}'.format(message.decode('utf-8')))
    # 关闭：后续无操作
    udp_client.close()


if __name__ == '__main__':
    client()
