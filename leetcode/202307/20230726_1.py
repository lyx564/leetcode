"""
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        i, j = 0, 0
        res = 1
        now = set()
        while j < len(s):
            if s[j] not in now:
                now.add(s[j])
                j += 1
            else:
                res = max(res, j - i)
                while i < j and s[i] != s[j]:
                    now.remove(s[i])
                    i += 1
                now.remove(s[i])
                i += 1

        return max(res, j-i)




if __name__ == '__main__':
    res = Solution().lengthOfLongestSubstring(s='pwwkew')
    print(res)