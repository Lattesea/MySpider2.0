import matplotlib.pyplot as plt
import re
import pytesseract
from PIL import Image
from aip import AipOcr
import json
import numpy as np
import time
from scipy import interpolate

def smooth(x,y):
    func = interpolate.interp1d(x, y, kind='cubic')

def baidu(filePath):
    # 定义常量
    APP_ID = '17711416'
    API_KEY = 'EYb372x8lvKK9c5dBUXhwzFV'
    SECRET_KEY = 'M9X5TSh3lBvsXphfOaEdqYqnToB1VoAo'

    # 初始化AipFace对象
    aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    # # 读取图片
    # filePath = "test.png"

    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

            # 定义参数变量

    options = {
        'detect_direction': 'true',
        'language_type': 'CHN_ENG',
    }

    # 调用通用文字识别接口
    result = aipOcr.basicGeneral(get_file_content(filePath), options)
    # print(type(result))
    print(result)

    if result['words_result']:
        return result['words_result'][0]['words']
    else:
        return ''
    # for i in result['words_result']:
    #     if ord(i['words'][0]) > 128:
    #         print(i['words'])
    # return result['words_result'][0]['words']


def Draw(map):
    plt.axis('off')
    # 数据格式为：  [{ : [[x],[y]]},{},{}{}{}]
    map_list = []
    count = 0
    for font in map:

        # count += 1
        # if count == 4:
        #     break
        # [[  [],[]  ]]
        for key,value in font.items():
            # print(key)
            # print(value)
            x = value[0]
            y = value[1]

            x = np.array(x)
            y = np.array(y)
            # vals = list(font.values())
            # print(vals[0])
            # print()
            color = 'black'
            plt.axis('off')
            plt.plot(x, y, color='black')
            plt.fill(x, y, color='black')

            filename = r'./font_image/' + key + '.png'
            plt.savefig(filename)
            # 这里一定要记得close，否则以后的图都会在前一个图的基础上叠加
            plt.close()

            word = baidu(filename)
            map_list.append({key:word})
    return map_list






if __name__ == '__main__':

    start = time.time()
    with open('01.xml','r',encoding='utf-8') as file:
        xml = file.read()

    # print(xml)

    # 获取每一个 <TTGlyph.*> ... </TTGlyph>
    lst = re.findall(r'<TTGlyph name="uni.*>[\w\W]*?</TTGlyph>',xml)
    # print(lst[0])


    map = []
    for TTGlyph in lst:
        # 提取出每个字的编码 <TTGlyph name="(.*?)"
        unicode = re.findall(r'<TTGlyph name="(.*?)"', TTGlyph)[0]
        # print(unicode)
        contours = re.findall(r'<contour>([\w\W]*?)</contour>',TTGlyph)

        # 该字的每个部首对应的坐标
        x = []
        y = []
        for contour in contours:
            x_axis = ([int(i) for i in re.findall(r'<pt x="(.*?)" y=', contour)])
            y_axis = ([int(i) for i in re.findall(r'y="(.*?)" on=', contour)])

            x += x_axis + [x_axis[0]] + [None]
            y += y_axis + [y_axis[0]] + [None]

        # 数据格式为：  [{ : [[x],[y]]},{},{}{}{}]
        map.append({unicode:[x, y]})


    # print(map)


    with open('map.json','w',encoding='utf-8') as file:
        file.write(json.dumps(map,indent=2))

    print('写入完毕')

    map_list = Draw(map)

    total = len(map_list)
    print('总共有 %d 个字'%total)

    count = 0
    for map in map_list:
        if list(map.values())[0]:
            count += 1
    print('总共识别出 %d 个字',count)
    print('识别率为：%.2f'%(count/total*100)+'%')


    with open('map_list.json','w',encoding='utf-8') as file:
        file.write(json.dumps(map_list,indent=2,ensure_ascii=False))

    end = time.time()

    print('匹配好一个woff用时：',(end - start))




