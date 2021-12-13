#coding=utf-8
"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积

Version: 0.1
Author: Jasn
Date: 2019-12-15

提示：
1、已知三边长度，任意两边之和大于第三边就是三角形。
2、用海伦公式求三角形面积
"""
import math

while True:
    a=float(input('>>a=：'))
    b=float(input('>>b=：'))
    c=float(input('>>c=：'))
    if a>0 and b>0 and c>0:
        break
    else:
        print("三角形边长应该大于0")
if (a+b>c) or (a+c>b) or (c+b>a):
    print("该三角形周长为：{:.2f}".format(a+b+c))
    p = (a + b + c) / 2  #半周长
    # math.sqrt()方法返回数字x的平方根。
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))  #海伦公式
    print('面积: {:.2f}' .format(area))
else:
    print('不能构成三角形')

