#### 练习1：英制单位英寸与公制单位厘米互换。

value = float(input('请输入长度: '))
unit = input('请输入单位(cm,in): ')
if unit == 'in' or unit == '英寸':
    print('%.3f英寸 = %.3f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%.3f厘米 = %.3f英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位')



#### 练习2：百分制成绩转换为等级制成绩
'''
    > **要求**：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
 '''
score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)

#### 练习3：输入三条边长，如果能构成三角形就计算周长和面积。

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积: %f' % (area))
else:
    print('不能构成三角形')