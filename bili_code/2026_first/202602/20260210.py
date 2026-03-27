"""
347. 前 K 个高频元素
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]

提示：
1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的

进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。

https://leetcode.cn/problems/top-k-frequent-elements/description/
"""

class Solution:
    def topKFrequent(self, nums, k: int):
        num_2_freq = {}
        for n in nums:
            if n not in num_2_freq:
                num_2_freq[n] = 0
            num_2_freq[n] += 1
        freq_2_num = {}
        for n in num_2_freq.keys():
            freq = num_2_freq[n]
            if freq not in freq_2_num:
                freq_2_num[freq] = []
            freq_2_num[freq].append(n)
        max_freq = max(freq_2_num.keys())
        all_res = []
        while len(all_res) < k:
            if max_freq in freq_2_num.keys():
                for x in freq_2_num[max_freq]:
                    all_res.append(x)
            max_freq -= 1
        all_res = all_res[:k]
        return all_res



if __name__ == '__main__':
    res = Solution().topKFrequent(nums = [5,3,1,1,1,3,3,1], k = 2)
    print(res)