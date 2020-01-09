# -*- coding: utf-8 -*-
import lxml
from xml.dom.minidom import Document


def main(char):
    temp = str(char)
    for i in temp:
        if '<' == i:
            char = char.replace('<', '&lt;')
        if '>' == i:
            char = char.replace('>', '&gt;')
        if '&' == i:
            char = char.replace('&', '&amp;')
        if '\"' == i:
            char = char.replace('\"', '&quot;')
        if '\'' == i:
            char = char.replace('\'', '&apos;')
        if '×' == i:
            char = char.replace('×', '&times;')
        if '÷' == i:
            char = char.replace('÷', '&divde;')
    return char


def writeInfoToXml(_str):
        # 创建dom文档
    doc = Document()
    # 创建根节点
    root = doc.createElement('root')
    # 根节点插入dom树
    doc.appendChild(root)
    # 先创建节点<text>，然后插入到父节点<root>下
    text = doc.createElement('text')
    text.appendChild(doc.createTextNode(str(_str)))
    root.appendChild(text)
    try:
        with open('python\\res\\data.xml', 'w') as f:
            doc.writexml(f, indent='\t', newl='\n',
                         addindent='\t', encoding='utf-8')
            f.close()
    except IOError as e:
        print(e)
        return
    print('保存数据完成!')


if __name__ == '__main__':
    temp = main('\"Do\'t worry about it\"')
    print(temp)
    writeInfoToXml(temp)
