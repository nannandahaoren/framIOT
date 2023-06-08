import socket
def main():
    
    # 1.socket创建套接字,用于监听连接
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    # 2.bind绑定自己的ip和port
    tcp_server.bind(("",7890))
    
    # 3.listen使套接字变得可以被连接
    tcp_server.listen(128)  # 为什么写128 ？
    
    while True:
        server_customer,clientaddr  = tcp_server.accept()  # 等待客户端连接
        print("-------2--------")
        

        # 5.recv/send接收发送数据
        recv_data = server_customer.recv(1024)  
        print(recv_data)
        
        # 给客户端发送数据
        # server_customer.send("hahhhaaa".encode("utf-8"))
        server_customer.close()
        
    tcp_server.close()


if __name__ == "__main__":
    main()