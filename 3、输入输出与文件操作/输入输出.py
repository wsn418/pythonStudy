import argparse
from datetime import datetime

# 命令行参数 argument
# 创建解析器
parser = argparse.ArgumentParser(description="处理命令行参数的示例")

# 添加参数
# nargs='*' 允许用户在命令行中提供任意数量的参数，包括零个参数
# type=int 强制转换参数为整数
# default=10 指定参数的默认值
# action='store_true' 用于存储布尔值的参数
parser.add_argument('number', nargs='*', help="命令行参数", type=int, default=10)

# 解析参数
args = parser.parse_args()

print(f"你输入的是{args.number}")
#如何使用
# python 输入输出.py args 100

# 编写一个程序，当用户输入 q 或 quit 时，程序退出，否则一直等待用户输入。
# while True:
#     user_input = input("请输入命令: ")
#     if user_input.lower() in ['q', 'quit']:
#         print("程序已退出")
#         break
#     else:
#         print(f"你输入的是: {user_input}")


#格式化输出 格式化字符串
# 格式化输出 格式化字符串

# 使用百分号 % 进行格式化
name = "Alice"
age = 30
print("姓名: %s, 年龄: %d" % (name, age))

# 使用 str.format() 方法进行格式化
print("姓名: {}, 年龄: {}".format(name, age))
print("姓名: {0}, 年龄: {1}".format(name, age))
print("姓名: {name}, 年龄: {age}".format(name=name, age=age))

# 使用 f-string (Python 3.6+)
print(f"姓名: {name}, 年龄: {age}")

# 格式化数字
number = 123.456
print("保留两位小数: {:.2f}".format(number))
print(f"保留两位小数: {number:.2f}")

# 格式化为百分比
percentage = 0.1234
print("百分比: {:.2%}".format(percentage))
print(f"百分比: {percentage:.2%}")

# 填充和对齐
text = "Hello"
print("居中填充: {:^10}".format(text))
print(f"居中填充: {text:^10}")
print("左对齐填充: {:<10}".format(text))
print(f"左对齐填充: {text:<10}")
print("右对齐填充: {:>10}".format(text))
print(f"右对齐填充: {text:>10}")


# 在程序中有字符串变量如下： 
# date="2022-05-20 13:14:00" 
# 请使⽤格式化输出功能，将上述字符串进⾏格式转换，输出格式为： 
# 智能助⼿为你报时，当前时间是 2022 年 5 ⽉ 20 ⽇ 13 点 14 分 0 秒
date = "2022-05-20 13:14:00"
year, month, day, hour, minute, second = date.replace("-", " ").replace(":", " ").split()
formatted_date = f"智能助手为你报时，当前时间是 {year} 年 {month} 月 {day} 日 {hour} 点 {minute} 分 {second} 秒"
print(formatted_date)

# F-strings：如何通过定义好的格式进行输出？
# F-strings 是 Python 3.6 引入的一种新的字符串格式化方法，它使用大括号 {} 来包含表达式，并在字符串前加上字母 f 或 F。
# F-strings 的优点是简洁、易读，并且支持任意的表达式。

# 基本用法
name = "Bob"
age = 25
print(f"姓名: {name}, 年龄: {age}")

# 表达式
print(f"明年年龄: {age + 1}")

# 调用函数
def greet(name):
    return f"Hello, {name}!"

print(f"问候: {greet(name)}")

# 使用字典
person = {"name": "Charlie", "age": 35}
print(f"姓名: {person['name']}, 年龄: {person['age']}")

# 格式化数字
# f"{对象:宽度.精度类型}" 宽度就是输出字符的长度，精度是小数点后的位数
number = 123.456
print(f"保留两位小数: {number:2.2f}")

# 格式化为百分比
percentage = 0.1234
print(f"百分比: {percentage:.2%}")

# 填充和对齐
text = "Hello"
print(f"居中填充: {text:^10}")
print(f"左对齐填充: {text:<10}")
print(f"右对齐填充: {text:>10}")

# 日期和时间
now = datetime.now()
print(f"当前时间: {now:%Y-%m-%d %H:%M:%S}")

# 多行字符串
name = "David"
age = 40
address = "123 Main St"
info = (
    f"姓名: {name}\n"
    f"年龄: {age}\n"
    f"地址: {address}"
)
print(info)

# 有⼀组由程序处理的浮点数，为了输出时保持⼯整，希望输出的字⾯值为 10 个数字，
# 且⼩数点后最多包含 3 位，请你⽤ F-strings 对它们的格式进⾏调整并输出。 
# 例：  
# 数字为：123.4567 
# 输出为：'000123.457
num = 123.4567
print(f"{num:0>10.3f}")  # 使用 0 填充
print(f"{num:*^10.3f}")  # 使用 * 填充并居中对齐
print(f"{num:#<10.3f}")  # 使用 # 填充并左对齐