"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例 1:

输入：s = "abaccdeff"
输出：'b'
示例 2:

输入：s = ""
输出：' '

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def firstUniqChar(self, s: str) -> str:
        w_map = {}
        for c in s:
            if c not in w_map:
                w_map[c] = 0
            w_map[c] += 1
        for c in s:
            if w_map[c] == 1:
                return c
        return ' '

    def firstUniqChar_1(self, s: str) -> str:
        w_pos = {}
        for i in range(len(s)):
            if s[i] not in w_pos:
                w_pos[s[i]] = i
            else:
                w_pos[s[i]] = -1
        idx = len(s)
        for c in w_pos.keys():
            if w_pos[c] != -1:
                idx = min(idx, w_pos[c])
        return s[idx] if idx < len(s) else ' '



if __name__ == '__main__':
    res = Solution().firstUniqChar_1(s = "abaccdeff")
    print(res)