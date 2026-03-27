"""
541. 反转字符串 II
给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。
如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例 1：
输入：s = "abcdefg", k = 2
输出："bacdfeg"

示例 2：
输入：s = "abcd", k = 2
输出："bacd"

https://leetcode.cn/problems/reverse-string-ii/

"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        i = 0
        last_idx = 0
        while i < len(s):
            i += 2*k
            s[last_idx:last_idx+k] = s[last_idx:last_idx+k][::-1]
            last_idx = i
        if len(s) - last_idx >= k:
            s[last_idx:last_idx+k] = s[last_idx:last_idx+k][::-1]
        else:
            s[last_idx:] = s[last_idx:][::-1]
        return ''.join(s)


if __name__ == '__main__':
    res = Solution().reverseStr(s = "abcdefg", k = 8)
    print(res)