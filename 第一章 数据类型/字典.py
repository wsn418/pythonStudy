# 字典概述

# 字典是Python中的一种内置数据类型，用于存储键值对（key-value pairs）。
# 每个键（key）必须是唯一的，且是不可变的（如字符串、数字或元组），
# 而值（value）可以是任何数据类型。

# 创建字典
# 使用类构造器创建字典
my_dict = dict(name='Alice', age=25, city='New York')

# 使用元组列表创建字典
my_dict = dict([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# 使用字典推导式创建字典
my_dict = {key: value for key, value in [('name', 'Alice'), ('age', 25), ('city', 'New York')]}

my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# 访问字典中的值
print(my_dict['name'])  # 输出: Alice

# 添加或更新键值对
my_dict['email'] = 'alice@example.com'
my_dict['age'] = 26

# 删除键值对
del my_dict['city']

# 遍历字典
for key, value in my_dict.items():
    print(f'{key}: {value}')

# 字典方法
# 删除指定键值对
my_dict.pop('name', None)  # 如果键不存在，不会引发错误

# 删除并返回任意键值对
key, value = my_dict.popitem()

# 判断字典是否为空
is_empty = not my_dict

# 获取字典的长度
length = len(my_dict)

# 合并两个字典
another_dict = {}
merged_dict = {**my_dict, **another_dict}

# 从字典中获取值，如果键不存在则设置默认值
value = my_dict.setdefault('country', 'Unknown')

# 获取所有键
keys = my_dict.keys()

# 获取所有值
values = my_dict.values()

# 获取所有键值对
items = my_dict.items()

# 检查键是否存在
if 'name' in my_dict:
    print('Name is in the dictionary')

# 获取键对应的值，如果键不存在则返回默认值
age = my_dict.get('age', 0)

# 清空字典
my_dict.clear()

# 复制字典
new_dict = my_dict.copy()

# 合并字典
another_dict = {'country': 'USA', 'gender': 'Female'}
my_dict.update(another_dict)

# 字典推导式
squared_numbers = {x: x**2 for x in range(5)}

# 输出: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(squared_numbers)

my_dict = {key: value for key, value in [('name', 'Alice'), ('age', 25), ('city', 'New York')]}

print("字典:", my_dict)

# 已知有两个列表，分别为: 
# [ 'name1', 'name2', 'name3' ] 
# [ '1111', '2222', '3333'] 
# 现需要将这两个列表组成⼀个如下字典，请编写程序实现： 
# { 'name1':'1111', 'name2':'2222', 'name3':'3333' }

keyList =  [ 'name1', 'name2', 'name3']
valueList = [ '1111', '2222', '3333']
my_dict = dict(zip(keyList, valueList))
my_dict = {key: value for key, value in zip(keyList, valueList)}
my_dict = {keyList[i]: valueList[i] for i in range(len(keyList))}

# 使用 setdefault 方法
# setdefault 方法用于获取指定键的值，如果键不存在，则将该键设置为指定的默认值，并返回该默认值。

# 示例
my_dict = {'name': 'Alice', 'age': 25}

# 获取存在的键的值
name = my_dict.setdefault('name', 'Unknown')
print(name)  # 输出: Alice

# 获取不存在的键的值，并设置默认值
country = my_dict.setdefault('country', 'Unknown')
print(country)  # 输出: Unknown

# 查看更新后的字典
print(my_dict)  # 输出: {'name': 'Alice', 'age': 25, 'country': 'Unknown'}

# 使用 |= 运算符合并字典
# 从 Python 3.9 开始，可以使用 |= 运算符来合并两个字典，新字典的键值对将覆盖原字典中的相同键值对。

dict1 = {'name': 'Alice', 'age': 25}
dict2 = {'city': 'New York', 'email': 'alice@example.com'}

# 合并 dict2 到 dict1
dict1 |= dict2

print(dict1)
# 输出: {'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com'}

# zip() 函数
# zip() 函数用于将多个可迭代对象（如列表、元组等）打包成一个元组的迭代器。
# 当你需要并行迭代多个可迭代对象时，zip() 非常有用。

# 示例
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# 使用 zip() 将两个列表打包成一个迭代器
zipped = zip(list1, list2)

# 将迭代器转换为列表
zipped_list = list(zipped)
print(zipped_list)  # 输出: [(1, 'a'), (2, 'b'), (3, 'c')]

# 遍历 zip() 生成的迭代器
for num, char in zip(list1, list2):
    print(f'Number: {num}, Character: {char}')

# 使用 zip() 解压缩
numbers, characters = zip(*zipped_list)
print(numbers)     # 输出: (1, 2, 3)
print(characters)  # 输出: ('a', 'b', 'c')

#使用*对数组进行解构
print([(1,'a'),(2,'b'),(3,'c')])
print(*[(1,'a'),(2,'b'),(3,'c')])

# 请你设计⼀个字典数据类型⽤于存储通讯录，通讯录中包含： 
# 必须填写的姓名、可以为空的备注名、1 个邮箱、⾄少 2 个⼿机号码， 
# 并尝试增加和删除联系⼈

contacts = {
    'name':'123',
    'email':'197@qq.com',
    'phone':[131],
}

# 添加联系人
conTactsList = []
conTactsList.append(contacts)
print(conTactsList)

# # 删除联系人
# conTactsList.remove(contacts)
# print(conTactsList)

#删除name为123的联系人
conTactsList = [contact for contact in conTactsList if contact['name'] != '123']
print(conTactsList)