"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
输入：digits = "2"
输出：["a","b","c"]

https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
"""


class Solution:
    def letterCombinations(self, digits: str):
        num_2_word = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        self.res = []

        def backtrace(now_idx, now_res):
            if now_idx > len(digits):
                return
            if len(now_res) == len(digits):
                self.res.append(now_res)
                return
            for w in num_2_word[digits[now_idx]]:
                backtrace(now_idx+1, now_res+w)

        backtrace(0, '')
        return self.res


if __name__ == '__main__':
    res = Solution().letterCombinations(digits="23")
    print(res)
