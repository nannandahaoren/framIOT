import sys #获取输入参数
import os #使用命令行
# 在windows查看端口占用,在CMD 输入: netstat -ano

port= "7890"   
r = os.popen("netstat -ano | findstr "+ port)  # 打开端口占用查看器，后面需要关掉
print(r)    # 结果为：<os._wrap_close object at 0x0000027EEFDF5C10>
text = r.read()
print(text)    # 结果为：TCP    127.0.0.1:10000        0.0.0.0:0              LISTENING       15580
arr=text.split("\n")
print(arr)    # 结果为一个列表长度为2：['  TCP    127.0.0.1:10000        0.0.0.0:0              LISTENING       15580', '']
print("进程个数为：",len(arr)-1)  # 2-1=1
for text0 in arr:
    print("===================")
    arr2=text0.split(" ")
    print(arr2)  
    
    # 结果为：
    """
    ['', '', 'TCP', '', '', '', '127.0.0.1:10000', '', '', '', '', '', '', '', 
    '0.0.0.0:0', '', '', '', '', '', '', '', '', '', '', '', '', '', 'LISTENING', '', '', '', '', '', '', '15580']
    
    """
    
    print(len(arr2))   # 结果是28
    if len(arr2)>1:
        pid=arr2[len(arr2)-1]
        os.system("taskkill /PID "+pid+" /T /F")  # 杀死端口的关键语句
        print(pid)
r.close()  # 关闭端口占用查看器
