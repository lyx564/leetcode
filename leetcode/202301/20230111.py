"""
2283. 判断一个数的数字计数是否等于数位的值
给你一个下标从 0 开始长度为 n 的字符串 num ，它只包含数字。

如果对于 每个 0 <= i < n 的下标 i ，都满足数位 i 在 num 中出现了 num[i]次，那么请你返回 true ，否则返回 false 。



示例 1：

输入：num = "1210"
输出：true
解释：
num[0] = '1' 。数字 0 在 num 中出现了一次。
num[1] = '2' 。数字 1 在 num 中出现了两次。
num[2] = '1' 。数字 2 在 num 中出现了一次。
num[3] = '0' 。数字 3 在 num 中出现了零次。
"1210" 满足题目要求条件，所以返回 true 。
示例 2：

输入：num = "030"
输出：false
解释：
num[0] = '0' 。数字 0 应该出现 0 次，但是在 num 中出现了一次。
num[1] = '3' 。数字 1 应该出现 3 次，但是在 num 中出现了零次。
num[2] = '0' 。数字 2 在 num 中出现了 0 次。
下标 0 和 1 都违反了题目要求，所以返回 false 。


提示：

n == num.length
1 <= n <= 10
num 只包含数字。
"""


class Solution:
    def digitCount(self, num: str) -> bool:
        count = [0]*10
        for n in num:
            count[int(n)] += 1
        for i in range(len(num)):
            if count[i] != int(num[i]):
                return False
        return True


"""
字符串的规范化输出，驼峰转下划线，LeetCode转化为leet_code，LeetHTTPBack转化为leet_http_back
"""


def get_trans_name(text):
    text = text + 'A'
    now = ''
    res = []
    for i in range(len(text)-1):
        if text[i].isupper():
            if text[i+1].islower():
                res.append(now)
                now = text[i]
            else:
                now = now + text[i]
        else:
            if text[i+1].isupper():
                res.append(now+text[i])
                now = ''
            else:
                now = now + text[i]
    res.append(now)
    res2 = []
    for r in res:
        if r:
            res2.append(r)
    return '_'.join(res2)


if __name__ == '__main__':
    # s = Solution()
    # res = s.digitCount(num = "030")
    # print(res)

    print(get_trans_name("LeetCodeA"))
    print(get_trans_name("LeetHTTPBack"))
    print(get_trans_name("HTTPBackAAQa"))
