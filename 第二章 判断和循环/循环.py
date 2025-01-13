# python 中的循环

# while 循环
count = 0
while count < 5:
    print("这是第", count + 1, "次循环")
    count += 1

#完善while循环 并且使用continue和break
#continue 语句用于跳过当前循环中的剩余代码，然后继续进行下一次循环。
#break 语句用于退出循环，即使循环条件没有变为 False。
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print("这是第", count, "次循环")
    if count == 4:
        break

# for 循环
for i in range(5):
    print("这是第", i + 1, "次循环")

# 遍历列表
fruits = ["苹果", "香蕉", "橘子"]
for fruit in fruits:
    print("我喜欢吃", fruit)

# 使用 break 退出循环
for i in range(10):
    if i == 5:
        break
    print(i)

# 使用 continue 跳过当前循环
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# 使用 else 子句在循环结束后执行代码
for i in range(5):
    print(i)
else:
    print("循环结束")

# 嵌套循环
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# 列表推导式
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# 使用 enumerate 获取索引和值
for index, fruit in enumerate(fruits):
    print(f"索引 {index} 对应的水果是 {fruit}")

# 使用 zip 同时遍历多个序列
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# enumerate 的使用
for i in enumerate(fruits, start=1):
    print(f"测试水果{i}")


# 编写⼀个猜数字的游戏程序。随机产⽣⼀个 100 以内的整数，并要求⽤户输⼊
# 三次数据，当任意⼀次输⼊的数字和随机数相同，游戏结束。否则需程序运⾏
# 三次后，提示正确答案，退出程序。 
# 提示： 使⽤ random.randint(1, 10) 函数，可以产⽣指定范围的随机数

import random
random_num = random.randint(1, 100)
# print(f"正确答案是: {random_num}")
# index = 0
# while index < 3:
#     guess_num = int(input("请输入一个 1-100 之间的整数: "))
#     index += 1
#     if guess_num == random_num:
#         print("恭喜你，猜对了！")
#         break
#     else:
#         print("猜错了，请继续猜！")

# print(f"正确答案是: {random_num}")

# 请根据以下要求，对该列表进⾏处理 [ "rachel", "monica", "Phoebe", "joey" ]： 
# 1. 需要将该列表按照⾸字⺟升序进⾏排列； 
# 2. 需将该列表中的每个元素全部改为⼤写字⺟； 
# 3. 需输出排序后的序号和列表内容

workList = [ "rachel", "monica", "Phoebe", "joey" ]
for i in range(len(workList)):
    # 将单词改为全部大写
    workList[i] = workList[i].upper()
print(workList)

# 需要将该列表按照⾸字⺟升序进⾏排列
workList.sort()

# 输出排序后的序号和列表内容
for index, item in enumerate(workList, start=1):
    print(f"{index}: {item}")

#请你使⽤嵌套语句在命令⾏打印九九乘法表：
for x in range(1,10):
    for y in range(1,x+1):
        print(f"{x} * {y} = {x * y}", end=" ")
    print("")   