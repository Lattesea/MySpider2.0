# DAY03

## Day02回顾

### 爬取网站思路

```python
1、先确定是否为动态加载网站
2、找URL规律
3、正则表达式
4、定义程序框架，补全并测试代码
```

### 数据持久化 - csv

```python
 import csv
 with open('xxx.csv','w') as f:
	writer = csv.writer(f)
 	writer.writerow([])
	writer.writerows([(),(),()])
```

### 数据持久化 - MySQL

```mysql
import pymysql

# __init__(self)：
	self.db = pymysql.connect('IP',... ...)
	self.cursor = self.db.cursor()
# write_data(self):
	self.cursor.execute('sql',[data1])
	self.cursor.executemany('sql',[(data1),(data2),(data3)])
	self.db.commit()
# main(self):
	self.cursor.close()
	self.db.close()
```

### 数据持久化 - MongoDB

```mysql
import pymongo

# __init__(self)：
	self.conn = pymongo.MongoClient('IP',27017)
	self.db = self.conn['db_name']
	self.myset = self.db['set_name']
	
# write_data(self):
	self.myset.insert_one(dict)
	self.myset.insert_many([{},{},{}])

# MongoDB - Commmand
>show dbs
>use db_name
>show collections
>db.collection_name.find().pretty()
>db.collection_name.count()
>db.collection_name.drop()
>db.dropDatabase()
```

### 多级页面数据抓取

```python
# 整体思路 
1、爬取一级页面,提取 所需数据+链接,继续跟进
2、爬取二级页面,提取 所需数据+链接,继续跟进
3、... ... 
# 代码实现思路
1、所有数据最终都会在一级页面遍历每条数据时全部拿到
2、避免重复代码 - 请求、解析需定义函数
```

## **Day03笔记**

## 电影天堂二级页面抓取案例



### **领取任务**

```python
# 地址
电影天堂 - 2019年新片精品 - 更多
# 目标
电影名称、下载链接

# 分析
*********一级页面需抓取***********
        1、电影详情页链接
        
*********二级页面需抓取***********
        1、电影名称
  		  2、电影下载链接
```

### 实现步骤

- **1、确定响应内容中是否存在所需抓取数据**
- **2、找URL规律**

```python
第1页 ：https://www.dytt8.net/html/gndy/dyzz/list_23_1.html
第2页 ：https://www.dytt8.net/html/gndy/dyzz/list_23_2.html
第n页 ：https://www.dytt8.net/html/gndy/dyzz/list_23_n.html
```

- **3、写正则表达式**

```python
1、一级页面正则表达式
   <table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>
2、二级页面正则表达式
   <div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>.*?<td style="WORD-WRAP.*?>.*?>(.*?)</a> 
```

- **4、代码实现**

```python

```

- **5、练习**

  把电影天堂数据存入MySQL数据库 - 增量爬取

  ```python
  # 思路
  # 1、MySQL中新建表 request_finger,存储所有爬取过的链接的指纹
  # 2、在爬取之前,先判断该指纹是否爬取过,如果爬取过,则不再继续爬取
  ```

  **练习代码实现**

  ```mysql
  # 建库建表
  create database filmskydb charset utf8;
  use filmskydb;
  create table request_finger(
  finger char(32)
  )charset=utf8;
  create table filmtab(
  name varchar(200),
  download varchar(500)
  )charset=utf8;
  ```

  ```python
  
  ```

## requests模块

### 安装

- **Linux**

```python
sudo pip3 install requests
```

- **Windows**

```python
# 方法一
   进入cmd命令行 ：python -m pip install requests
# 方法二
   右键管理员进入cmd命令行 ：pip install requests
```

### requests.get()

- **作用**

```python
# 向网站发起请求,并获取响应对象
res = requests.get(url,headers=headers)
```

- **参数**

```python
1、url ：需要抓取的URL地址
2、headers : 请求头
3、timeout : 超时时间，超过时间会抛出异常
```

- **响应对象(res)属性**

```python
1、encoding ：响应字符编码
   res.encoding = 'utf-8'
2、text ：字符串
3、content ：字节流
4、status_code ：HTTP响应码
5、url ：实际数据的URL地址
```

- **非结构化数据保存**

```python
with open('xxx.jpg','wb') as f:
	f.write(res.content)
```

- **示例**

保存赵丽颖图片到本地

```python

```

- **练习**

```python
1、将猫眼电影案例改写为 requests 模块实现
2、将电影天堂案例改写为 requests 模块实现
3、百度图片抓取: 输入要抓取的图片内容,抓取首页的30张图片,保存到对应的文件夹，比如:
   你想要谁的照片，请输入: 赵丽颖
   创建文件夹到指定目录: 赵丽颖  并把首页30张图片保存到此文件夹下
```

**百度图片练习代码实现**

```python

```

## Chrome浏览器安装插件

### 安装方法

```python
1、把下载的相关插件（对应操作系统浏览器）后缀改为 .zip 
2、解压,打开Chrome浏览器 -> 右上角设置 -> 更多工具 -> 扩展程序 -> 点开开发者模式
#3、把相关插件文件夹拖拽到浏览器中,释放鼠标即可安装
#3、有的插件直接拖拽 .zip 文件释放即可
```

### 需要安装插件

```python
1、Xpath Helper: 轻松获取HTML元素的xPath路径
  # 开启/关闭: Ctrl + Shift + x
2、Proxy SwitchyOmega: Chrome浏览器中的代理管理扩展程序
3、JsonView: 格式化输出json格式数据
```

## xpath解析

### 定义

```python
XPath即为XML路径语言，它是一种用来确定XML文档中某部分位置的语言，同样适用于HTML文档的检索
```

### 示例

```html
<ul class="CarList">
	<li class="bjd" id="car_001" href="http://www.bjd.com/">
        <p class="name">布加迪</p>
        <p class="model">威航</p>
        <p class="price">2500万</p>
        <p class="color">红色</p>
    </li>
    
    <li class="byd" id="car_002" href="http://www.byd.com/">
        <p class="name">比亚迪</p>
        <p class="model">秦</p>
        <p class="price">15万</p>
        <p class="color">白色</p>
    </li>
</ul>
```

### 匹配演示

```python
1、查找所有的li节点
  //li
2、获取所有汽车的名称: 所有li节点下的子节点p的值 (class属性值为name）
  //li/p[@class="name"]  
3、找比亚迪车的信息: 获取ul节点下第2个li节点的汽车信息
  //ul/li[2]                          
4、获取所有汽车的链接: ul节点下所有li子节点的href属性的值
  //ul/li/@href

# 只要涉及到条件,加 []
# 只要获取属性值,加 @
```

### 选取节点

```python
1、// ：从所有节点中查找（包括子节点和后代节点）
2、@  ：获取属性值
   # 使用场景1（属性值作为条件）
     //div[@class="movie-item-info"]
   # 使用场景2（直接获取属性值）
     //div[@class="movie-item-info"]/a/img/@src
```

### 匹配多路径（或）

```python
xpath表达式1 | xpath表达式2 | xpath表达式3
```

### 常用函数

```python
1、contains() ：匹配属性值中包含某些字符串节点
   # 查找id属性值中包含字符串 "car_" 的 li 节点
   
2、text() ：获取节点的文本内容
   # 查找所有汽车的价格
   
```

## lxml解析库

### 安装

```python
sudo pip3 install lxml
```

### 使用流程

```python
1、导模块
   from lxml import etree
2、创建解析对象
   parse_html = etree.HTML(html)
3、解析对象调用xpath
   r_list = parse_html.xpath('xpath表达式')
```

### html样本

```html
<div class="wrapper">
	<a href="/" id="channel">新浪社会</a>
	<ul id="nav">
		<li><a href="http://domestic.sina.com/" title="国内">国内</a></li>
		<li><a href="http://world.sina.com/" title="国际">国际</a></li>
		<li><a href="http://mil.sina.com/" title="军事">军事</a></li>
		<li><a href="http://photo.sina.com/" title="图片">图片</a></li>
		<li><a href="http://society.sina.com/" title="社会">社会</a></li>
		<li><a href="http://ent.sina.com/" title="娱乐">娱乐</a></li>
		<li><a href="http://tech.sina.com/" title="科技">科技</a></li>
		<li><a href="http://sports.sina.com/" title="体育">体育</a></li>
		<li><a href="http://finance.sina.com/" title="财经">财经</a></li>
		<li><a href="http://auto.sina.com/" title="汽车">汽车</a></li>
	</ul>
</div>
```

### 示例+练习

```python
from lxml import etree

html = '''
<div class="wrapper">
	<a href="/" id="channel">新浪社会</a>
	<ul id="nav">
		<li><a href="http://domestic.sina.com/" title="国内">国内</a></li>
		<li><a href="http://world.sina.com/" title="国际">国际</a></li>
		<li><a href="http://mil.sina.com/" title="军事">军事</a></li>
		<li><a href="http://photo.sina.com/" title="图片">图片</a></li>
		<li><a href="http://society.sina.com/" title="社会">社会</a></li>
		<li><a href="http://ent.sina.com/" title="娱乐">娱乐</a></li>
		<li><a href="http://tech.sina.com/" title="科技">科技</a></li>
		<li><a href="http://sports.sina.com/" title="体育">体育</a></li>
		<li><a href="http://finance.sina.com/" title="财经">财经</a></li>
		<li><a href="http://auto.sina.com/" title="汽车">汽车</a></li>
	</ul>
</div>'''
# 创建解析对象
parse_html = etree.HTML(html)
# 调用xpath返回结束,text()为文本内容
a_list = parse_html.xpath('//a/text()')
print(a_list)

# 提取所有的href的属性值

# 提取所有href的值,不包括 / 

# 获取 图片、军事、...,不包括新浪社会

```

### xpath最常使用方法

```python
1、先匹配节点对象列表
  # r_list: ['节点对象1','节点对象2']
  r_list = parse_html.xpath('基准xpath表达式')
2、遍历每个节点对象,利用节点对象继续调用 xpath
  for r in r_list:
        name = r.xpath('./xxxxxx')
        star = r.xpath('.//xxxxx')
        time = r.xpath('.//xxxxx')
```

## 链家二手房案例（xpath）

### 实现步骤

- 确定是否为静态

```python
打开二手房页面 -> 查看网页源码 -> 搜索关键字
```

- xpath表达式

```python
1、基准xpath表达式(匹配每个房源信息节点列表)
   此处滚动鼠标滑轮时,li节点的class属性值会发生变化,通过查看网页源码确定xpath表达式
  //ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]

2、依次遍历后每个房源信息xpath表达式
   * 名称: './/a[@data-el="region"]/text()'
   
   # 户型+面积+方位+是否精装
   info_list = './/div[@class="houseInfo"]/text()'  [0].strip().split('|')
   * 户型: info_list[1]
   * 面积: info_list[2]
   * 方位: info_list[3]
   * 精装: info_list[4]
   

   * 楼层: './/div[@class="positionInfo"]/text()'
   * 区域: './/div[@class="positionInfo"]/a/text()'
   * 总价: './/div[@class="totalPrice"]/span/text()'
   * 单价: './/div[@class="unitPrice"]/span/text()'
```

### 代码实现

```python

```

## 作业1 - 猫眼电影数据抓取

**实现分析**

```python
1、基准xpath: 匹配所有电影信息的节点对象列表
    
    
2、遍历对象列表，依次获取每个电影信息
   for dd in dd_list:
	   电影名称 ：
	   电影主演 ：
	   上映时间 ：
```

## 作业2 - 百度贴吧图片抓取

### 目标思路

* 目标

```python
抓取指定贴吧所有图片
```

* 思路

```python
1、获取贴吧主页URL,下一页,找到不同页的URL规律
2、获取1页中所有帖子URL地址: [帖子链接1,帖子链接2,...]
3、对每个帖子链接发请求,获取图片URL
4、向图片的URL发请求,以wb方式写入本地文件
```

### 实现步骤

- 贴吧URL规律

```python
http://tieba.baidu.com/f?kw=??&pn=50
```

- xpath表达式

```python
1、帖子链接xpath
   //div[@class="t_con cleafix"]/div/div/div/a/@href
    
2、图片链接xpath
   //div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src
    
3、视频链接xpath
   //div[@class="video_src_wrapper"]/embed/@data-video
   # 注意: 此处视频链接前端对响应内容做了处理,需要查看网页源代码来查看，复制HTML代码在线格式化
```

## 作业3 - 电影天堂（xpath）

## 作业4 - 糗事百科（xpath）

```python
1、URL地址: https://www.qiushibaike.com/text/
2、目标 ：用户昵称、段子内容、好笑数量、评论数量
```

