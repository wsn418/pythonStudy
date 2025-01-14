import os
# import chardet
import locale
import shutil

# Python 文件的打开

# 使用 open() 函数打开文件
# open() 函数的第一个参数是文件的路径，第二个参数是模式（mode）
# 常见的模式有：
# 'r' - 只读模式（默认）
# 'w' - 写入模式（会覆盖文件，如果文件不存在则创建）
# 'a' - 追加模式（在文件末尾添加内容，如果文件不存在则创建）
# 'b' - 二进制模式（与其他模式结合使用，如 'rb', 'wb'）
# 't' - 文本模式（默认，与其他模式结合使用，如 'rt', 'wt'）
# 'x' - 独占创建模式（如果文件已存在则会引发 FileExistsError）
# '+' - ⽀持读取与写⼊

# # 示例：以只读模式打开文件
# file_path = 'd:/software/TestCode/pythonStudy/3、输入输出与文件操作/example.txt'
# try:
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print(f"文件 {file_path} 不存在")
# except IOError:
#     print(f"读取文件 {file_path} 时出错")

# # 示例：以写入模式打开文件
# try:
#     with open(file_path, 'w', encoding='utf-8') as file:
#         file.write("这是一个示例文本")
#         print(f"写入文件 {file_path} 成功")
# except IOError:
#     print(f"写入文件 {file_path} 时出错")

# # 示例：以追加模式打开文件
# try:
#     with open(file_path, 'a', encoding='utf-8') as file:
#         file.write("\n这是追加的文本")
#         print(f"追加文件 {file_path} 成功")
# except IOError:
#     print(f"追加文件 {file_path} 时出错")

# # 示例：以二进制模式读取文件
# binary_file_path = '/d:/software/TestCode/pythonStudy/3、输入输出与文件操作/example.bin'
# try:
#     with open(binary_file_path, 'rb') as file:
#         binary_content = file.read()
#         print(binary_content)
# except FileNotFoundError:
#     print(f"文件 {binary_file_path} 不存在")
# except IOError:
#     print(f"读取文件 {binary_file_path} 时出错")
    
# # 导入 os 模块

# # os 模块提供了与操作系统进行交互的功能
# # 例如，可以使用 os 模块来检查文件是否存在、创建目录、删除文件等

#os chdir
#os.chdir 是 Python 中 os 模块提供的一个方法，用于更改当前工作目录。它的全称是 "change directory"。使用这个方法可以将当前的工作目录更改为指定的路径。
#os.chdir(path)
# import os

# # 打印当前工作目录
# print("当前工作目录:", os.getcwd())

# # 更改工作目录
os.chdir('d:/software/TestCode/pythonStudy/3、输入输出与文件操作/')

# # 打印更改后的工作目录
# print("更改后的工作目录:", os.getcwd())

# # 示例：检查文件是否存在
# if os.path.exists(file_path):
#     print(f"文件 {file_path} 存在")
# else:
#     print(f"文件 {file_path} 不存在")

# # 示例：创建目录
# directory_path = 'd:/software/TestCode/pythonStudy/3、输入输出与文件操作/new_directory'
# try:
#     os.makedirs(directory_path)
#     print(f"目录 {directory_path} 创建成功")
# except FileExistsError:
#     print(f"目录 {directory_path} 已经存在")
# except OSError as e:
#     print(f"创建目录 {directory_path} 时出错: {e}")

# # 示例：删除文件
# try:
#     os.remove(file_path)
#     print(f"文件 {file_path} 删除成功")
# except FileNotFoundError:
#     print(f"文件 {file_path} 不存在，无法删除")
# except OSError as e:
#     print(f"删除文件 {file_path} 时出错: {e}")
    
# 示例：使用相对路径打开文件
relative_file_path = './example.txt'

# 创建文件以确保它存在
if not os.path.exists(relative_file_path):
    with open(relative_file_path, 'w', encoding='utf-8') as file:
        file.write("这是一个示例文本")

try:
    with open(relative_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"文件 {relative_file_path} 不存在")
except IOError:
    print(f"读取文件 {relative_file_path} 时出错")
    
    
#如何解决不同操作系统的⽂件乱码问题？
# 解决不同操作系统的文件乱码问题可以通过以下几种方法：

# 1. 使用正确的文件编码
# 确保在打开文件时使用正确的编码，例如 'utf-8'。在写入和读取文件时都指定编码。

# 2. 使用 chardet 库检测文件编码
# chardet 库可以检测文件的编码，然后使用检测到的编码来读取文件。

# Windows 默认使⽤ GBK 编码 
# Linux 和 macOS 使⽤ UTF-8 编码

# def read_file_with_chardet(file_path):
#     with open(file_path, 'rb') as file:
#         raw_data = file.read()
#         result = chardet.detect(raw_data)
#         encoding = result['encoding']
#         print(f"检测到的文件编码: {encoding}")
#         return raw_data.decode(encoding)

# try:
#     content = read_file_with_chardet(relative_file_path)
#     print(content)
# except FileNotFoundError:
#     print(f"文件 {relative_file_path} 不存在")
# except IOError:
#     print(f"读取文件 {relative_file_path} 时出错")

# 3. 使用 locale 模块获取系统默认编码

# default_encoding = locale.getpreferredencoding()
# print(f"系统默认编码: {default_encoding}")

# try:
#     with open(relative_file_path, 'r', encoding=default_encoding) as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print(f"文件 {relative_file_path} 不存在")
# except IOError:
#     print(f"读取文件 {relative_file_path} 时出错")



# 1. 请将以下字符串内容保存到⽂本⽂件 a.txt 中。 
# 2. 请使⽤⽂件读写功能将 a.txt ⽂件复制为 b.txt 并保存。 
string = """Python 3.11 is up to 10-60% faster than Python 3.10. 
On average, we measured a 1.25x speedup on the standard 
benchmark suite. See Faster CPython for details. """

# 示例：使用相对路径打开文件
aTxtPath = './a.txt'
bTxtPath = './b.txt'
# 创建文件以确保它存在
if not os.path.exists(aTxtPath):
    with open(aTxtPath, 'w', encoding='utf-8') as file:
        file.write(string)
#将 a.txt ⽂件复制为 b.txt 并保存
try:
    with open(aTxtPath, 'r', encoding='utf-8') as file_a:
        content = file_a.read()
    with open(bTxtPath, 'w', encoding='utf-8') as file_b:
        file_b.write(content)
    print(f"文件 {aTxtPath} 成功复制为 {bTxtPath}")
except FileNotFoundError:
    print(f"文件 {aTxtPath} 不存在")
except IOError as e:
    print(f"复制文件时出错: {e}")

# 文件的关闭

# 使用 open() 函数打开文件后，应该在不再需要文件时将其关闭。
# 关闭文件可以使用 close() 方法。

# 示例：手动关闭文件
try:
    file = open(aTxtPath, 'r', encoding='utf-8')
    content = file.read()
    print(content)
finally:
    file.close()

# 使用 with 语句可以自动关闭文件，无需显式调用 close() 方法。
# 这是推荐的做法，因为它可以确保文件在任何情况下（即使发生异常）都能正确关闭。

# 示例：使用 with 语句自动关闭文件
try:
    with open(aTxtPath, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"文件 {aTxtPath} 不存在")
except IOError as e:
    print(f"读取文件时出错: {e}")


# 如何使⽤ Python 合并多个⽂件？
# 将a.txt b.txt c.txt 合并到 d.txt中
# 示例：合并多个文件
cTxtPath = './c.txt'
dTxtPath = './d.txt'

# 合并 a.txt, b.txt 和 c.txt 到 d.txt
try:
    with open(dTxtPath, 'w', encoding='utf-8') as file_d:
        for file_path in [aTxtPath, bTxtPath, cTxtPath]:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                file_d.write(content + '\n')
    print(f"文件 {aTxtPath}, {bTxtPath}, {cTxtPath} 成功合并到 {dTxtPath}")
except FileNotFoundError as e:
    print(f"文件不存在: {e}")
except IOError as e:
    print(f"合并文件时出错: {e}")
    
# 将 d.txt 移动到另一个文件夹

destination_folder = './new_folder/'
destination_path = os.path.join(destination_folder, 'd.txt')

# 创建目标文件夹（如果不存在）
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

try:
    shutil.move(dTxtPath, destination_path)
    print(f"文件 {dTxtPath} 成功移动到 {destination_path}")
except FileNotFoundError:
    print(f"文件 {dTxtPath} 不存在")
except IOError as e:
    print(f"移动文件时出错: {e}")