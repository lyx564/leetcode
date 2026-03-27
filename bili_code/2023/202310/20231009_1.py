# 找出字符串s中a和b数量相等的最长子串

def f(string):
    n = len(string)
    nums = []
    res = 0
    for s in string:
        if s == 'a':
            nums.append(1)
        else:
            nums.append(-1)
    print(nums)
    sums = [0 for _ in range(n)]
    sums[0] = nums[0]
    for i in range(1, n):
        sums[i] = sums[i - 1] + nums[i]
    print(sums)
    for i in range(n):
        j = n-1
        while j < n and sums[j] - sums[i] != 0:
            j -= 1
        if j > i and sums[j] == sums[i]:
            print(i, j)
            res = max(res, j - i)
    return res


if __name__ == '__main__':
    res = f('aabbbaaab')
    print(res)
