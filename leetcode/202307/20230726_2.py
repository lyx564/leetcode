"""
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

示例 1：
输入：n = 12
输出：5

示例 2：
输入：n = 13
输出：6

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution:
    def countDigitOne(self, n: int) -> int:
        str_n = str(n)
        wei = len(str_n)
        res = 0
        for i in range(wei-1, -1, -1):
            high, low = 0, 0
            if i > 0:
                high = int(str_n[:i])
            if i < wei-1:
                low = int(str_n[i+1:])
            if int(str_n[i]) == 0:
                res += high * pow(10, wei-i-1)
            elif int(str_n[i]) == 1:
                res += high * pow(10, wei-i-1) + 1 + low
            else:
                res += (high + 1) * pow(10, wei-i-1)
        return res


if __name__ == '__main__':
    res = Solution().countDigitOne(n=12106)
    print(res)