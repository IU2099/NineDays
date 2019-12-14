

''' 输入输出
#input 默认是 string
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
print('num1 + num2 = {}' .format(num1 + num2))
'''

'''猜拳游戏
import random

player = input('请输入:剪刀(0) 石头(1) 布(2) :\n')
player = int (player)

computer = random.randint(0,2)

if ((player == 0 and computer == 2) 
    or (player == 1 and computer == 0)
    or (player == 2 and computer == 1)):
    print('胜')
elif player == computer:
    print('平')
else:
    print('输')


i = 1
sum = 0
while i < 100:
    sum = sum  + i
    i+=1
 
print("1~100 和 : {}" .format(sum))

'''
"""while for循环
for 临时变量 in 列表或者字符串等:
    循环满足条件时执行的代码
name = 'Hello, World!'

for x in name:
    print(x)
#-------------------
num = int(input())
i = 1
while i <= num :
    j = 1
    while j <= i:
        print("*",end='') # end  不换行,打印'' 
        j+=1
    print('\n')
    i+=1
while i > 1 :
    j = i - 2
    while j > 0:
        print("*",end='') # end  不换行,打印'' 
        j -= 1
    print('\n')
    i-=1
"""

'''创建文件夹
import os

def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  #makedirs 创建文件时如果路径不存在会创建这个路径
        print("该文件夹创建成功")
    else:
        print("该文件夹存在")

file = "./Resources"
mkdir(file)
'''

