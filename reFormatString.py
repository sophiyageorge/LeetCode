'''
You are given an alphanumeric string s.
 (Alphanumeric string is a string consisting of
   lowercase English letters and digits).

You have to find a permutation of the string
 where no letter is followed by another letter
   and no digit is followed by another digit. That is,
 no two adjacent characters have the same type.
'''
def reFormat(s:str) -> str:
    result =""
    l = len(s)
    digits = ""
    alpha = ""
    for i in s:
        if i.isdigit():
            digits +=i
        if i.isalpha():
            alpha +=i


    l_reformat= len(digits) if len(digits) > len(alpha) else len(alpha)
    for i in range(l_reformat):
        if len(digits) - len(alpha) >1|-1:
            return ""
        
    return result

# Test cases

print(reFormat("a0b1c2"))

        
