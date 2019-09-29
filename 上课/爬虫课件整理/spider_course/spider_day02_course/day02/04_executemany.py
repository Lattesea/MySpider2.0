'''使用executemany()方法插入2条表记录'''
import pymysql

# 1.创建2个对象
db = pymysql.connect(
    'localhost','root','123456','maoyandb',charset='utf8'
)
cursor = db.cursor()
# 2. 直接执行sql命令
ins = 'insert into filmtab values(%s,%s,%s)'
film_list = [('月光宝盒','周星驰','1993'),('大圣娶亲','周星驰','1993')]
cursor.executemany(ins,film_list)
# 3. 提交到数据库执行
db.commit()
cursor.close()
db.close()


















