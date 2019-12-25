###  练习1：华氏温度转换为摄氏温度。
###  > 提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

#### 练习2：输入圆的半径计算计算周长和面积。

import math

radius = float(input('请输入圆的半径：'))
perimeter =  2 * math.pi * radius
area = math.pi * math.pow(radius,2)

print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)


#### 练习3：输入年份判断是不是闰年。
year = int(input('请输入年份: '))
is_leap = (year % 4 == 0 and year % 100 != 0) or \
           year % 400 == 0
print(is_leap)