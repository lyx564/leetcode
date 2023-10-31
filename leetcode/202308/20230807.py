"""
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
请写一个函数，求任意第n位对应的数字。

示例 1：
输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution:
    def findNthDigit(self, n: int) -> int:
        d, count = 1, 9
        num = 0
        while n > num:
            num += d * count
            d += 1
            count *= 10
        d -= 1
        count //= 10
        start_idx = num - d * count
        start_num = pow(10, d-1)
        n = n - start_idx - 1
        i = n % d
        j = n // d
        res = int(str(start_num + j)[i])
        return res




    #
    # 0-9 : 10*1
    # 10-99: 90*2
    # 100-999: 900*3
    # 1000-9999 9000*4
    # 10000-99999 90000*5


if __name__ == '__main__':
    res = Solution().findNthDigit(n=3)
    print(res)