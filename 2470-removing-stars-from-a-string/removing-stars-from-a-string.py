class Solution:
    def removeStars(self, s: str) -> str:
       stack = []

       for ch in s:
        if ch is '*':
            stack.pop()
        else:
            stack.append(ch)

       return ''.join(stack)
        
                

        