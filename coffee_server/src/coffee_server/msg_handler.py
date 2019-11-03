# msg.py
# 消息处理模块
from msg import *
import json
from db_coffee_dao import *

def parse_msg(msg_str):
        print(msg_str)
        machine_status = json.loads(msg_str)

        machine_id = machine_status['MACHINE_ID']
        recv_time = machine_status['RECV_TIME']
        enviroment_temperature = machine_status['ENVIROMENT_TEMPERATURE']
        boiler_temperature = machine_status['BOILER_TEMPERATURE']
        boiler_pressue = machine_status['BOILER_PRESSUE']
        material_remainder = machine_status['MATERIAL_REMAINDER']
        orders_num = machine_status['ORDERS_NUM']
        orders_amt = machine_status['ORDERS_AMT']

        msg = Msg(machine_id, recv_time, enviroment_temperature, boiler_temperature,
                boiler_pressue, material_remainder, orders_num, orders_amt)
        print(msg)

        db_helper = DBHelper()  #实例化一个数据访问对象
        coffeeDao = CoffeeDao(db_helper)

        coffeeDao.insert_machine_status(msg)


