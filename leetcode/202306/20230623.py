"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。

数值（按顺序）可以分成以下几个部分：

若干空格
一个小数或者整数
（可选）一个'e'或'E'，后面跟着一个整数
若干空格
小数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
下述格式之一：
至少一位数字，后面跟着一个点 '.'
至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
一个点 '.' ，后面跟着至少一位数字
整数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
至少一位数字
部分数值列举如下：

["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]
部分非数值列举如下：

["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]


示例 1：

输入：s = "0"
输出：true
示例 2：

输入：s = "e"
输出：false
示例 3：

输入：s = "."
输出：false
示例 4：

输入：s = ".1"
输出：true

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()

        def zhengshu(s):
            if not s:
                return False
            if s[0] in {'+', '-'}:
                s = s[1:]
            if_num = False
            for c in s:
                if str(c).isdigit():
                    if_num = True
                else:
                    return False
            if not if_num:
                return False
            return True

        def xiaoshu(s):
            if not s:
                return False
            if s[0] in {'+', '-'}:
                s = s[1:]
            if_dian, if_num = False, False
            for c in s:
                if c == '.' and not if_dian:
                    if_dian = True
                elif c == '.':
                    return False
                elif str(c).isdigit():
                    if_num = True
                else:
                    return False
            if not if_dian or not if_num:
                return False
            return True

        if 'e' in s or 'E' in s:
            s = s.lower()
            s_split = s.split('e')
            if len(s_split) != 2:
                return False
            if (xiaoshu(s_split[0]) or zhengshu(s_split[0])) and zhengshu(s_split[1]):
                return True
        elif xiaoshu(s) or zhengshu(s):
            return True
        return False


if __name__ == '__main__':
    res = Solution().isNumber(s="    .1    ")
    print(res)
