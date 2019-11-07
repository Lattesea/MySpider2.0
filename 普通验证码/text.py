import requests
import json

import base64

import urllib.parse

from PIL import Image

# class GetCode(object):
#
#     def __init__(self):
#         self.url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}"
#         self.api = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token={}"
#         self.header = {
#             "Content-Type":'application/json; charset=UTF-8'
#         }
#
#         self.key = ""
#         self.secret = ""
#
#
#     def get_accesstoken(self):
#
#         res = requests.post(self.url.format(self.key,self.secret),headers=self.header)
#         content = res.text
#         if (content):
#
#             return json.loads(content)["access_token"]
#
#     def init_table(self,threshold=155):
#         table = []
#         for i in range(256):
#             if i < threshold:
#                 table.append(0)
#             else:
#                 table.append(1)
#         return table
#
#
#
#     def opt_image(self):
#         im = Image.open("66.png")
#
#         im = im.convert('L')
#         im = im.point(self.init_table(), '1')
#         im.save('66_s.png')
#         return "66_s.png"
#
#     def get_file_content(self,file_path):
#         with open(file_path, 'rb') as fp:
#             base64_data = base64.b64encode(fp.read())
#             s = base64_data.decode()
#
#             data = {}
#             data['image'] = s
#
#             decoded_data = urllib.parse.urlencode(data)
#             return decoded_data
#
#
#     def show_code(self):
#         image = self.get_file_content(self.opt_image())
#         headers = {
#             "Content-Type":	"application/x-www-form-urlencoded"
#         }
#         res = requests.post(self.api.format(self.get_accesstoken()),headers=headers,data=image)
#         print(res.text)


from aip import AipOcr

# 定义常量
APP_ID = '17711416'
API_KEY = 'EYb372x8lvKK9c5dBUXhwzFV'
SECRET_KEY = 'M9X5TSh3lBvsXphfOaEdqYqnToB1VoAo'

# 初始化文字识别分类器
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "2.png"


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 定义参数变量
options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}

# 网络图片文字文字识别接口
result = aipOcr.webImage(get_file_content(filePath), options)

print(result)

# if __name__ == '__main__':
#     code = GetCode()
#     code.show_code()
