"""

螺旋打印矩阵
n * n

"""

def f(n):
    num = 1
    res = [[0 for _ in range(n)] for _ in range(n)]
    i, j = 0, 0
    top, down, left, right = 0, n-1, 0, n-1
    res[0][0] = 1
    while num <= n * n:
        while num <= n * n and i == top and j <= right:
            res[i][j] = num
            num += 1
            j += 1
        top += 1
        j -= 1
        i += 1

        while num <= n * n and j == right and i <= down:
            res[i][j] = num
            num += 1
            i += 1
        right -= 1
        i -= 1
        j -= 1

        while num <= n * n and i == down and j >= left:
            res[i][j] = num
            num += 1
            j -= 1
        down -= 1
        j += 1
        i -= 1

        while num <= n * n and j == left and i >= top:
            res[i][j] = num
            num += 1
            i -= 1
        left += 1
        i += 1
        j += 1

    return res



if __name__ == '__main__':
    res = f(n=4)
    for r in res:
        print(r)