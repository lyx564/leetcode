"""
763. 划分字母区间
给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
例如，字符串 "ababcc" 能够被分为 ["abab", "cc"]，但类似 ["aba", "bcc"] 或 ["ab", "ab", "cc"] 的划分是非法的。
注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
返回一个表示每个字符串片段的长度的列表。

示例 1：
输入：s = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。

示例 2：
输入：s = "eccbbbbdec"
输出：[10]

https://leetcode.cn/problems/partition-labels/description/
"""


class Solution:
    def partitionLabels(self, s: str):
        word_2_l_r_pos = {}
        for idx, w in enumerate(s):
            if w not in word_2_l_r_pos:
                word_2_l_r_pos[w] = [9999999999, -999999999]
            word_2_l_r_pos[w][0] = min(word_2_l_r_pos[w][0], idx)
            word_2_l_r_pos[w][1] = max(word_2_l_r_pos[w][1], idx)
        now_pos = [word_2_l_r_pos[w] for w in word_2_l_r_pos.keys()]
        now_pos.sort(key=lambda x: x[0])
        # print(now_pos)
        res = []
        now_l = now_pos[0][0]
        max_r = now_pos[0][1]
        for l, r in now_pos[1:]:
            if l < max_r:
                max_r = max(max_r, r)
            else:
                res.append(max_r-now_l+1)
                now_l = l
                max_r = r
        res.append(max_r-now_l+1)
        return res

    def partitionLabels_1(self, s: str):
        w_max_r = {s[i]: i for i in range(len(s))}
        max_r = -1
        l = 0
        res = []
        for i in range(len(s)):
            w = s[i]
            max_r = max(max_r, w_max_r[w])
            if i == max_r:
                res.append(max_r-l+1)
                l = i+1
        return res


if __name__ == '__main__':
    res = Solution().partitionLabels_1(s = "ababcbacadefegdehijhklij")
    print(res)