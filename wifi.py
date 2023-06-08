# 这是一个连接wifi的函数，可以自动连接WiFi
# 缺点是必须在源码处设定wifi账号和密码
# 必须导入network包

import time
import network


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('津发科技_2.4G', 'kingfarwuxian')
        i = 1
        while not wlan.isconnected():
            # print("正在链接...{}".format(i))
            i += 1
            time.sleep(1)
    print('network config:', wlan.ifconfig())





if __name__ == "__main__":
    
    #do_connect()
    
    wlan = network.WLAN(network.STA_IF) # create station interface
    wlan.active(True)       # activate the interface
    wlan.scan()             # scan for access points
    wlan.isconnected()      # check if the station is connected to an AP
    #wlan.connect('vivo iQOO Monster', '75800000') # connect to an AP
    # wlan.config('mac')      # get the interface's MAC address
    # wlan.ifconfig()         # get the interface's IP/netmask/gw/DNS addresses

    from socket import *

    # 1. 创建udp套接字
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    # 绑定端口
    udp_socket.bind(("0.0.0.0",7788))

    # 2. 准备接收方的地址
    dest_addr = ('192.168.29.155', 8000)

    # 3. 从键盘获取数据
    send_data = "hello world"

    # 4. 发送数据到指定的电脑上
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

