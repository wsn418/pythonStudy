# 判断.py
# 这个文件包含了关于 Python 中条件判断的详细介绍和示例代码。
# 在编程中，条件判断是一个非常重要的概念。它允许程序根据不同的条件执行不同的代码块。Python 提供了几种条件判断语句，包括 if 语句、if-else 语句和 if-elif-else 语句。
# 1. if 语句:
# if 语句用于在条件为真的情况下执行代码块。
# 示例:
# if condition:
#     # 执行代码块
# 2. if-else 语句:
# if-else 语句用于在条件为真时执行一个代码块，在条件为假时执行另一个代码块。

# 示例:
# if condition:
#     # 条件为真时执行的代码块
# else:
#     # 条件为假时执行的代码块

# 3. if-elif-else 语句:
# if-elif-else 语句用于在多个条件之间进行选择。

# 示例:
# if condition1:
#     # 条件1为真时执行的代码块
# elif condition2:
#     # 条件2为真时执行的代码块
# else:
#     # 以上条件都不为真时执行的代码块

# 以下是一些具体的示例代码:
# """

# 示例 1: 简单的 if 语句
x = 10
if x > 5:
    print("x 大于 5")

# 示例 2: if-else 语句
y = 3
if y > 5:
    print("y 大于 5")
else:
    print("y 小于或等于 5")

# 示例 3: if-elif-else 语句
z = 7
if z > 10:
    print("z 大于 10")
elif z > 5:
    print("z 大于 5 但小于或等于 10")
else:
    print("z 小于或等于 5")
# 示例 4: 同时判断两个条件
a = 4
b = 6
if a > 2 and b < 10:
    print("a 大于 2 且 b 小于 10")
elif a > 2 and b >= 10:
    print("a 大于 2 且 b 大于或等于 10")
else:
    print("a 小于或等于 2 或 b 大于或等于 10")

# 4. match 语句 (Python 3.10 及以上版本):
# match 语句用于在多个模式之间进行选择。它类似于其他编程语言中的 switch 语句。

# 示例:
value = 2
match value:
    case 1:
        print("值为 1")
    case 2:
        print("值为 2")
    case 3:
        print("值为 3")
    case _:
        print("值不在 1, 2, 3 之中")

# 示例 5 match 语句中的模式组合
status_code = 404
match status_code:
    case 200 | 201:
        print("成功")
    case 400:
        print("错误请求")
    case 401 | 403:
        print("未授权或禁止访问")
    case 404:
        print("未找到")
    case _:
        print("其他错误")