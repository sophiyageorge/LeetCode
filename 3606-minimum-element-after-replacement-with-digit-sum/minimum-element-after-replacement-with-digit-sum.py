class Solution:
    def minElement(self, nums: List[int]) -> int:
        sum_dig = [sum(int(x) for x in str(num)) for num in nums]
        print(sum_dig)
        return min(sum_dig)        