import execjs

with open('translate.js','r') as f:
    js_data = f.read()

# 执行js
exec_obj = execjs.compile(js_data)
sign = exec_obj.eval('e("china","320305.131321201")')

print(sign)


















