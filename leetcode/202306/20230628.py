"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof/?envType=study-plan-v2&envId=coding-interviews
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    # 直接排序
    def getLeastNumbers_1(self, arr, k: int):
        arr.sort(reverse=False)
        return arr[:k]

    # 二分查找法
    def getLeastNumbers_2(self, arr, k: int):
        if not arr or k == 0:
            return []
        stack = [arr[0]]
        for a in arr[1:]:
            if len(stack) < k or a < stack[-1]:
                if a <= stack[0]:
                    stack = [a] + stack
                else:
                    i, j = 0, len(stack)
                    mid = (i + j) // 2
                    while i < mid < j:
                        if a < stack[mid]:
                            j = mid
                        elif a > stack[mid]:
                            i = mid
                        else:
                            break
                        mid = (i+j) // 2
                    if stack[mid] < a:
                        mid += 1
                    # print(a, i, j, mid, stack)
                    stack = stack[:mid] + [a] + stack[mid:]
                if len(stack) > k:
                    stack = stack[:-1]
        return stack


if __name__ == '__main__':
    res = Solution().getLeastNumbers_2(arr=[0,0,1,2,4,2,2,3,1,4], k=8)
    print(res)