from django.db import models


# Create your models here.
class EqType(models.Model):
    category_id = models.AutoField('类型编号', primary_key=True)
    name = models.CharField('类型名称', max_length=64, default="")
    size = models.CharField('尺寸', max_length=64, default="")
    weight = models.DecimalField('重量', max_digits=10, decimal_places=2)
    power = models.CharField('重量', max_length=32, default="")
    dissipation = models.IntegerField('功率')
    material_buckets = models.IntegerField('配料桶数')
    water_proofing_grade = models.CharField('防水级别', max_length=16, default="")
    pipe_standard = models.CharField('水管标准', max_length=16, default="")
    inflow_pressue = models.CharField('供水压力', max_length=16, default="")
    work_temperature = models.CharField('工作温度', max_length=16, default="")
    screen_size = models.DecimalField('屏幕尺寸', max_digits=10, decimal_places=2)
    comm_interface = models.CharField('通信接口', max_length=32, default="")
    os = models.CharField('操作系统', max_length=32, default="")
    payment_cate = models.CharField('支付类型', max_length=32, default="")
    data_standard = models.CharField('数据标准', max_length=32, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '设备类型信息'
        verbose_name_plural = '设备类型信息'

class EqInfo(models.Model):
    machine_id = models.AutoField('设备编号', primary_key=True)
    category_id = models.IntegerField('设备类型')
    name = models.CharField('设备名称', max_length=64, default="")
    mac_addr = models.CharField('网卡地址', max_length=64, default="")
    addr = models.CharField('地址', max_length=128, default="")
    position = models.CharField('位置', max_length=64, default="")
    install_date= models.DateField('安装日期')
    install_emp_id = models.CharField('安装人员', max_length=16, default="")
    status = models.IntegerField('设备状态')
    mantain_emp_id= models.CharField('运维人员', max_length=16, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '设备信息'
        verbose_name_plural = '设备信息'


class EqState(models.Model):
    id = models.AutoField('编号', primary_key=True)
    machine_id = models.IntegerField('设备编号')
    recv_time = models.DateTimeField('状态上报时间')
    enviroment_temperature = models.CharField('工作环境温度', max_length=16, default="")
    boiler_temperature = models.CharField('锅炉温度', max_length=16, default="")
    boiler_pressue = models.CharField('锅炉压力', max_length=16, default="")
    material_remainder = models.CharField('配料桶余料', max_length=16, default="")
    orders_num = models.IntegerField('订单数量')
    orders_amt = models.DecimalField('订单总金额', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '设备状态'
        verbose_name_plural = '设备状态'


class EqWarning(models.Model):
    id = models.AutoField('编号', primary_key=True)
    machine_id = models.IntegerField('设备编号')
    alter_msg = models.CharField('异常信息', max_length=128, default="")
    check_time = models.DateTimeField('异常发现时间')

    def __str__(self):
        return self.machine_id

    class Meta:
        verbose_name = '设备报警'
        verbose_name_plural = '设备报警'