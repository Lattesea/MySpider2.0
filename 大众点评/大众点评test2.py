#!/usr/bin/env python
# encoding: utf-8
# @Time:2019-10-23 5:12
# @Author: Lattesea
# @File: 大众点评test2.py
import requests
import json
import re
from fake_useragent import UserAgent
from fontTools.ttLib import TTFont


class DianpingSpider(object):
    def __init__(self):
        self.url = 'http://www.dianping.com/ajax/json/shopDynamic/allReview?'

    def get_headers(self):
        ua = UserAgent()
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Cookie": "cityid=4; _hc.v=2e96cbeb-4dcf-0cee-e3c6-e1b2eae4e61d.1569347054; baidusearch_ab=shopreviewlist%3AA%3A1; _lxsdk_cuid=16d645fa60cc8-0046b4de207f1c-7373e61-144000-16d645fa60cc8; _lxsdk=16d645fa60cc8-0046b4de207f1c-7373e61-144000-16d645fa60cc8; seouser_ab=shopreviewlist%3AA%3A1; cy=4; cye=guangzhou; default_ab=shopreviewlist%3AA%3A1; dper=9d7cb8868867648f5d1932800f94703bd7640d5b0ca0d38f85a38e42f14acfe6f0cc0f5d7eaf13e9f7c134a7bdd13d3fef03eec18f4f2870bdce40b29582b61158271f2e3a729b897e38da56b13fe99652744ee97bcf10a4e585c6f3c903847b; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_3896667530; ctu=51ed98c68ae176af9e3e6a65b79a06e959497a01fe3407722f0508809b1f6adf; uamo=18998261232; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; s_ViewType=10; _lxsdk_s=16df52b0955-f92-0d4-7e1%7C%7C26",
            "Host": "www.dianping.com",
            "Referer": "http://www.dianping.com/shop/66250176",
            "User-Agent": ua.random,
            "X-Requested-With": "XMLHttpRequest"
        }
        return headers

    def get_font_map():
        # 这个字体文件需要先析网页，找到这个url，然后下载下来到本地，然后使用TTFont()加载字体文件
        #       字体文件的名字
        font = TTFont('219b5cf4.woff')
        # 得到cmap 字体对应代码->字体名字
        font_cmap = font.getBestCmap()
        # 得到所有的字体名字
        font_names = font.getGlyphOrder()
        # 这个文字是先使用fontCreator软件打开字体文件，然后查看到字体，从而得到的数据
        texts = [
            '', '', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', '0', '店', '中', '美', '家', '馆', '小', '车', '大',
            '市', '公', '酒', '行', '国', '品', '发', '电', '金', '心',
            '业', '商', '司', '超', '生', '装', '园', '场', '食', '有',
            '新', '限', '天', '面', '工', '服', '海', '华', '水', '房',
            '饰', '城', '乐', '汽', '香', '部', '利', '子', '老', '艺',
            '花', '专', '东', '肉', '菜', '学', '福', '饭', '人', '百',
            '餐', '茶', '务', '通', '味', '所', '山', '区', '门', '药',
            '银', '农', '龙', '停', '尚', '安', '广', '鑫', '一', '容',
            '动', '南', '具', '源', '兴', '鲜', '记', '时', '机', '烤',
            '文', '康', '信', '果', '阳', '理', '锅', '宝', '达', '地',
            '儿', '衣', '特', '产', '西', '批', '坊', '州', '牛', '佳',
            '化', '五', '米', '修', '爱', '北', '养', '卖', '建', '材',
            '三', '会', '鸡', '室', '红', '站', '德', '王', '光', '名',
            '丽', '油', '院', '堂', '烧', '江', '社', '合', '星', '货',
            '型', '村', '自', '科', '快', '便', '日', '民', '营', '和',
            '活', '童', '明', '器', '烟', '育', '宾', '精', '屋', '经',
            '居', '庄', '石', '顺', '林', '尔', '县', '手', '厅', '销',
            '用', '好', '客', '火', '雅', '盛', '体', '旅', '之', '鞋',
            '辣', '作', '粉', '包', '楼', '校', '鱼', '平', '彩', '上',
            '吧', '保', '永', '万', '物', '教', '吃', '设', '医', '正',
            '造', '丰', '健', '点', '汤', '网', '庆', '技', '斯', '洗',
            '料', '配', '汇', '木', '缘', '加', '麻', '联', '卫', '川',
            '泰', '色', '世', '方', '寓', '风', '幼', '羊', '烫', '来',
            '高', '厂', '兰', '阿', '贝', '皮', '全', '女', '拉', '成',
            '云', '维', '贸', '道', '术', '运', '都', '口', '博', '河',
            '瑞', '宏', '京', '际', '路', '祥', '青', '镇', '厨', '培',
            '力', '惠', '连', '马', '鸿', '钢', '训', '影', '甲', '助',
            '窗', '布', '富', '牌', '头', '四', '多', '妆', '吉', '苑',
            '沙', '恒', '隆', '春', '干', '饼', '氏', '里', '二', '管',
            '诚', '制', '售', '嘉', '长', '轩', '杂', '副', '清', '计',
            '黄', '讯', '太', '鸭', '号', '街', '交', '与', '叉', '附',
            '近', '层', '旁', '对', '巷', '栋', '环', '省', '桥', '湖',
            '段', '乡', '厦', '府', '铺', '内', '侧', '元', '购', '前',
            '幢', '滨', '处', '向', '座', '下', '県', '凤', '港', '开',
            '关', '景', '泉', '塘', '放', '昌', '线', '湾', '政', '步',
            '宁', '解', '白', '田', '町', '溪', '十', '八', '古', '双',
            '胜', '本', '单', '同', '九', '迎', '第', '台', '玉', '锦',
            '底', '后', '七', '斜', '期', '武', '岭', '松', '角', '纪',
            '朝', '峰', '六', '振', '珠', '局', '岗', '洲', '横', '边',
            '济', '井', '办', '汉', '代', '临', '弄', '团', '外', '塔',
            '杨', '铁', '浦', '字', '年', '岛', '陵', '原', '梅', '进',
            '荣', '友', '虹', '央', '桂', '沿', '事', '津', '凯', '莲',
            '丁', '秀', '柳', '集', '紫', '旗', '张', '谷', '的', '是',
            '不', '了', '很', '还', '个', '也', '这', '我', '就', '在',
            '以', '可', '到', '错', '没', '去', '过', '感', '次', '要',
            '比', '觉', '看', '得', '说', '常', '真', '们', '但', '最',
            '喜', '哈', '么', '别', '位', '能', '较', '境', '非', '为',
            '欢', '然', '他', '挺', '着', '价', '那', '意', '种', '想',
            '出', '员', '两', '推', '做', '排', '实', '分', '间', '甜',
            '度', '起', '满', '给', '热', '完', '格', '荐', '喝', '等',
            '其', '再', '几', '只', '现', '朋', '候', '样', '直', '而',
            '买', '于', '般', '豆', '量', '选', '奶', '打', '每', '评',
            '少', '算', '又', '因', '情', '找', '些', '份', '置', '适',
            '什', '蛋', '师', '气', '你', '姐', '棒', '试', '总', '定',
            '啊', '足', '级', '整', '带', '虾', '如', '态', '且', '尝',
            '主', '话', '强', '当', '更', '板', '知', '己', '无', '酸',
            '让', '入', '啦', '式', '笑', '赞', '片', '酱', '差', '像',
            '提', '队', '走', '嫩', '才', '刚', '午', '接', '重', '串',
            '回', '晚', '微', '周', '值', '费', '性', '桌', '拍', '跟',
            '块', '调', '糕'
        ]

        font_name_map = {}

        # 将 字体名字 和 我们查看到的值 组成一个字典
        for index, value in enumerate(texts):
            font_name_map[font_names[index]] = value

        return font_cmap, font_name_map

    def parse(self):
        params = {
            "shopId": "66250176",
            "cityId": "4",
            "shopType": "10",
            "tcv": "c78wfqvotm",
            "_token": "eJxVj1FvgjAUhf/LfV0DbcUWSXww0xgRtoyKZhgfABUJItV2Ki777yuJe9jTOee79yT3fsNltgWPYIwdguC6u4AHxMIWAwRamUmfE84HjHHOMIL8H3MpdxBkl+UYvDUbYMQp3XQgMnlN+j2GXOZs0NNSY6mDOoFsZlbgoLX0bPt2u1nbMj3J8lRYeVPb6tBImzHax4R3l4Bp1IuuwXoEUcY6UHXAaPpU/ZdD84MpqbI4Gbfz7wuhHHXeR6FaLKO2HcyFoG2Qk0DEveAx0W+xuL63r+5IyDKZJlU69c9Zsa8Ox4+V1M3nNFWr41dW+1GyfCmzWoqxnFdKq8rFutXhvLX9IJfx6HzPi0kxHMLPL00uY3c=",
            "uuid": "2e96cbeb-4dcf-0cee-e3c6-e1b2eae4e61d.1569347054",
            "platform": "1",
            "partner": "150",
            "optimusCode": "10",
            "originUrl": "http%3A%2F%2Fwww.dianping.com%2Fshop%2F66250176"
        }
        html_json = requests.get(url=self.url, headers=self.get_headers(), params=params).text
        html_json = re.sub('<.*?>', '', html_json)
        html_py = json.loads(html_json)
        print(html_py)
        all_review = html_py['reviewAllDOList']
        for review in all_review:
            # 得到用户名
            username = review['user']['userNickName']
            # 得到评论内容
            content = review['reviewDataVO']['reviewBody']
            # 这里我们就是简单的显示出内容就是了，没有进行储存
            print('*' * 30, '\n', username, content, '\n', '*' * 30)

    def run(self):
        self.parse()


if __name__ == '__main__':
    spider = DianpingSpider()
    spider.run()
