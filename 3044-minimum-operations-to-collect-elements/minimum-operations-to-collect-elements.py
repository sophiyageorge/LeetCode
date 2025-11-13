class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        # n = len(nums)
        # is_added = [False]*k
        # count =0
        # for i in range(n-1,-1,-1):
        #     if nums[i]>k or is_added[nums[i]-1]:
        #         continue
        #     is_added[nums[i]-1] = True
        #     count += 1
        #     if count == k :
        #         return n-i

        seen = set()

        for i,num in enumerate(reversed(nums)):
            if num>k:
                continue
            seen.add(num)
            if k==len(seen):
                return i+1

   