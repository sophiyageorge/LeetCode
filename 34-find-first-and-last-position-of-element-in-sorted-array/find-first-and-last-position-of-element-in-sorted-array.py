class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right = 0,len(nums)-1
        first = -1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                right = mid-1
                first = mid

            elif nums[mid]>target:
                right = mid-1
                
            else:
                left = mid+1
                
            
        last =-1
        left,right = 0,len(nums)-1

        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                left = mid+1
                last = mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left  = mid+1

        return [first,last]

        
