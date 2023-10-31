"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
输入：digits = ""
输出：[]

示例 3：
输入：digits = "2"
输出：["a","b","c"]

https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
"""

class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        num2word = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        word_lists = []
        for s in digits:
            word_lists.append(list(num2word[s]))
        if len(digits) == 1:
            return word_lists[0]

        for i in range(1, len(digits)):
            word1, word2 = word_lists[i-1], word_lists[i]
            now_res = []
            for w_1 in word1:
                for w_2 in word2:
                    now_res.append(w_1 + '' + w_2)
            word_lists[i] = now_res
        return word_lists[-1]


    def letterCombinations_1(self, digits: str):
        if not digits:
            return []
        num2word = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 1:
            return list(num2word[digits[0]])
        self.res = []

        def digui(now_i, now_res):
            if len(now_res) == len(digits):
                self.res.append(now_res)
                return
            for i in list(num2word[digits[now_i]]):
                digui(now_i+1, now_res+''+i)
        digui(0, '')
        return self.res



if __name__ == '__main__':
    res = Solution().letterCombinations_1(digits = "23")
    print(res)