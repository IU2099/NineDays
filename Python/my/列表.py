#列表  列表中的元素可以是不同类型的

testList = [1, 'a' , 2]
#print(testList[0])
#print(testList[1])
#print(testList[2])

print(len(testList))

for i in testList:
    print(i,end = " ")

print()
testList.append(9) #增

for i in testList:
    print(i,end = " ")

print()

addList = [4,5,4]

testList.extend(addList) #extend可以将另一个集合中的元素逐一添加到列表中

for i in testList:
    print(i,end = " ")

#insert(index, object) 在指定位置index前插入元素object

print()
testList[1] = '修改'
for i in testList:
    print(i,end = " ")

#查找元素("查"in, not in, index, count)
print()
findName = 5

if findName  in testList:
        print('找到了')
else:
        print('没有找到')

print(testList.index(9))
print(testList.count(4))

#删除元素("删"del, pop, remove)

#del：根据下标进行删除
#pop：删除最后一个元素
#remove：根据元素的值进行删除

#排序(sort, reverse)

a = [9,2,1,5,7,6,8,4]
a.reverse(); #倒序
print(a)
a.sort() #list按特定顺序重新排列 默认为由小到大 参数reverse=True可改为倒序，由大到小。
print(a)
a.sort(reverse=True)
print(a)


#多维链表
schoolNames = [['北京大学','清华大学'],
               ['南开大学','天津大学','天津师范大学'],
               ['山东大学','中国海洋大学']]

import random

# 定义一个列表用来保存3个办公室
offices = [[],[],[]]

# 定义一个列表用来存储8位老师的名字
names = ['A','B','C','D','E','F','G','H']

i = 0
for name in names:
    index = random.randint(0,2)    
    offices[index].append(name)

i = 1
for tempNames in offices:
    print('办公室%d的人数为:%d'%(i,len(tempNames)))
    i+=1
    for name in tempNames:
        print("%s"%name,end='')
    print("\n")
    print("-"*20)