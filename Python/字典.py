#字典类型
info = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}
#键值查找 不存在会报错
print(info['name'])
print(info['address'])

# get 查找 不存在返回 None ,或者 设置默认值
test = info.get('age')
test = info.get('age',"不存在")
print(test)

#------------字典的常见操作
#添加元素
info['age'] = 20
print(info['age'])
info['age'] = 18 #修改
print(info['age'])

del info['age']  #删除 某个键值对

print('清空前,%s'%info)
info.clear()     #清空
print('清空后,%s'%info)
del info         #删除整个字典

dict = {'name':'班长', 'id':100, 'sex':'f', 'address':'地球亚洲中国北京'}

print(len(dict)) #键值对的个数

print(dict.keys()) #返回所有 key

print(dict.values()) #返回所有 value


print(dict.items()) #返回一组键值

#has_key 如果key在字典中，返回True，否则返回False
#Python 3.X 里不包含 has_key() 函数，被 __contains__(key) 替代:
print(dict.__contains__('name')) 
print(dict.__contains__('hhh')) 

#字典遍历
##遍历 键
for i in dict.keys():
    print (i,end = " ")

print()

#遍历 值
for i in dict.values():
    print (i,end = " ")

#遍历 键值对
print()
for i in dict.items():
    print (i,end = " ")

print()
print()
for key,value in dict.items():
    print ("key = {},value = {}".format(key,value))

#带下标的遍历
chars = ['a','b','c','d']
i=0
for chr in chars:
    print(i,chr)
    i+=1
print('enumerate')
#enumerate
for i,chr in enumerate(chars):
    print(i,chr)
