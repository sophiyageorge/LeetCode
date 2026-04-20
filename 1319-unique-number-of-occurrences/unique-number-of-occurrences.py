
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num] = 1
        set_freq = set()
        for num in freq:
            
            if freq[num] in set_freq:
                return False
            set_freq.add(freq[num])
        return True

        