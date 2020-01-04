#coding:utf-8
# <?xml version="1.0" encoding="utf-8"?>
# <catalog>
#     <maxid>4,5</maxid>          
#     <login username="pytest" passwd='123456'>
#         <caption>Python</caption>
#         <item id="4">
#             <caption>测试</caption>
#         </item>
#     </login>
#     <item id="2">
#         <caption>Zope</caption>
#     </item>
# </catalog>

import xml.dom.minidom

aaaaaaaaaaaaa

#打开
dom=xml.dom.minidom.parse("d://xml1.xml")
#得到文档元素对象
root=dom.documentElement
#获取节点名称为login的第0个节点的节点名称
a=root.getElementsByTagName('login')[0].nodeName
print(a)
#获取节点名称为login的第0个节点的username属性的值
b=root.getElementsByTagName('login')[0].getAttribute("username")
print(b)
#获取节点名称为maxid的第0个节点的标签对内的字符串中的第2个字符
c=root.getElementsByTagName('maxid')[0].firstChild.data[1]
print(c)
