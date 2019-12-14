'''
Python中没有像C++中public和private这些关键字来区别公有属性和私有属性
它是以属性命名方式来区分，如果在属性名前面加了2个下划线'__'，则表明该属性是私有属性，
否则为公有属性（方法也是一样，方法名前面加了2个下划线的话表示该方法是私有的，否则为公有的）
'''

class People(object):

    def __init__(self, name):
        self.__name = name

    def __del__(self):          #析构
        print("__del__方法被调用")
        print("%s对象被干掉了..."%self.__name)

    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName

   
xiaoming = People("dongGe")
#print(xiaoming.__name)  #这里会报错,私有对象 无法直接访问

xiaoming.setName('xiaoming')
print(xiaoming.getName()) 
del xiaoming

people1 = People("people1")
people2 = people1
people3 = people1

print("---  删除people1对象")
del people1
print("---  删除people2对象")
del people2
print("---  删除people3对象")
del people3
'''
    当有1个变量保存了对象的引用时，此对象的引用计数就会加1
    当使用del删除变量指向的对象时，如果对象的引用计数不会1，比如3，那么此时只会让这个引用计数减1，即变为2，当再次调用del时，变为1，如果再调用1次del，此时会真的把对象进行删除
'''
print()
#------------单继承-------------
class Cat(object):

    def __init__(self, name, color="白色"):
        self.name = name
        self.color = color

    def run(self):
        print("%s--在跑"%self.name)


# 定义一个子类，继承Cat类如下:
class Bosi(Cat):

    def setNewName(self, newName):
        self.name = newName

    def eat(self):
        print("%s--在吃"%self.name)

cat = Bosi('波斯猫')
print('cat的名字为:%s'%cat.name)
print('cat的颜色为:%s'%cat.color)
cat.run()
cat.setNewName("短尾猫")
cat.eat()
'''
    私有的属性，不能通过对象直接访问，但是可以通过方法访问
    私有的方法，不能通过对象直接访问
    私有的属性、方法，不会被子类继承，也不能被访问
    一般情况下，私有的属性、方法都是不对外公布的，往往用来做内部的事情，起到安全的作用
'''

#多继承
class base(object):
    def __init__(self,name):
        self.name = name
        self.color = 'yellow'

    def test(self):
        print('----base test----')
# 定义一个父类
class A(base):
    def __init__(self,name):
        super().__init__(name)

    def test(self):
        print('---- A test----')

    def printA(self):
        print('----A----')

# 定义一个父类
class B(base):
    def test(self):
        print('---- B test----')

    def printB(self):
        print('----B----')

# 定义一个子类，继承自A、B
class C(A,B):
    def printC(self):
        print('----C----')

obj_C = C('xiaoming')
obj_C.printA()
obj_C.printB()
obj_C.printC()
obj_C.test()        #调用A的test
print(C.__mro__) #可以查看C类的对象搜索方法时的先后顺序

obj_A = A('xiaoming')
print(obj_A.name)
print(obj_A.color)