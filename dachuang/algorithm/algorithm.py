import graph.graph as gra

def dfs(start , end , g , screen):
    mod = 10 ** 9
    st = [[False for i in range(40)] for j in range(40)]
    ans = []
    path = []
    dx = [0 , 0 , 1 , -1]
    dy = [1 , -1 , 0 , 0]
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
        if [y , x] == end:
            ans.append(path.copy())

        gra.show_pos((255, 0, 255), screen, y, x, 0)
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            fun(g , tx , ty)
        st[x][y] = False
        path.pop()

    fun(g , start[1] , start[0])
    path = []
    for i in ans:
        if not len(path):
            path = i
        else:
            if len(path) > len(i):
                path = i
    print(path)
    for i in path:
        gra.show_pos((0 , 255 , 127) , screen , i[1] , i[0] , 0)

    gra.show_pos((0, 0, 255), screen, start[0], start[1], 0)
    gra.show_pos((0, 0, 255), screen, end[0], end[1], 0)