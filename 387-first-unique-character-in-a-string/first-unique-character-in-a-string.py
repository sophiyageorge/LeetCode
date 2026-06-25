class Solution:
    def firstUniqChar(self, s: str):
        char_dct = {}
        for i in s:
            if i in char_dct:
                char_dct[i]+=1
            else:
                char_dct[i]=1
        indx =0
        for i in s:
           
            if char_dct[i]==1:
                return indx
            indx += 1   
        return -1
        