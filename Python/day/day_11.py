#读写文本文件


""" def main():
    f=None
    try:
        f = open('..res/test01.txt','r',encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


if __name__ == "__main__":
   main();  """

#在Python中，我们可以将那些在运行时可能会出现状况的代码放在try代码块中，在try代码块的后面可以跟上一个或多个except来捕获可能出现的异常状况。例如在上面读取文件的过程中，文件找不到会引发FileNotFoundError，指定了未知的编码会引发LookupError，而如果读取文件时无法按指定方式解码会引发UnicodeDecodeError，我们在try后面跟上了三个except分别处理这三种不同的异常状况。最后我们使用finally代码块来关闭打开的文件，释放掉程序中获取的外部资源，由于finally块的代码不论程序正常还是异常都会执行到（甚至是调用了sys模块的exit函数退出Python环境，finally块都会被执行，因为exit函数实质上是引发了SystemExit异常），因此我们通常把finally块称为“总是执行代码块”，它最适合用来做释放外部资源的操作。如果不愿意在finally代码块中关闭文件对象释放资源，也可以使用上下文语法，通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源，代码如下所示。

""" import time

def main():
    try:
        with open(r'python\res\test01.txt', 'r', encoding='utf-8') as f:
            #一次性读取整个文件内容
            # print(f.read())  
            # 通过for-in循环逐行读取
            # for line in f:
            #     print(line, end='')
            #     time.sleep(0.1)
            # 读取文件按行读取到列表中
            lines = f.readlines()    
            print(lines)
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


if __name__ == '__main__':
    main() """

#写入文件
""" 
使用open函数时指定好文件名并将文件模式设置为'w'即可。注意如果需要对文件内容进行追加式写入，应该将模式设置为'a' 
"""
""" from math import sqrt


def is_prime(n):
    #判断素数的函数
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main():
    path = 'python\\res\\'
    filenames = (path+'a.txt', path+'b.txt', path+'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成!')

if __name__ == '__main__':
    main() """

# 读写二进制文件

# def main():
#     path = 'python\\res\\'
#     try:
#         with open(path+'BG.PNG', 'rb') as fs1:
#             data = fs1.read()
#             print(type(data))  # <class 'bytes'>
#         with open(path+'copy.jpg', 'wb') as fs2:
#             fs2.write(data)
#     except FileNotFoundError as e:
#         print('指定的文件无法打开.')
#     except IOError as e:
#         print('读写文件时出现错误.')
#     print('程序执行结束.')


# if __name__ == '__main__':
#     main()

# import requests
# import json

# def main():
#     resp = requests.get('http://api.tianapi.com/txapi/ensentence/index?key=80b2e236a0a8e18786e8393a3a39981c')
#     data_model = json.loads(resp.text)
#     if data_model['code'] == 200:
#         for news in data_model['newslist']:
#             print(news['en'])
#             print(news['zh'])
#     else:
#         print(data_model['msg'])


# if __name__ == '__main__':
#     main()

# -*- coding: UTF-8 -*-
import json

def main():
    mydict = {
        'name': 'IU',
        'age': 38,
        'qq': 957658,
        'friends': ["李知恩", '林允儿'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('python\\res\\data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict,fs,ensure_ascii=False)
    except IOError as e:
        print(e)
        return
    print('保存数据完成!')


if __name__ == '__main__':
    main()