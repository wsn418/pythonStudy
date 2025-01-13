# 集合（set）是Python中的一种数据类型，它是一个无序且不重复的元素集合。
# 集合主要用于成员测试和消除重复元素，可以使用大括号 {} 或者 set() 函数来创建集合。

# 创建集合
# 使用大括号创建集合
fruits = {"apple", "banana", "cherry"}
print(fruits)

# 使用 set() 函数创建集合
vegetables = set(["carrot", "potato", "cucumber"])
print(vegetables)

# 集合的基本操作
# 添加元素
fruits.add("orange")
print(fruits)

# 移除元素
fruits.remove("banana")
print(fruits)

# 成员测试
print("apple" in fruits)
print("banana" in fruits)

# 集合运算
# 并集
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # 输出: {1, 2, 3, 4, 5}

# 交集
print(set1 & set2)  # 输出: {3}

# 差集
print(set1 - set2)  # 输出: {1, 2}

# 对称差集
print(set1 ^ set2)  # 输出: {1, 2, 4, 5}

# 集合推导式
squared = {x**2 for x in range(10)}
print(squared)

# 冻结集合
# 冻结集合（frozenset）是不可变的集合，一旦创建就不能修改
frozen_set = frozenset([1, 2, 3, 4])
print(frozen_set)

# 创建一个 frozenset
fs = frozenset([1, 2, 3, 4, 5])

# 尝试添加元素会导致错误
# fs.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'

# 可以进行集合操作，例如并集、交集等
another_fs = frozenset([3, 4, 5, 6, 7])
union_fs = fs | another_fs  # 并集
intersection_fs = fs & another_fs  # 交集

print("frozenset:", fs)
print("Union:", union_fs)
print("Intersection:", intersection_fs)


# 给列表去重并且转换为元组输出
list1 = [ 'r', 'g', 'b', 'g', 'b', 'r', 'g' ]
listSet = set(list1)
newTuple = tuple(listSet)
print(newTuple)