class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        word_list = [word[::-1] for word in words]
        return " ".join(word_list)

        