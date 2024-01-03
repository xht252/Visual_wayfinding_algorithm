import graph.graph as gra

def dfs(start , end , g , screen):
    mod = 10 ** 9
    st = [[False for i in range(40)] for j in range(40)]
    st[start[0]][start[1]] = True
    dx = [0 , 0 , 1 , -1]
    dy = [1 , -1 , 0 , 0]
    ans = []
    path = [(start[0] , start[1])]
    # 四个方向
    def fun(x , y):
        gra.show_pos((255, 0, 255), screen, y, x, 0)
        st[x][y] = True

        nonlocal path , ans
        if [x , y] == end:
            ans.append(path)
            return
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            # 代探索的路径
            if tx <= 0 or tx > 25 or ty <= 0 or ty > 25:
                continue
            if g[tx][ty] >= mod or st[tx][ty]:
                continue
            path.append((tx , ty))
            fun(tx , ty)
            path.pop()

    fun(start[0] , start[1])

    gra.show_pos((0, 0, 255), screen, end[0], end[1], 0)
    print(ans)