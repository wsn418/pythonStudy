#计算两个数的四则运算
#输入两个数和运算符，输出结果
try:
    x = float(input("请输入A: "))
    y = float(input('请输入B: '))
    z = input("请输入运算符: ")

    if z == '/' and y == 0:
        print("错误: 除数不能为0")
    else:
        result = eval(f"{x} {z} {y}")
        print("结果是", result)
except ValueError:
    print("错误: 请输入有效的数字")
except SyntaxError:
    print("错误: 请输入有效的运算符")
except Exception as e:
    print(f"发生错误: {e}")