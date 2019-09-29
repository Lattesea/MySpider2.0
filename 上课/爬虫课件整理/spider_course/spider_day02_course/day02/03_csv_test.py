import csv

with open('fengyun.csv','w') as f:
    writer = csv.writer(f)
    # 写1行 - []
    writer.writerow(['步惊云','超哥哥'])
    # 写n行 - [(),(),()]
    writer.writerows([('聂风','梦'),('秦霜','孔慈')])






