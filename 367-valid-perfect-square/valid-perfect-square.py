class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<2:
            return True
        left =0
        right =num//2
        print(right)

        while left<=right:
            mid = (left+right)//2
            print(mid)
            if mid*mid == num:
                return True
            elif mid*mid>num:
                right = mid-1
            else:
                   left =mid+1
                
        return False
