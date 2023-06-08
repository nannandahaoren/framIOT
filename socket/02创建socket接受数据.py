import socket

# AF INET (又称 PF INET)是P4 网络协议的套接类型，
# AF INET6 则是 Pv6 的;
# 而AF UNIX 则是 Unix 系统本地通信。
# socket.SOCK_STREAM 意思是TCP
# socket.SOCK_DGRAM 意思是UDP

# 如果想实现循环接受，只需把接收数据的代码放在循环中

# 创建一个套接字

udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 必须绑定自己的ip 就用''
local_addr = ('',7788)

# 绑定端口,有一个固定的端口号
udp_socket.bind(local_addr)

# 使用套接字接受数据
# 需要知道对方的端口和IP，使用元组包括起来

# udp_socket.sendto(b"hello",dest_addr)
recv_data = udp_socket.recvfrom(2048)


print(recv_data)  # 结果为：(b'Welcome', ('192.168.1.238', 8000))，是一个元组，第一个是接收的数据，第二个是发送方的ip和端口
print(recv_data[0].decode("utf-8"))

udp_socket.close()

