# >=90    A 绩点为4
# 80-89   B 绩点为3
# 70-79   C 绩点为2
# 60-69   D 绩点为1
# <=59    E 绩点为0
a=float(input('输入该学生的成绩：'))
if a>=90:
    print('等级为A 绩点为4')
elif a>=80:
    print('等级为B 绩点为3')
elif a>=70:
    print('等级为C 绩点为2')
elif a>=60:
    print('等级为D 绩点为1')
else:
    print('等级为E 绩点为0')