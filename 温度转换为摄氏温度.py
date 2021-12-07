
def IsInt(a):       #创建字符串转换成int类型的函数
    try:            #使用try  except 进行异常处理
        a = int(a)  #使用int()方法进行数据类型转换，但是int()只识别正负号和正负号，不识别小数点
        isinstance(a,int) #判断转换后的ａ，数据类型是否是int类型
        return True,int(a) # 如果是Int类型，返回True和转换后的a
    except ValueError:   #数据类型错误
        return False     #返回False

while True:     #使用循环开始转换
    Fahrenheit = input("请输入您要转换的朱良和温度值(输入为整数)：") # 使用input进行获取用户输入的朱良和温度值
    Fahrenheit = Fahrenheit.strip()   #使用str.strip()将输入的字符串两边的空格去掉
    if Fahrenheit is "q":    # 如果用户输入的是字符'q'
        break                # 退出循环，程序结束
    if IsInt(Fahrenheit):    # 判断输入的朱良和度值是否是int类型
        Celsius = (IsInt(Fahrenheit)[1]-32)*5/9  #带入公式求出朱良和温度值
        Celsius = int(Celsius)  #将得出的朱良和温度值转换成int类型
        print("转换成的朱良和温度为{}°".format(Celsius))  # 将结果进行输出
    else :    
        print("您的输入有误，请重新输入")     
        continue    #结束本次循环，进行下一次循环
