class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        alternate_list = zip_longest(word1,word2,fillvalue='')
        return ''.join(a+b for a,b in alternate_list)

        