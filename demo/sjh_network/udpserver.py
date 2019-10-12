# -*- encoding: utf-8 -*-
from socket import *

# 地址和端口号：元组(目标地址或组播地址,端口号)
sendAddress = ('172.22.184.144', 8888)


def server():
    print('启动服务器，准备发送消息……')
    # 实例化socket对象：family = AF_INET是IPV4 ，type=SOCK_DGRAM是UDP协议
    udp_server = socket(AF_INET, SOCK_DGRAM)
    # 消息：消息必须处理为bytes类型
    message = input('输入消息：')
    # 发送消息：看目标地址（某台计算机，组播一系列计算机）
    udp_server.sendto(bytes(message, encoding='utf-8'), sendAddress)
    # 关闭：释放，后续无法使用，如果是连续发送消息时，发送消息代码在循环内
    udp_server.close()


if __name__ == '__main__':
    server()
