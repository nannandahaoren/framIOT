import socket

# AF INET (又称 PF INET)是P4 网络协议的套接类型，
# AF INET6 则是 Pv6 的;
# 而AF UNIX 则是 Unix 系统本地通信。


# socket.SOCK_STREAM 意思是TCP
# socket.SOCK_DGRAM 意思是UDP

# 创建一个套接字

tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 发送方最好也绑定一个端口
# 接收方必须绑定端口
# 一般一个客户端，既是接收方也是发送方

# 使用套接字发送数据
# 需要知道对方的端口和IP，使用元组包括起来
send_data = input("请输入要输入的语句:\n")

dest_addr = ("192.168.1.238",8000)

# tcp_socket.sendto(b"hello",dest_addr)
tcp_socket.sendto(send_data.encode("utf-8"),dest_addr)



tcp_socket.close()

