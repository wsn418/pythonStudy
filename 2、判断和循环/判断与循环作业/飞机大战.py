from pynput import keyboard

# 对象： 我⽅⻜机、敌机 
# 属性： 坐标、⽣命值 
# ⾏为： 移动、命中⻜机（敌我双⽅

# 使用pynput包监听键盘的输入
# 定义一个处理函数来处理按键按下事件
background = [
    [0, 0, 0],
    [0, 'x', 0],
    [0, 0, 0]
]

HP = 100

# 获取飞机的当前位置
def get_plane_position():
    for i, row in enumerate(background):
        for j, cell in enumerate(row):
            if cell == 'x':
                return i, j

# 更新飞机的位置
def move_plane(new_i, new_j):
    old_i, old_j = get_plane_position()
    background[old_i][old_j] = 0
    background[new_i][new_j] = 'x'

# 打印背景
def print_background():
    for row in background:
        print(*row)
    print(f"当前血量为{HP}")

def on_press(key):
    global HP
    try:
        i, j = get_plane_position()
        if key.char == 'w' and i > 0:
            move_plane(i - 1, j)
        elif key.char == 'a' and j > 0:
            move_plane(i, j - 1)
        elif key.char == 's' and i < len(background) - 1:
            move_plane(i + 1, j)
        elif key.char == 'd' and j < len(background[0]) - 1:
            move_plane(i, j + 1)
        elif key.char == '-':
            HP = HP - 1
            if(HP == 0): 
                print('游戏结束')
                exit(-1)
            # print(HP)
        elif key.char == '+': HP = HP + 1
        print_background()
    except AttributeError:
        pass

# 定义一个处理函数来处理按键释放事件
def on_release(key):
    if key == keyboard.Key.esc:
        # 停止监听
        return False

# 开始监听键盘事件
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

#血量进行加减 加血的时候血量+1 减血的时候血量-1 通过监听键盘上的+和-实现
   