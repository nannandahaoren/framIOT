import socket

# 实现同时收发的思路：
"""
创建发送数据的函数
创建接收数据的函数
"""
# 创建一个套接字，一个套接字可以同时收，同时发（全双工--同时收发）
def send_msg(tcp_socket):
    
    # 要发送的数据
    send_data = input("请输入要发送的语句:\n")

    # 发送目标IP地址和端口
    dest_addr = ("192.168.1.238",8000)  

    # 调用sendto发送数据
    # tcp_socket.sendto(b"hello",dest_addr)
    tcp_socket.sendto(send_data.encode("utf-8"),dest_addr)

def recv_msg(tcp_socket):
    recv_data = tcp_socket.recvfrom(1024)
    print("%s:%s" %(str(recv_data[1]),recv_data[0].decode('utf-8')))
    
    
    
tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
tcp_socket.bind('',8899)

# 发送方最好也绑定一个端口
# 接收方必须绑定端口
# 一般一个客户端，既是接收方也是发送方

# 使用套接字发送数据
# 需要知道对方的端口和IP，使用元组包括起来

# 从键盘获取数据





tcp_socket.close()

