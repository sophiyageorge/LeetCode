'''
Given an integer array nums and an integer val,
 remove all occurrences of val in nums in-place.
   The order of the elements may be changed.
 Then return the number of elements in nums which are not equal to val.
'''

from typing import List


def removeElement( nums: List[int], val: int) -> int:
        l = len(nums)
        count=0
        for i in range(l):
            if nums[i]==val:
                continue
            else:
                nums[count]=nums[i]
                count += 1
        return count
nums =[3,2,2,3] 
val =3
print(removeElement(nums, val))