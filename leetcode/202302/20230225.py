"""
有两个长度相同的字符串s1 和s2，且它们其中只含有字符"x" 和"y"，你需要通过「交换字符」的方式使这两个字符串相同。
每次「交换字符」的时候，你都可以在两个字符串中各选一个字符进行交换。
交换只能发生在两个不同的字符串之间，绝对不能发生在同一个字符串内部。也就是说，我们可以交换s1[i] 和s2[j]，但不能交换s1[i] 和s1[j]。
最后，请你返回使 s1 和 s2 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回-1 。

示例 1：
输入：s1 = "xx", s2 = "yy"
输出：1
解释：
交换 s1[0] 和 s2[1]，得到 s1 = "yx"，s2 = "yx"。

示例 2：
输入：s1 = "xy", s2 = "yx"
输出：2
解释：
交换 s1[0] 和 s2[0]，得到 s1 = "yy"，s2 = "xx" 。
交换 s1[0] 和 s2[1]，得到 s1 = "xy"，s2 = "xy" 。
注意，你不能交换 s1[0] 和 s1[1] 使得 s1 变成 "yx"，因为我们只能交换属于两个不同字符串的字符。

示例 3：
输入：s1 = "xx", s2 = "xy"
输出：-1

示例 4：
输入：s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
输出：4

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-swaps-to-make-strings-equal
"""


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = 0, 0
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy += 1
            if a == 'y' and b == 'x':
                yx += 1
        if (xy + yx) % 2 == 1:
            return -1
        return xy // 2 + yx // 2 + xy % 2 + yx % 2


if __name__ == '__main__':
    res = Solution().minimumSwap(s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx")
    print(res)