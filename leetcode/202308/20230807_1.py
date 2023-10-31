"""
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/zi-fu-chuan-de-pai-lie-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution:
    def permutation(self, s: str):
        all_res = []

        def huisu(s, res):
            if len(s) == 0:
                all_res.append(''.join(res))
                return
            his = set()
            for i in range(len(s)):
                if s[i] in his:
                    continue
                his.add(s[i])
                huisu(s[:i] + s[i+1:], res+s[i])

        huisu(s, '')
        return all_res


if __name__ == '__main__':
    res = Solution().permutation(s = "aab")
    print(res)
