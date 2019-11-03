# db_helper.py
# pymysql数据库访问类
from db_conf import *
import pymysql


class DBHelper:
    def __init__(self):  # 构造方法
        self.db_conn = None  # 数据库连接对象

    def open_conn(self):  # 连接数据库
        try:
            self.db_conn = pymysql.connect(host, user, password, dbname)
        except Exception as e:
            print("连接数据库错误")
            print(e)
        else:
            print("连接数据库成功")

    def close_conn(self):  # 关闭数据库
        try:
            self.db_conn.close()
        except Exception as e:
            print("关闭数据库错误")
            print(e)
        else:
            print("关闭数据库成功")

    def do_query(self, sql):  # 查询
        try:
            cursor = self.db_conn.cursor()  # 获取游标
            if not sql:
                print("SQL语句对象不合法")
                return None
            if sql == "":
                print("SQL语句不能为空")
                return None

            # 执行查询
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()  # 关闭游标
            return result
        except Exception as e:
            print("执行SQL语句错误")
            print(e)
            return None

    def do_update(self, sql):  # 执行增删改
        try:
            cursor = self.db_conn.cursor()  # 获取游标
            if not sql:
                print("SQL语句对象不合法")
                return None
            if sql == "":
                print("SQL语句不能为空")
                return None

            # 执行查询
            result = cursor.execute(sql)
            self.db_conn.commit()
            cursor.close()  # 关闭游标
            return result
        except Exception as e:
            self.db_conn.rollback()
            print("执行SQL语句错误")
            print(e)
            return None
