import json

# json.dumps() : python类型 -> json格式
item = {'name':'QQ','app_id':'001'}
print(type(item))
item = json.dumps(item)
print(type(item))

# json.dump() : python类型->json串->存到json文件
app_list = [
    {'name':'qq','app_id':'001'},
    {'name':'微信','app_id':'002'}
]

# 小米应用商店,抓取的数据保存 xiaomi.json 中
with open('xiaomi.json','w') as f:
    json.dump(app_list,f,ensure_ascii=False)




















