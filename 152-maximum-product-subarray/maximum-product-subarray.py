class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax,curMin = 1,1

        for n in nums:
            tem = curMax*n
            curMax = max(tem,curMin*n,n)
            curMin = min(tem,curMin*n,n)

            res = max(res,curMax)

        return res
        