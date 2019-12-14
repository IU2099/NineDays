'''
  def 函数名():
        代码
'''

def printInfo():
        print ('------------------------------------')
        print ('         人生苦短，我用Python'        )
        print ('------------------------------------')

# 打印一条横线
def printOneLine():
    print("-"*50) 

#有参
def sum1(a,b):
    print(a+b)

#具有返回值
def sum2(a,b): 
    return a+b
#多个返回值,本质是元组
def divid(a,b=10): #缺省参数,默认值
    num1 = a + b
    num2 = a % b
    num3 = a // b
    return num1,num2,num3       #num 局部变量

#不定长参数 加了星号（*）的变量args会存放所有未命名的变量参数，args为元组；而加**的变量kwargs会存放命名参数，即形如key=value的参数， kwargs为字典。
def functionname(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


#-------------------------调用
printInfo()
sum1(1,2)

printOneLine()

c = sum2(2,2)
print(c)

printOneLine()

num1,num2,num3 = divid(8) #全局变量
print("num1 = {},num2 = {},num3 = {}".format(num1,num2,num3))

functionname(1,2,3,4,5,m=6,n=7,i=8,j=9)

printOneLine()
printOneLine()

#----------引用传参
def selfAdd(num):
    print(id(num))  #打印 地址
    num+=num         
    print(id(num))  
    num = num + num
    print(id(num))

a_int = 100 #定义一个全局变量
print(a_int)
print("a-int : %d" %id(a_int))
selfAdd(a_int)
print("a-int : %d" %id(a_int))
print(a_int)  #  a 的 值 未发生变化,

printOneLine()

a_list =  [1,2]
print(a_list)
selfAdd(a_list)
print(a_list) #a 的值 发生变化 

# Python中函数参数是引用传递（注意不是值传递）。
# 对于不可变类型，因变量不能修改，所以运算不会影响到变量自身；
# 而对于可变类型来说，函数体中的运算有可能会更改传入的参数变量。
'''
可变类型，值可以改变：
    列表 list
    字典 dict
不可变类型，值不可以改变：
    数值类型 int, long, bool, float
    字符串 str
    元组 tuple
'''
printOneLine()
printOneLine()
printOneLine()
#匿名函数 
#   Lambda 函数能接收任何数量的参数但只能返回一个表达式的值
#   匿名函数 不能直接调用print，因为lambda需要一个表达式

sum = lambda arg1, arg2: arg1 + arg2

#调用sum函数
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))

printOneLine()
#匿名函数  作为参数传递
def fun(a, b, opt):
    print ("a =", a)
    print ("b =", b)
    print ("result =", opt(a, b))

fun(1, 2, lambda x,y:x+y)

stus = [
    {"name":"z", "age":18}, 
    {"name":"s", "age":19}, 
    {"name":"a", "age":17}
]
#按name排序：
stus.sort(key = lambda x:x['name'])
print("按name排序:\n",stus)

#按age排序：
stus.sort(key = lambda x:x['age'])
print("按age排序：\n",stus)