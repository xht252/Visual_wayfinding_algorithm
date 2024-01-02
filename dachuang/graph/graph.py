from tkinter import Tk, Label, Entry, IntVar, ttk, Radiobutton, Button

import pygame
# 以25x25的方格矩阵为例讨论

def show_pos(color , screen , x , y , st):
    # 填充方格
    # 1空心
    # 0实心
    t = 540 // 27
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
    screen = pygame.display.set_mode((540, 540))
    cols , rows = 27 , 27

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
    start = Label(window, text='(注意坐标为1~25,填写形式1,1)起点坐标(x,y): ')
    startBox = Entry(window)
    end = Label(window, text='(注意坐标为1~25,填写形式1,1)终点坐标(x,y): ')
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
    grid[pos_s[1]][pos_s[0]] = 0x3f3f3f3f3f
    grid[pos_e[1]][pos_e[0]] = 0x3f3f3f3f3f

    pos_s[0] , pos_s[1] = pos_s[1] , pos_s[0]
    pos_e[0], pos_e[1] = pos_e[1], pos_e[0]
    def mousePress(x):
        t = x[0]
        w = x[1]
        # 判断在第几个格子
        g1 = t // (540 // cols)
        g2 = w // (540 // rows)
        # 设置障碍
        grid[g2][g1] = 0x3f3f3f3f
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

    return pos_s , pos_e , idx , grid