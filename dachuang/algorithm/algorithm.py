from time import sleep
import threading
import pygame

import graph.graph as gra

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
        if x <= 0 or y <= 0 or x > 25 or y > 25:
            return
        if g[x][y] != 0 or st[x][y]:
            return
        st[x][y] = True
        path.append((x , y))
        if [x , y] == end:
            ans.append(path.copy())

        gra.show_pos((255, 0, 255), screen, y, x, 0)
        pygame.time.delay(5)

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
        gra.show_pos((0 , 255 , 127) , screen , i[1] , i[0] , 0)
        pygame.time.delay(5)
    gra.show_pos((0, 0, 255), screen, start[1], start[0], 0)
    gra.show_pos((0, 0, 255), screen, end[1], end[0], 0)


def bfs(start, end, g, screen):
    queue = [(start[0], start[1])]
    st = [[False for i in range(40)] for j in range(40)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    path = []
    print(start , end)
    while len(queue):
        x, y = queue[0]
        queue.pop(0)

        gra.show_pos((255, 0, 255), screen, y, x, 0)

        st[x][y] = True
        path.append((x, y))
        if [x , y] == end:
            break

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if tx <= 0 or ty <= 0 or tx > 25 or ty > 25:
                continue
            if g[tx][ty] != 0 or st[tx][ty]:
                continue
            queue.append((tx, ty))


    for i in path:
        gra.show_pos((0, 255, 127), screen, i[1], i[0], 0)