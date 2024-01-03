import math
import sys
from turtle import goto

import pygame

from tkinter import Tk, Label, Entry, IntVar, ttk, Radiobutton, Button
import pygame
# 以25x25的方格矩阵为例讨论

def dfs(start , end , g , screen):
    st = [[False for i in range(40)] for j in range(40)]
    ans = []
    path = []
    dx = [1 , -1 , 0 , 0]
    dy = [0 , 0 , 1 , -1]
    # 四个方向
    def fun(g , x , y):
        nonlocal path, ans
        if len(ans):
            return
        if x <= 0 or y <= 0 or x > 15 or y > 15:
            return
        if g[x][y] != 0 or st[x][y]:
            return
        st[x][y] = True
        path.append((x , y))
        if [x , y] == end:
            ans.append(path.copy())

        show_pos((255, 0, 255), screen, y, x, 0)
        pygame.time.delay(1)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            fun(g , tx , ty)
        st[x][y] = False
        path.pop()

    fun(g , start[0] , start[1])
    path = []
    for i in ans:
        if not len(path):
            path = i
        else:
            if len(path) > len(i):
                path = i

    for i in path:
        show_pos((0 , 255 , 127) , screen , i[1] , i[0] , 0)
        pygame.time.delay(1)
    show_pos((0, 0, 255), screen, start[1], start[0], 0)
    show_pos((0, 0, 255), screen, end[1], end[0], 0)

### 注意没有路径选择
def bfs(start, end, g, screen):
    queue = [(start[0], start[1])]
    st = [[False for i in range(40)] for j in range(40)]
    # dist = [[10 ** 9 for i in range(40)] for j in range(40)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    parent = {}
    path = []
    # dist[start[0]][start[1]] = 0
    while len(queue):
        x, y = queue[0]
        queue.pop(0)

        show_pos((255, 0, 255), screen, y, x, 0)
        pygame.time.delay(1)
        if [x , y] == end:
            break

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx <= 0 or ty <= 0 or tx > 15 or ty > 15:
                continue
            if g[tx][ty] != 0 or st[tx][ty]:
                continue
            st[x][y] = True
            parent[(tx , ty)] = (x , y)
            # dist[tx][ty] = dist[x][y] + 1
            queue.append((tx, ty))

    print(parent)
    now = tuple(end)
    while now != tuple(start):
        path.append(now)
        now = parent[now]

    path = path[::-1]
    for i in path:
        show_pos((0 , 255 , 127) , screen , i[1] , i[0] , 0)
        pygame.time.delay(10)

def dij(start, end, g, screen):
    # 对于解决该问题该方法没有意义
    # 因为边权一样，即两点的距离都是某一个距离x
    # 对于迪杰斯特拉算法不是非常的使用
    # 可以用bfs线性的复杂度的方法解决
    return "unknown"

def Astar(start , end , grid , screen):
    '''
    * 初始化open_set和close_set；
    * 将起点加入open_set中，并设置优先级为0（优先级最高）；
    * 如果open_set不为空，则从open_set中选取优先级最高的节点n：
        * 如果节点n为终点，则：
            * 从终点开始逐步追踪parent节点，一直达到起点；
            * 返回找到的结果路径，算法结束；
        * 如果节点n不是终点，则：
            * 将节点n从open_set中删除，并加入close_set中；
            * 遍历节点n所有的邻近节点：
                * 如果邻近节点m在close_set中，则：
                    * 跳过，选取下一个邻近节点
                * 如果邻近节点m也不在open_set中，则：
                    * 设置节点m的parent为节点n
                    * 计算节点m的优先级
                    * 将节点m加入open_set中
    '''
    dx = [0 , 0 , 1 , -1]
    dy = [1 , -1 , 0 , 0]
    def Manhattan(x , y , start):
        return abs(start[0] - x) + abs(start[1] - y)
    def Euclid(x , y , start):
        return math.sqrt(pow(x - start[0] , 2) + pow(y - start[1] , 2))

    open_set , close_set = [] , []
    open_set.append((start[0] , start[1] , 0))
    parent = {}

    while len(open_set):
        fx = 10 ** 9
        now = 0
        idx = -1
        for i in range(len(open_set)):
            x , y , g = open_set[i]
            tfx = g + Manhattan(x , y , start)
            if tfx < fx:
                fx = tfx
                idx = i
                now = open_set[i]

        show_pos((255, 0, 255), screen, now[1], now[0], 0)
        pygame.time.delay(10)

        for i in range(4):
            tx = now[0] + dx[i]
            ty = now[1] + dy[i]
            g = now[2]

            if tx <= 0 or ty <= 0 or tx > 15 or ty > 15:
                continue
            if grid[tx][ty] != 0 or (tx , ty) in close_set:
                continue

            if (tx , ty , g + 1) not in open_set:
                open_set.append((tx , ty , g + 1))
                parent[(tx , ty)] = (now[0] , now[1])

        open_set.pop(idx)
        close_set.append((now[0] , now[1]))
        f = False
        for i in open_set:
            if [i[0] , i[1]] == end:
                f = True
                break
        if f:
            break
    path = []
    now = tuple(end)
    while now != tuple(start):
        path.append(now)
        now = parent[now]

    path = path[::-1]
    for i in path:
        show_pos((0 , 255 , 127) , screen , i[1] , i[0] , 0)
        pygame.time.delay(10)


def show_pos(color , screen , x , y , st):
    # 填充方格
    # 1空心
    # 0实心
    t = 340 // 17
    pygame.draw.rect(screen , color , (x * t , y * t , t , t) , st)
    pygame.display.update()

def show():
    pygame.init()
    pygame.display.set_caption("My Board")
    exit = False
    show_map()
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True


def show_map():
    mod = 10 ** 9
    screen = pygame.display.set_mode((340 , 340), pygame.HWSURFACE)
    screen.set_alpha(None)
    cols , rows = 17 , 17

    # 定义颜色
    black = (0 , 0 , 0)
    white = (255 , 255 , 255)
    green = (0 , 255 , 0)
    pink = (255 , 192 , 203)
    red = (255 , 0 , 0)
    blue = (0 , 0 , 255)

    grey = (220, 220, 220)

    # 矩阵
    grid = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            show_pos(white , screen , i , j , 1)

    # 画围墙
    for i in range(rows):
        show_pos(grey , screen , i, 0, 0)
        show_pos(grey, screen, i, cols - 1, 0)
        show_pos(grey, screen, 0, i, 0)
        show_pos(grey, screen, cols - 1, i, 0)


    # 输入起始和终止点
    global window
    window = Tk()
    window.title('初始化地图')
    start = Label(window, text='(注意坐标为1~15,填写形式1,1)起点坐标(x,y): ')
    startBox = Entry(window)
    end = Label(window, text='(注意坐标为1~15,填写形式1,1)终点坐标(x,y): ')
    endBox = Entry(window)

    var = IntVar()

    d = {0 : "深度优先遍历dfs" , 1 : "广度优先遍历bfs" , 2 : "迪杰斯特拉算法" , 3 : "A星算法"}

    idx = 0
    def get_idx():
        nonlocal idx
        idx1 = var.get()
        idx = idx1


    for x, y in d.items():
        b = Radiobutton(window, text=y, variable=var, value=x , command=get_idx)
        b.pack()

    pos_s , pos_e = [] , []
    def onsubmit():
        st = list(map(int , startBox.get().split(',')))
        en = list(map(int , endBox.get().split(',')))

        nonlocal pos_s , pos_e
        # 获取坐标
        pos_s = st
        pos_e = en

        window.quit()
        window.destroy()
    start.pack()
    startBox.pack()

    end.pack()
    endBox.pack()

    submit = Button(window, text='提交', command=onsubmit)
    submit.pack()
    window.mainloop()

    show_pos(blue , screen , pos_s[1] , pos_s[0] , 0)
    show_pos(blue , screen , pos_e[1] , pos_e[0] , 0)
    pygame.display.flip()
    # pos_s[0] , pos_s[1] = pos_s[1] , pos_s[0]
    # pos_e[0], pos_e[1] = pos_e[1], pos_e[0]
    def mousePress(x):
        t = x[0]
        w = x[1]
        # 判断在第几个格子
        g1 = t // (340 // cols)
        g2 = w // (340 // rows)
        # 设置障碍
        grid[g2][g1] = mod
        if [g2 , g1] != pos_s and [g2 , g1] != pos_e:
            show_pos(grey, screen , g1 , g2 , 0)

    # 画障碍
    loop = True
    while loop:
        ev = pygame.event.poll()
        if pygame.mouse.get_pressed()[0]:
            try:
                pos = pygame.mouse.get_pos()
                mousePress(pos)
            except AttributeError:
                pass
        if ev.type == pygame.QUIT:
            pygame.quit()
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_SPACE:
                loop = False

    pygame.display.flip()
    return pos_s , pos_e , idx , grid , screen



if __name__ == "__main__":
    exit = False
    while not exit:
        pygame.init()
        pygame.display.set_caption("My Board")
        start , end , idx , grid , screen = show_map()
        clock = pygame.time.Clock()
        if idx == 0:
            dfs(start , end , grid , screen)
        elif idx == 1:
            bfs(start , end , grid , screen)
        elif idx == 2:
            dij(start , end , grid , screen)
        else:
            Astar(start , end , grid , screen)
        while True:
            f = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
                    f = True
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        f = True
                        break
            if f:
                break
