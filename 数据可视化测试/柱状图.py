# -*- coding: utf-8 -*- 
# @Time : 2019/12/13 20:25 
# @Author : lattesea 
# @File : 柱状图.py
from pyecharts import Bar

x = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋"]
y1 = [5, 20, 36, 10, 75]
y2 = [10, 25, 8, 60, 20]

bar = Bar(title = "产品月销量",width = 600,height = 420)
bar.add(name = "商家A", x_axis = x, y_axis = y1)
bar.add(name = "商家B", x_axis = x, y_axis = y2,is_xaxis_boundarygap =True)

# 导出绘图html文件，可直接用浏览器打开
bar.render('柱形图示范.html')