from mitmproxy import ctx
#必须这么写
def request(flow):
    # print(flow.request.headers)
    ctx.log.info(str(flow.request.headers))
    ctx.log.warn(str(flow.request.headers))
    ctx.log.error(str(flow.request.headers))



#http.HTTPFlow 实例 flow
#flow.request.headers #获取所有头信息，包含Host、User-Agent、Content-type等字段
#flow.request.url #完整的请求地址，包含域名及请求参数，但是不包含放在body里面的请求参数
#flow.request.pretty_url #同flow.request.url目前没看出什么差别
#flow.request.host #域名
#flow.request.method #请求方式。POST、GET等
#flow.request.scheme #什么请求 ，如https
#flow.request.path # 请求的路径，url除域名之外的内容
#flow.request.get_text() #请求中body内容，有一些http会把请求参数放在body里面，那么可通过此方法获取，返回字典类型
#flow.request.query #返回MultiDictView类型的数据，url直接带的键值参数
#flow.request.get_content()#bytes,结果如flow.request.get_text()
#flow.request.raw_content #bytes,结果如flow.request.get_content()
#flow.request.urlencoded_form #MultiDictView，content-type：application/x-www-form-urlencoded时的请求参数，不包含url直接带的键值参数
#flow.request.multipart_form #MultiDictView，content-type：multipart/form-data

#以上均为获取request信息的一些常用方法，对于response，同理
#flow.response.status_code #状态码
#flow.response.text#返回内容，已解码
#flow.response.content #返回内容，二进制
#flow.response.setText()#修改返回内容，不需要转码
#以上为不完全列举