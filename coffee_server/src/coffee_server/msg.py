# msg.py
# 消息类
'''
    {
        "MACHINE_ID":1,
        "RECV_TIME":"2019-04-07 12:34:56"
        "ENVIROMENT_TEMPERATURE":26
        "BOILER_TEMPERATURE":75.6
        "BOILER_PRESSUE":4
        "MATERIAL_REMAINDER":[0.4,0.4,0.5]
        "ORDERS_NUM":30
        "ORDERS_AMT":450.00
    }
'''

class Msg:
    def __init__(self, machine_id, recv_time, enviroment_temperature,
                boiler_temperature, boiler_pressue, material_remainder,
                orders_num, orders_amt):
        self.machine_id = machine_id
        self.recv_time = recv_time
        self.enviroment_temperature = enviroment_temperature
        self.boiler_temperature = boiler_temperature
        self.boiler_pressue = boiler_pressue
        self.material_remainder = material_remainder
        self.orders_num = int(orders_num)
        self.orders_amt = orders_amt

    def __str__(self):
        ret = "%s,%s,%s,%s,%s,%s,%d,%s" % (self.machine_id, self.recv_time,
                self.enviroment_temperature, self.boiler_temperature,
                self.boiler_pressue, self.material_remainder,
                self.orders_num, self.orders_amt)
        return ret

    

