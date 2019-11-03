import csv
import datetime
import json
import random,re

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest
from django.http import HttpResponse
from .models import *
from .form import *


def index(request):
    # return HttpResponse("hello, world!")
    print("views.manage")
    return render(request, 'index.html', context={'title':'首页'}, status=200)


def map_views(request):
    machine_infos = EqInfo.objects.all()
    machine_infos = list(machine_infos)
    dic_all = {}
    i = 1
    for machine_info in machine_infos:
        name = machine_info.name
        position_lat = machine_info.position.split(',')[1]
        position_lng = machine_info.position.split(',')[0]
        dic = {'name': name, 'lat': float(position_lat), 'lng': float(position_lng)}
        dic_all['dic'+str(i)] = dic
        i+=1


    machine_warnings = EqWarning.objects.all()
    machine_warnings = list(machine_warnings)
    warning_all = {}
    x = 1
    for machine_warning in machine_warnings:

        machine_id = machine_warning.machine_id
        machine_warning_infos = EqInfo.objects.filter(machine_id=machine_id)
        for machine_warning_info in machine_warning_infos:


            name = machine_warning_info.name
            position_lat = machine_warning_info.position.split(',')[1]
            position_lng = machine_warning_info.position.split(',')[0]
            dic = {'name':name,'machine_id': machine_id, 'lat': float(position_lat), 'lng': float(position_lng)}
            warning_all['dic'+str(x)] = dic
        x+=1


    all_dic = {'dic_all': json.dumps(dic_all), 'warning_all': json.dumps(warning_all)}
    print(all_dic['dic_all'])
    print(all_dic['warning_all'])
    return render(request,'map_test.html',all_dic)