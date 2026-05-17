class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0 
        max_sum = sum(nums[:k])
        window_sum = sum(nums[:k])

        for right in range(k,len(nums)):
            window_sum += nums[right]
            window_sum -= nums[left]
            
            max_sum = max(max_sum,window_sum)

               

            left += 1
        return max_sum/k

        