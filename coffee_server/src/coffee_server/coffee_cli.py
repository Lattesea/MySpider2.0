# coffee_cli.py
# 咖啡监控程序客户端模拟程序
# 通过100个线程，模拟100台被监控的咖啡机向服务器发送数据
from socket import *
import sys, time, random
from threading import Thread
import datetime

address = ("127.0.0.1", 9999)

# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

#消息收发
def coffee_maker(MACHINE_ID):
    # 初始值设置
    ENVIROMENT_TEMPERATURE = round(random.uniform(23, 30))   # 工作环境温度
    BOILER_TEMPERATURE = random.uniform(73, 93)              # 锅炉温度
    BOILER_PRESSUE = 4                                       # 锅炉压力
    MATERIAL_REMAINDER = [1.0, 1.0, 1.0]                     # 配料桶配料余量
    ORDERS_NUM = 0                                           # 当日销售数量
    ORDERS_AMT = 0.00                                        # 当日销售金额
    while True:
        times = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 上报时间
        data = '''
        {
            "MACHINE_ID":"%d",
            "RECV_TIME":"%s",
            "ENVIROMENT_TEMPERATURE":"%d",
            "BOILER_TEMPERATURE":"%.2f",
            "BOILER_PRESSUE":"%d",
            "MATERIAL_REMAINDER":%s,
            "ORDERS_NUM":"%d",
            "ORDERS_AMT":"%.2f"
        }
        '''%(MACHINE_ID,times,ENVIROMENT_TEMPERATURE,BOILER_TEMPERATURE,BOILER_PRESSUE,MATERIAL_REMAINDER,ORDERS_NUM,ORDERS_AMT)
        print('设备编号：',MACHINE_ID)

        ENVIROMENT_TEMPERATURE = round(random.uniform(ENVIROMENT_TEMPERATURE-2, ENVIROMENT_TEMPERATURE+2))
        BOILER_TEMPERATURE = round(random.uniform(BOILER_TEMPERATURE-5, BOILER_TEMPERATURE+5), 1)
        BOILER_PRESSUE = round(random.uniform(BOILER_PRESSUE-1, BOILER_PRESSUE+1))
        for i in range(len(MATERIAL_REMAINDER)):
            MATERIAL_REMAINDER[i] = round(MATERIAL_REMAINDER[i] - 0.1,2)
            if MATERIAL_REMAINDER[i] == 0:
                MATERIAL_REMAINDER = [1.0, 1.0, 1.0]
        ORDERS_NUM += 1
        ORDERS_AMT = ORDERS_NUM * 12

        if MACHINE_ID not in [11,38,91]:   # 模拟故障设备
            sockfd.sendto(data.encode(),address)
        time.sleep(60)
    sockfd.close()

t_list = []
for i in range(100):
    MACHINE_ID = i+1
    t = Thread(target=coffee_maker,args=(MACHINE_ID,))
    t_list.append(t)
    t.start()

for t in t_list:
    t.join()