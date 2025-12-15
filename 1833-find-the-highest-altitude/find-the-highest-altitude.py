class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        currAlt =0
        for g in gain:
            currAlt +=g
            ans = max(ans,currAlt)

        return ans