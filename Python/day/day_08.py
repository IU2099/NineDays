# Pythob Object 
# 注：私有属性 __  两个下划线开头

class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    
    def study(self,course_name):
        print('%s正在学习%s'%(self.name,course_name))
    def watch_movie(self):
        if self.__age < 18:
            print(f'{self.name}正在看喜羊羊与灰太狼。')
        else:
            print(f'{self.name}正在看岛国电影。')

    def getage(self):
        self.__test()
        return self.__age
    def __test(self):
        print(f'test:{self.__age}')


# 但是，Python并没有从语法上严格保证私有属性或方法的私密性，仍旧能够通过规则访问 
def main_student():
    stu1 = Student('Yuner',17)
    stu2 = Student('IU',28)
    stu1.study('Python 程序设计')
    stu1.watch_movie()
    stu2.study('三字经')
    stu2.watch_movie()

    print(stu1.name)
    print(stu1.getage())

    print(stu2._Student__age)
    stu2._Student__test()

# 实际开发中，我们并不建议将属性设置为私有的，因为这会导致子类无法访问。所以大多数Python程序员会遵循一种命名惯例就是让属性名以单下划线开头来表示属性是受保护的，本类之外的代码在访问这样的属性时应该要保持慎重。
import time

class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main_clock():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        time.sleep(1)
        clock.run()

from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        """初始化方法
        
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """移动到指定位置
        
        :param x: 新的横坐标
        "param y: 新的纵坐标
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """移动指定的增量
        
        :param dx: 横坐标的增量
        "param dy: 纵坐标的增量
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """计算与另一个点的距离
        
        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def main_Point():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))

if __name__ == '__main__':
    main_Point()
