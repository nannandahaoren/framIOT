import socket
import sys


def main():
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ipport = ("192.168.1.238",8855)
    tcp_client_socket.connect(ipport)
    
    # 要下载的文件名
    filename = "kkk"
    
    # 发送文件下载请求
    tcp_client_socket.send(filename.encode("utf-8"))
    
    #接收对方发送过来的数据,接收到的数据是2进制的
    recv_data = tcp_client_socket.recv(188888)
    
    if recv_data:
        # 由于接收到的数据是2进制的，因此以2进制方式打开
        # 使用with方式打开，文件f就不需要关闭了
        # with的前提是open可以打开的情况下不报异常，否则打不开的话会抛出异常
        with open("[接受]"+ filename,"wb") as f:
            f.write(recv_data)
    
    print("下载文件完成")
    
    tcp_client_socket.close()
    
if __name__ == "__main__":
    main()