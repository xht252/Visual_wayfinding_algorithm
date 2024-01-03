import graph.graph as gra

def dfs(start , end , g , screen):
    st = [[False for i in range(40)] for j in range(40)]
    dx = [0 , 0 , 1 , -1]
    dy = [1 , -1 , 0 , 0]
    f = False
    path = []
    # 四个方向
    def fun(x , y):
        nonlocal f , path
        if f:
            return True
        if [x , y] == end:
            f = True
            return True

        path.append((x , y))
        st[x][y] = True
        # 已经走过的路径
        gra.show_pos((124,252,0) , screen , x , y , 0)

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            # 代探索的路径
            if tx <= 0 or tx > 25 or ty <= 0 or ty > 25:
                continue
            if (g[tx][ty] == 0x3f3f3f3f3f and [tx , ty] == end) or st[tx][ty]:
                continue
            gra.show_pos((255 , 0 , 255) , screen , tx , ty , 0)
            fun(tx , ty)
        path.pop()

    fun(start[0] , start[1])
    print(path)