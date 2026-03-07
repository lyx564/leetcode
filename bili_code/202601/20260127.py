"""
242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

提示:
1 <= s.length, t.length <= 5 * 104
s 和 t 仅包含小写字母

https://leetcode.cn/problems/valid-anagram/
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        for x in s:
            if x not in s_count:
                s_count[x] = 0
            s_count[x] += 1
        for x in t:
            if x not in s_count or s_count[x] == 0:
                return False
            s_count[x] -= 1
        for x in s_count.keys():
            if s_count[x] > 0:
                return False
        return True



if __name__ == '__main__':
    res = Solution().isAnagram(s = "anagram", t = "nagaram")
    print(res)