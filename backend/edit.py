import re, os
import xml.dom.minidom
import codecs

class Edit_Congif(object):

    def __init__(self,location,find_str='',new_str=''):
        self.location = location
        self.find_str = find_str
        self.new_str = new_str

    def Globa_Edit(self):
        '''find_str 接收参数，查找关键字更改内容'''
        data = ''
        # /Users/heyang/expert/WEB-INF/classes/jeesite.properties
        with open('%s' %self.location, 'r+', encoding='utf-8') as f:
            for line in f.readlines():
                # cas.server.url
                # print(line)
                if (line.find('%s' %self.find_str) == 0):
                    line = '%s=%s' % (self.find_str,self.new_str,) + '\n'
                data += line
        with open('%s' %self.location, 'r+', encoding='utf-8') as f:
            #time.sleep(0.01)
            f.writelines(data)

    def Re_Edit(self,re1='(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d]):{0,1}\d{0,6}'):
        '''正则查找IP:Port 如：10.1.1.1:111 更改文件'''
        with open(self.location, "r", encoding="utf-8") as f1, \
                open("%s.bak" % self.location, "w", encoding="utf-8") as f2:
            # print(f1.read())
            for line in f1:
                # print(line)
                f2.write(re.sub(r'%s' %re1,
                                self.new_str, line))
        os.remove(self.location)
        os.rename("%s.bak" % self.location, self.location)

    def Xml_Edit(self,report_url):
        '''xml 查找节点修改'''
        dom = xml.dom.minidom.parse(self.location)
        root = dom.documentElement
        int = 0
        find_obj = root.getElementsByTagName(self.find_str)

        for i in range(0, 8):
            find_obj[int].setAttribute('value', self.new_str)
            int += 14
        find_obj[131].setAttribute('value', report_url)

        f = codecs.open(self.location, 'w', 'utf-8')
        dom.writexml(f, addindent='  ', newl='\n', encoding='utf-8')
        f.close()


    def Xml_Redis(self):
        '''cas redis xml更改'''
        dom = xml.dom.minidom.parse(self.location)
        root = dom.documentElement
        find_obj = root.getElementsByTagName(self.find_str)[0]
        find_obj.setAttribute('value',  self.new_str)

        f = codecs.open(self.location, 'w', 'utf-8')
        dom.writexml(f, addindent='  ', newl='\n', encoding='utf-8')
        f.close()

    def Xml_Redis2(self):
        '''project redis xml更改'''
        dom = xml.dom.minidom.parse(self.location)
        root = dom.documentElement
        bb = root.getElementsByTagName(self.find_str)[2].getElementsByTagName(self.find_str)
        # print(bb)

        for i in range(len(bb)):
            bb[i].parentNode.removeChild(bb[i])

        f = codecs.open(self.location, 'w', 'utf-8')
        dom.writexml(f, addindent='  ', newl='\n', encoding='utf-8')
        f.close()

        fp = open(self.location, 'r', encoding='utf-8')
        lines = []
        for line in fp:  # 内置的迭代器, 效率很高
            lines.append(line.strip())
        fp.close()

        new_list = self.new_str.split(",")

        for i in range(len(new_list)):
            ip = re.search(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])',new_list[i]).group()
            port = re.search(':{1,9}\d{2,4}',new_list[i]).group().strip(':')
            new = '''
            <bean class="redis.clients.jedis.HostAndPort">  
                                <constructor-arg name="host" index="0" value="%s"></constructor-arg>  
                                <constructor-arg name="port" index="1" value="%s"></constructor-arg>  
                            </bean>  
            ''' %(ip, port)
            lines.insert(lines.index('<set>') + 1, new)

        s = '\n'.join(lines)
        fp = open(self.location, 'w', encoding='utf-8')
        fp.write(s)
        fp.close()