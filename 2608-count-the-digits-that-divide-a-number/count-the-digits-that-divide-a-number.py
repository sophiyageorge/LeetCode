class Solution:
    def countDigits(self, num: int) -> int:
        digits = str(num)
        count = 0
        for d in digits:
            if num%int(d) == 0:
                count += 1  
        return count      