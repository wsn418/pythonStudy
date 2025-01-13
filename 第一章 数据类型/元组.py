# 元组（Tuple）和序列（Sequence）在Python中都是用于存储多个元素的数据结构，但它们有一些关键的区别：

# 可变性：

# 元组是不可变的。一旦创建了元组，就不能修改其内容。这意味着你不能添加、删除或更改元组中的元素。
# 序列（如列表）是可变的。你可以随时修改列表的内容，包括添加、删除或更改元素。
# 语法：

# 元组使用圆括号 () 来定义。例如：my_tuple = (1, 2, 3)
# 列表使用方括号 [] 来定义。例如：my_list = [1, 2, 3]
# 用途：

# 元组通常用于存储一组相关的数据，这些数据在整个程序的生命周期中不应改变。由于元组是不可变的，它们可以用作字典的键或存储在集合中。
# 列表则用于需要频繁修改的数据集合。
# 性能：

# 由于元组是不可变的，它们在某些情况下可能比列表更高效。元组的不可变性使得它们在某些优化中表现更好。

# 定义一个元组

# 定义一个空元组
empty_tuple = ()
print("空元组:", empty_tuple)

# 定义一个包含单个元素的元组（注意逗号）
single_element_tuple = (1,)
print("单元素元组:", single_element_tuple)

# 使用 tuple() 函数将列表转换为元组
list_to_tuple = tuple([1, 2, 3])
print("列表转换为元组:", list_to_tuple)

# 使用 tuple() 函数将字符串转换为元组
string_to_tuple = tuple("hello")
print("字符串转换为元组:", string_to_tuple)

# 使用 tuple() 函数将字典的键转换为元组
dict_to_tuple = tuple({"a": 1, "b": 2})
print("字典键转换为元组:", dict_to_tuple)

my_tuple = (1, 2, 3)
print("元组:", my_tuple)

# 尝试修改元组中的元素（会引发错误）
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# 定义一个列表
my_list = [1, 2, 3]
print("列表:", my_list)

# 修改列表中的元素
my_list[0] = 10
print("修改后的列表:", my_list)

# 序列操作示例

# 获取序列中的最大值和最小值
print("元组中的最大值:", max(my_tuple))
print("元组中的最小值:", min(my_tuple))
print("列表中的最大值:", max(my_list))
print("列表中的最小值:", min(my_list))

# 计算序列中某个元素出现的次数
print("元组中2出现的次数:", my_tuple.count(2))
print("列表中10出现的次数:", my_list.count(10))

# 查找序列中某个元素的索引
print("元组中2的索引:", my_tuple.index(2))
print("列表中10的索引:", my_list.index(10))
# 获取序列的长度
print("元组长度:", len(my_tuple))
print("列表长度:", len(my_list))

# 访问序列中的元素
print("元组第一个元素:", my_tuple[0])
print("列表第一个元素:", my_list[0])

# 切片操作
print("元组切片:", my_tuple[1:3])
print("列表切片:", my_list[1:3])

# 序列连接
new_tuple = my_tuple + (4, 5)
new_list = my_list + [4, 5]
print("连接后的元组:", new_tuple)
print("连接后的列表:", new_list)

# 序列重复
print("重复元组:", my_tuple * 2)
print("重复列表:", my_list * 2)

# 检查元素是否在序列中
print("2 是否在元组中:", 2 in my_tuple)
print("10 是否在列表中:", 10 in my_list)

# 遍历序列
print("遍历元组:")
for item in my_tuple:
    print(item)

print("遍历列表:")
for item in my_list:
    print(item)

# newTup = tuple('xyz')
# print(newTup)
# newTup[2]