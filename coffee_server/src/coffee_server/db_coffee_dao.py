# db_coffee_dao.py
# 数据访问对象
from db_helper import *
from msg import *


class CoffeeDao:
    # 构造函数
    def __init__(self, db_helper):
        self.db_helper = DBHelper()  # 创建DBHelper对象
        self.db_helper.open_conn()  # 打开数据库连接

    # 析构函数
    def __del__(self):
        self.db_helper.close_conn()  # 关闭数据库连接

    # 新增订单
    def insert_machine_status(self, msg):  # 插入对象
        try:
            sql = '''insert into manage_eqstate(MACHINE_ID,
                    RECV_TIME,
                    ENVIROMENT_TEMPERATURE,
                    BOILER_TEMPERATURE,
                    BOILER_PRESSUE,
                    MATERIAL_REMAINDER,
                    ORDERS_NUM,
                    ORDERS_AMT)
                values(%s,'%s','%s','%s','%s','%s',%s,%s)
            ''' % (msg.machine_id, msg.recv_time, msg.enviroment_temperature,
                   msg.boiler_temperature, msg.boiler_pressue, msg.material_remainder,
                   msg.orders_num, msg.orders_amt)

            print("\nsql:%s\n" % sql)
            result = self.db_helper.do_update(sql)
            self.db_helper.db_conn.commit()
            print("插入设备状态表成功")
            return result
        except Exception as e:
            print("插入设备状态表出错")
            self.db_helper.db_conn.rollback()
            return None

    # 查询每台设备最后发送数据的时间到当前时间的差值（单位：秒）
    def query_machine_last_send(self):
        sql = '''
            SELECT a.machine_id,
                TIMESTAMPDIFF(SECOND, b.last_time, NOW()) time_diff
            FROM
                manage_eqinfo a
            LEFT JOIN (
                SELECT
                    max(recv_time) last_time,
                    machine_id machine_id
                FROM
                    manage_eqstate
                GROUP BY
                    machine_id
            ) AS b ON a.machine_id = b.machine_id
        '''
        result = self.db_helper.do_query(sql)
        return result

    def query_machine_last_send_temperature(self):
        sql = '''
                SELECT a.machine_id,
                    TIMESTAMPDIFF(SECOND, b.last_time, NOW()) time_diff
                FROM
                    manage_eqinfo a
                LEFT JOIN (
                    SELECT
                        max(recv_time) last_time,
                        machine_id machine_id
                    FROM
                        manage_eqstate
                    GROUP BY
                        machine_id
                ) AS b ON a.machine_id = b.machine_id
            '''


    # 查询所有设备状态信息
    def get_all_eqstate(self):
        sql = "select * from manage_eqstate"
        result = self.db_helper.do_query(sql)
        return result

    # 根据设备编号查询该设备是否有报警信息
    def get_warning_by_machine_id(self, machine_id):
        try:
            sql = '''select * from manage_eqwarning 
                    where machine_id = %d''' % machine_id

            print("\nsql:%s\n" % sql)
            result = self.db_helper.do_query(sql)
            return result
        except Exception as e:
            print("查询设备报警信息失败")
            print(e)
            return None

    # 更新设备状态
    def update_machine_state(self, id, status, commit_flag):
        sql = '''update manage_eqinfo
                set status = %d
                where machine_id = %d
        ''' % (status, id)

        print(sql)

        try:
            result = self.db_helper.do_update(sql)
            self.db_helper.db_conn.commit()
            print("更新或插入设备警告表成功")
            return result
        except Exception as e:
            print("更新或插入设备警告表成功出错")
            self.db_helper.db_conn.rollback()
            return None

    def add_machine_warnings(self, id, msg):  # 插入对象
        result = self.get_warning_by_machine_id(id)
        if not result:
            sql = '''insert into manage_eqwarning(id, MACHINE_ID, alter_msg, check_time)   
                values(NULL, %d, '%s', now())
            ''' % (id, msg)
        else:
            sql = '''update manage_eqwarning
                    set alter_msg = '%s',
                        check_time = now()  
                    where MACHINE_ID = %d ''' % (msg, id)
        print(sql)
        try:
            result = self.db_helper.do_update(sql)  # 登记设备故障表
            # 修改设备信息表中设备状态
            sql = '''update manage_eqinfo
                    set status = 3
                    where machine_id = %d''' % id

            result = self.db_helper.do_update(sql)

            self.db_helper.db_conn.commit()
            print("更新或插入设备警告表成功")
            return result
        except Exception as e:
            print("更新或插入设备警告表成功出错")
            self.db_helper.db_conn.rollback()
            return None
