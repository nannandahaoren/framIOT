# TCP服务端的创建过程
# 1.socket创建套接字
# 2.bind绑定自己的ip和port
# 3.listen使套接字变得可以被连接
# 4.accept等待客户端的连接
# 5.recv/send接收发送数据


import socket
def main():
    # 1.socket创建套接字,用于监听连接
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    # 2.bind绑定自己的ip和port
    tcp_server.bind(("",7890))
    
    # 3.listen使套接字变得可以被连接
    tcp_server.listen(3)  # 为什么写128 ？
    
    # 4.accept等待客户端的连接
    # server_customer是tcp_server的客服
    # server_customer负责通信，与客户端通信
    # tcp_server负责监听，然后分配客服
    # accept()会阻塞
    # 返回值是一个元组，一个是套接字（服务器的客服），一个是别人（客户端）的IP和端口
    print("-------1--------")
    server_customer,clientaddr  = tcp_server.accept()  
    print("-------2--------")
    
    
    # 5.recv/send接收发送数据
    recv_data = server_customer.recv(1024)  
    print(recv_data)
    
    # 给客户端发送数据
    server_customer.send("hahhhaaa".encode("utf-8"))

if __name__ == "__main__":
    main()