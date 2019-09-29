from selenium import webdriver

url = 'https://maoyan.com/board/4'
browser = webdriver.Chrome()
browser.get(url)
# 基准xpath: [<selenium xxx li at xxx>,<selenium xxx li at>]
li_list = browser.find_elements_by_xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
for li in li_list:
    item = {}
    # info_list: ['1', '霸王别姬', '主演：张国荣', '上映时间：1993-01-01', '9.5']
    info_list = li.text.split('\n')
    item['number'] = info_list[0]
    item['name'] = info_list[1]
    item['star'] = info_list[2]
    item['time'] = info_list[3]
    item['score'] = info_list[4]

    print(item)

















