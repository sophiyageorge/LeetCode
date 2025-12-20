class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        words = s.split()
        result = words[::-1]
        return " ".join(result)