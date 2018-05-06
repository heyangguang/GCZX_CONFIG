# import re, os
# def alter(file, new_str):
#     with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
#         for line in f1:
#             f2.write(re.sub(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d]):{0,1}\d{0,6}',
#                             new_str, line))
#     os.remove(file)
#     os.rename("%s.bak" % file, file)

# -*- coding:utf-8 -*-

# xml
# import xml.dom.minidom
# import codecs
#
# dom = xml.dom.minidom.parse('test.xml')
#
# root = dom.documentElement
# int = 0
# bb = root.getElementsByTagName('property')
#
# for i in range(0, 8):
#     bb[int].setAttribute('value',"bb")
#     int += 14
# bb[131].setAttribute('value', 'bb')
#
# f = codecs.open('test.xml','w','utf-8')
# dom.writexml(f,addindent='  ',newl='\n',encoding = 'utf-8')
# f.close()

# lxml jsp
# from lxml import etree
#
# html = etree.HTML("casLoginView.jsp")
# html_data = html.xpath('//td/a[@href="http://10.2.146.100:8010/uams/servlet/registerUserServlet"]')
# print(html_data)
# for i in html_data:
#     print(i.text)
# html_data = html.xpath('//*')
# print(html_data)
# for i in html_data:
#     print(i.text)

# try:
#     import xml.etree.cElementTree as ET
# except ImportError:
#     import xml.etree.ElementTree as ET
#
# tree = ET.parse('casLoginView.jsp')
# print(tree)
# root = tree.getroot()

# def string_switch(x, y, z, s=1):
#     with open(x, "r", encoding="utf-8") as f:
#         # readlines以列表的形式将文件读出
#         lines = f.readlines()
#
#     with open(x, "w", encoding="utf-8") as f_w:
#         # 定义一个数字，用来记录在读取文件时在列表中的位置
#         n = 0
#         # 默认选项，只替换第一次匹配到的行中的字符串
#         if s == 1:
#             for line in lines:
#                 if y in line:
#                     line = line.replace(y, z)
#                     f_w.write(line)
#                     n += 1
#                     break
#                 f_w.write(line)
#                 n += 1
#             # 将剩余的文本内容继续输出
#             for i in range(n, len(lines)):
#                 f_w.write(lines[i])
#         # 全局匹配替换
#         elif s == 'g':
#             for line in lines:
#                 if y in line:
#                     line = line.replace(y, z)
#                 f_w.write(line)
# acb = '''<a href="http://10.2.146.100:822222222/uams/servlet/registerUserServlet">&nbsp;&nbsp;注册用户&nbsp;</a></td>'''
# # string_switch("casLoginView.jsp","注册用户",acb,"g")
#
# import os
# import re
#
# f_path = r'casLoginView.jsp'
# f = open(f_path, "r+")
# open('casLoginView1.jsp', 'w').write(re.sub(r'注册用户', acb, f.read()))

# import re
# import os
#
#
# with open('casLoginView.jsp', "r", encoding="utf-8") as f1, \
#         open('casLoginView.jsp.bak', "w", encoding="utf-8") as f2:
#     for line in f1:
#         f2.write(re.sub(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d]):{0,1}\d{0,6}(?!/acbplat)',
#                         'eee', line))
# os.remove('casLoginView.jsp')
# os.rename('casLoginView.jsp.bak', 'casLoginView.jsp')


# class test(object):
#
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#         if self.a == self.b:
#             print(a+b)
#         else:
#             print("error")
#
#
# if __name__ == '__main__':
#     test(1,1)


# if __name__ == '__main__':
    # alter("/Users/heyang/expert/WEB-INF/classes/raqreport.properties", "10.2.146.100:1113")


# import xml.etree.ElementTree as ET
# import sys
#
# tree = ET.parse("/Users/heyang/test_config/cas/WEB-INF/spring-configuration/ticketRegistry.xml")
#
# root = tree.getroot()
# print (root.tag, "---", root.attrib )
# for child in root:
#     print (child.tag, "---", child.attrib)
#
#
# print(root[2])
# # print ("*"*10 )
# # print (root[0].tag, root[0].text )
# # print ("*"*10 )

# from xml.dom.minidom import parse
# import xml.dom.minidom
#
#
# DOMTree = xml.dom.minidom.parse("/Users/heyang/test_config/cas/WEB-INF/spring-configuration/ticketRegistry.xml")
# collection = DOMTree.documentElement
# if collection.hasAttribute("name"):
#    print ("Root element : %s" % collection.getAttribute("name"))

# import codecs
# import xml.etree.ElementTree as ET
# tree = ET.parse('/Users/heyang/test_config/cas/WEB-INF/spring-configuration/ticketRegistry.xml')
# root = tree.getroot()
#
# root[1][0].set('value', '1')
#
# f = codecs.open('/Users/heyang/test_config/cas/WEB-INF/spring-configuration/ticketRegistry2.xml', 'w', 'utf-8')
# tree.writexml(f, addindent='  ', newl='\n', encoding='utf-8')
# f.close()

# import xml.dom.minidom
# import codecs
#
# dom = xml.dom.minidom.parse('/Users/heyang/test_config/acb/WEB-INF/classes/spring-context-jedis.xml')
# root = dom.documentElement
# bb = root.getElementsByTagName('bean')[2].getElementsByTagName('bean')
# print(bb)
#
# for i in range(len(bb)):
#     bb[i].parentNode.removeChild(bb[i])
#
# f = codecs.open('/Users/heyang/test_config/acb/WEB-INF/classes/spring-context-jedis3.xml', 'w', 'utf-8')
# dom.writexml(f, addindent='  ', newl='\n', encoding='utf-8')
# f.close()
#
# fp = open('/Users/heyang/test_config/acb/WEB-INF/classes/spring-context-jedis3.xml','r')
# lines = []
# for line in fp:  # 内置的迭代器, 效率很高
#     lines.append(line.strip())
# fp.close()
# new = '''
# <bean class="redis.clients.jedis.HostAndPort">
#                     <constructor-arg name="host" index="0" value="10.2.146.192"></constructor-arg>
#                     <constructor-arg name="port" index="1" value="6379"></constructor-arg>
#                 </bean>
# '''
# lines.insert(lines.index('<set>')+1, new)
# s = '\n'.join(lines)
# fp = open('data.txt', 'a')
# fp.write(s)
# fp.close()

# print(lines)
# lines.insert(3,"666\n")           #第四行插入666并回车
# s=''.join(lines)
# f=open("d:\\1script\\1.txt",'w+') #重新写入文件
# f.write(s)
# f.close()
# del lines[:]                      #清空列表
# print lines

# print(bb.getElementsByTagName('constructor-arg')[1].getAttribute('value'))
# bb1 = bb[0].getElementsByTagName('constructor-arg')
# print(bb1[1].getAttribute('value'))

# bb.setAttribute('value', '192.168.45:2')
# f = codecs.open('/Users/heyang/test_config/cas/WEB-INF/spring-configuration/ticketRegistry2.xml', 'w', 'utf-8')
# dom.writexml(f, addindent='  ', newl='\n', encoding='utf-8')
# f.close()