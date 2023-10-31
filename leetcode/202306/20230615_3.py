"""
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

示例:

输入: [1,2,3,4,5]
输出: [120,60,40,30,24]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/gou-jian-cheng-ji-shu-zu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def constructArr(self, a):
        if not a:
            return []
        length = len(a)
        res, right = [1]*length, 1
        for i in range(1, length):
            res[i] = res[i-1] * a[i-1]
        for j in range(length-2, -1, -1):
            right = right * a[j + 1]
            res[j] *= right
        return res


if __name__ == '__main__':
    res = Solution().constructArr(a = [1,2,3,4,5])
    print(res)