from xml.dom.minidom import parse

#minidom解析器打开xml文档并将其解析为内存中的一棵树

# book.xml中的数据由知网题录导出为NoteFirst格式的方式导出
# 亦可将所有数据写入到数据库后再进行分析

DOMTree=parse(r'book.xml')
#获取xml文档对象，就是拿到树的根
biblist=DOMTree.documentElement

keywords = biblist.getElementsByTagName('Keyword')
titles = biblist.getElementsByTagName('Title')


print('共有 %d 个标题节点' % len(titles))
print('共有 %d 个keyword节点' % len(keywords))
englist = []
chineselist = []
# 取出所有的英文关键词列表，同样可以取出所有的中文关键词列表
for keyword in keywords:
    if keyword.hasAttribute('Lang'):
        if keyword.getAttribute('Lang') == 'en':
            if len(keyword.childNodes) > 0:
                englist.append(keyword.childNodes[0].data)
                #print(keyword.childNodes[0].data)
print(englist)
for keyword in keywords:
    if keyword.hasAttribute('Lang'):
        if keyword.getAttribute('Lang') == 'zh-CHS':
            if len(keyword.childNodes) > 0:
                chineselist.append(keyword.childNodes[0].data)
print(chineselist)
