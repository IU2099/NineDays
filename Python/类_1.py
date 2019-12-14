#定义类
class Car:  

    def __init__(self,_WheelNum=4, _Color='黄色'):  #类似C++ 构造函数   self 当做 C++ 中类里面的 this
        self.wheelNum = _WheelNum
        self.color = _Color
 #在python中方法名如果是__xxxx__()的，那么就有特殊的功能，叫做“魔法”方法
 #当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
    def __str__(self):  
        msg = "嘿。。。我的颜色是" + self.color + "我有" + (str)(self.wheelNum )+ "个轮胎..."
        return msg
    # 定义方法
    def getCarInfo(self):
        print('车轮子个数:%d, 颜色:%s'%(self.wheelNum, self.color))

    def move(self):
        print("车正在移动...")


BMW = Car() #创建对象
BMW.color = '黑色'    #给对象添加属性
BMW.wheelNum = 4    
BMW.move()
BMW.getCarInfo()

BC = Car(8,"红色")
BC.move()
BC.getCarInfo()
print(BC)

