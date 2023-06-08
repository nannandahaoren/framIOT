import socket

def send_file_2_client(server_customer,clientaddr):
    
    # 6.recv/接收客户端发送过来的文件名
    filename = server_customer.recv(1024).decode("utf-8")
    print("客户端要下载的文件名为：",str(filename))
    
    # 7.打开文件，获取数据
    
    file_content = None
    try:
        # 以2进制方式打开，就可以直接发送了
        f = open(str(filename),"rb")
        file_content = f.read()
    except Exception as ret:
        print("没有要下载的文件")
        
    # 8.发送文件的数据给客户端
    if file_content:
        server_customer.send(file_content)


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
    # 如果想实现为多个客户端服务，可以将下面的代码全部放在while True中
    server_customer,clientaddr  = tcp_server.accept()  
    
    # 5.调用发送文件的函数，将服务端的文件的数据发送给客户端
    send_file_2_client(server_customer,clientaddr)
    
    # 关闭套接字
    server_customer.close()
    tcp_server.close()
    

if __name__ == "__main__":
    main()