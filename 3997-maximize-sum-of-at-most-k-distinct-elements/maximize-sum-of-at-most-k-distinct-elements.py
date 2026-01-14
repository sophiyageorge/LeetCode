class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        # l = 0
        # r = k
        # sum_num =0
        # max_sum = 0
        # result = []
        # while l<k:
        #     for num in nums:
        #         sum_num +=num
        #         if max_sum>sum_num:
        #             result.append(num)

        #         l+=1
        nums = set(nums)
        sort_list = sorted(nums)
        result = []
        print(sort_list)
        # if k>len(nums):
        #     return sorted_list
        reverse = (sort_list[::-1])

        result = (reverse)
        
        return reverse[:k]
        

                




             