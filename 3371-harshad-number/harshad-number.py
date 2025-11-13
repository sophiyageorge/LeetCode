class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        nums = str(x)
     
        sum_digits = sum(int(num) for num in nums)
        return sum_digits if x%sum_digits==0 else -1
        