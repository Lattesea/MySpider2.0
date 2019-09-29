from socket import *
from threading import Thread
import time

from msg_handler import *
from msg import *


# 创建自定义类
class MyThread(Thread):
	def __init__(self, target, name="tedu", args = (), kwargs = {}):
		super().__init__()
		self.name = name
		self.target = target 
		self.args = args 
		self.kwargs = kwargs 

	def run(self):
		self.target(*self.args, **self.kwargs)

# 线程运行函数
def recv_machine_status(machine_status):  #socket
    print("recv_machine_status:-------------------------")
    json_str = machine_status.decode()
    print(json_str)
    parse_msg(json_str)


if __name__ == "__main__":
    address = (("0.0.0.0", 9999))
    # 创建套接字
    server = socket(AF_INET, SOCK_DGRAM) #创建数据报套接字

    # 绑定
    server.bind(address)
    print("服务器已启动:", address)

    # 收发消息
    while True:
        data, addr = server.recvfrom(1024) # 接收数据
        print("recv from:", addr)

        #　创建线程
        t = MyThread(target = recv_machine_status, args=(data,))
        t.start()
        t.join()

    server.close()