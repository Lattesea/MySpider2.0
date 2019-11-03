from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Type)
# admin.site.register(TypeDetail)
# admin.site.register(Product)

admin.site.site_title = '智能咖啡机监控系统'
admin.site.site_header = 'CoffeeMonitor'

# 自定义EqTypeAdmin类并继承ModelAdmin
@admin.register(EqType)
class EqTypeAdmin(admin.ModelAdmin):
    # 设置显示字段
    list_display = ['category_id', 'name', 'size', 'weight', 'power',
                'dissipation','material_buckets','water_proofing_grade',
                'pipe_standard','inflow_pressue','work_temperature','screen_size',
                'comm_interface','os','payment_cate','data_standard',
    ]


@admin.register(EqInfo)
class EqInfoAdmin(admin.ModelAdmin):
    # 设置显示字段
    list_display = ['machine_id', 'category_id', 'name', 'mac_addr', 'addr',
                'position','install_date','install_emp_id',
                'status','mantain_emp_id',
    ]


@admin.register(EqState)
class EqStateAdmin(admin.ModelAdmin):
    # 设置显示字段
    list_display = ['id', 'machine_id', 'recv_time', 'enviroment_temperature',
                'boiler_temperature','boiler_pressue','material_remainder',
                'orders_num','orders_amt',
    ]


@admin.register(EqWarning)
class EqWarningAdmin(admin.ModelAdmin):
    # 设置显示字段
    list_display = ['id','machine_id', 'alter_msg', 'check_time',]

















