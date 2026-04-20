class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1_set = set(nums1)
        num2_set = set(nums2)
        answer =[]
        answer.append(list(num1_set-num2_set))
        answer.append(list(num2_set-num1_set))
        print(answer)
        return answer
        