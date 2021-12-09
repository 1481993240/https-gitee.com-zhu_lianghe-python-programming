year = input('输入年份：')
while not year.isdigit():
    year = input('输入错误，重新输入：')

year = int(year)
if year/400 == int(year/400):
    print('是')
else:
    if year/4 == int(year/4) and year/100 != int(year/100):
        print('是')
    else:
        print('不是')
