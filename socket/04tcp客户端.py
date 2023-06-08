# TCP 严格区分客户端和服务器，因此需要分别创建客户端和服务器

# 下面是客户端的程序
import socket
# from socket import *

# os用于杀死某一个进程

"""
重复执行下列语句时，由于频繁连接某一个端口号，
程序会报错：
server_addr = ("192.168.1.238",6699)
tcp_client_socket.connect(server_addr)
报错内容如下：
OSError: [WinError 10048] 通常每个套接字地址(协议/网络地址/端口)只允许使用一次。
在windows查看端口占用,在CMD 输入: netstat -ano,会看到6699已经被绑定
解决方案，先杀掉要系统已经运行的、连接的端口号

    
    
"""
import os #使用命令行

# 杀死端口，传入端口号 port = "7788",是str类型的
def killport(port):
    r = os.popen("netstat -ano | findstr "+ port)  # 打开端口占用查看器，后面需要关掉
    text = r.read()
    arr=text.split("\n")
    print("进程个数为：",len(arr)-1)  # 2-1=1
    for text0 in arr:
        arr2=text0.split(" ")
        if len(arr2)>1:
            pid=arr2[len(arr2)-1]
            os.system("taskkill /PID "+pid+" /T /F")  # 杀死端口的关键语句
            print(pid)
    r.close()  # 关闭端口占用查看器
    



def main():
    # 1.创建socket 客户端
    # socket.SOCK_STREAM 就是TCP
    # socket.SOCK_DGRAM 就是UDP
    # udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    tcp_client_socket.bind(('',8888))  # 请求本地的网络端口，第一次正常运行，第二次就会报错，因此绑定一次就可以，否则会报错
    # 2.链接服务器 里面是元组，服务器的IP和端口
    server_addr = ("192.168.1.238",6699)
    tcp_client_socket.connect(server_addr)
    
    send_data = "hello_world"
    
    # 在UDP中发送数据使用sendto,在TCP中，发送数据使用send
    # 在这里不需要再指定IP和端口了，因为，上面使用connnect链接了
    tcp_client_socket.send(send_data.encode("utf-8"))
    
    # tcp_client_socket.close()  # 关闭
    
    # 判断是否链接成功
    # if tcp_client_socket.is_connected():
        # print("链接成功！")
     
main()