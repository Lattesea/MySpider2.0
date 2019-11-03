from django.apps import AppConfig
import os
import pymysql

# pymysql.install_as_MySQLdb() #wdb 20190803 如果报mysqlclient未知道到就打开
default_app_config = 'manage.ManageConfig'

def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

class ManageConfig(AppConfig):
    print('Manage.config()')
    name = get_current_app_name(__file__)
    verbose_name = '网站首页'









































