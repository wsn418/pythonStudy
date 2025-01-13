# 计算文件的文章中每个字母出现的次数

import pprint
with open('d:/software/TestCode/pythonStudy/数据类型作业/workWords.txt') as f:
    file_data = f.read()
pprint.pprint(file_data)

print(file_data)

# 生成一个a-z的数组 
import string
a_z = list(string.ascii_lowercase)
A_Z = list(string.ascii_uppercase)
print(a_z)
# print(string.ascii_lowercase)
# 计算文章中有多少个 a-z 字母 分别输出
count = {}
for i in a_z:
    count[i] = file_data.count(i)
print(count)

for i in A_Z:
    count[i] = file_data.count(i)
print(count)

#将原始文章转换为以单词为单位的列表
import re
from collections import Counter
words = re.findall(r'\b\w+\b', file_data)
print(words)
# 计算每个单词出现的次数
word_count = Counter(words)
print(dict(word_count))

#不用collections方法进行实现
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

# 定义⼀个列表 list1 和元组 tuple1，当 tuple1 作为字典 dict1 的键时，
# 是否能够成功定义字典？请说明原因。执⾏后，观察执⾏结果。
list1 = [ 1, 2, 3]
tuple1 = ( 'abc', list1 )
# dict1 = { tuple1, 1 } 
print(tuple1)
thple2 = ('abc')
dict1 = {'12':'22'}
print(dict1)

# 
it = iter( [ 1, 2, 3, 4 ] )
print( next( it, 0 ) )