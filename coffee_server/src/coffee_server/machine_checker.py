# machine_checker.py
# 设备故障判断，对设备上报的数据进行查询、分析
# 如果某个设备一定时间未报告状态，或关键数据超标
# 则插入一笔数据到设备故障表
from db_coffee_dao import *
from db_helper import *
from db_conf import *
import time


def main():
    db_helper = DBHelper()  # 实例化一个数据访问对象
    coffeeDao = CoffeeDao(db_helper)

    while True:
        do_check_last_send_time(coffeeDao)  # 检查设备最后发送数据时间
        do_check_last_send_temp(coffeeDao)  # 检查设备最后发送数据温度
        time.sleep(120)


# 查询所有设备最后发送数据时间到当前时间点的事件间隔，并判断故障
def do_check_last_send_time(coffeeDao):
    result = coffeeDao.query_machine_last_send()
    for i in result:
        machine_id = int(i[0])  # 设备ID
        diff_time = i[1]  # 到当前时间点时间差
        alert_msg = ""
        is_broken = False

        if not diff_time:
            is_broken = True
            alert_msg = "编号%d的咖啡机没有上报状态，可能存在故障" % machine_id
        elif diff_time >= machine_max_interval:
            is_broken = True
            alert_msg = "编号%d的咖啡机最后一次上报状态已经%d秒，可能存在故障" % (machine_id, diff_time)

        if is_broken:
            result = coffeeDao.add_machine_warnings(machine_id, alert_msg)


def do_check_last_send_temp(coffeeDao):
    result = coffeeDao.get_last_data()
    for row in result:
        machine_id = int(row[1])  # 设备编号
        boiler_tempr = row[4]  # 锅炉温度
        eqtype = coffeeDao.get_catetory_info_by_machine_id(machine_id)
        if len(eqtype) <= 0:
            pass
        else:
            work_boiler_tempr = float(eqtype[0][10])
            boiler_tempr = float(boiler_tempr)
            if boiler_tempr > work_boiler_tempr:
                alert_msg = "编号%d的设备锅炉温度超标" % machine_id
                print(alert_msg)
                coffeeDao.add_machine_warnings(machine_id, alert_msg)


if __name__ == "__main__":
    main()
