class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        curr_sum =0
        curr_str =""
        result = ""
        for ch in s:
            if ch.isdigit():
                curr_sum = curr_sum*10+int(ch)
            elif ch=='[':
                stack.append((curr_str,curr_sum))
                curr_sum =0
                curr_str =""
            elif ch==']':
                prev_str,num = stack.pop()
                curr_str = prev_str+num * curr_str
            else:
                curr_str+=ch

        return curr_str