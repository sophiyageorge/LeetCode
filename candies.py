'''
There are n kids with candies. You are given an
 integer array candies, where each candies[i] 
 represents the number of candies the ith kid has, 
 and an integer extraCandies, denoting the number of
 extra candies that you have.

Return a boolean array result of length n,
 where result[i] is true if, after giving 
 the ith kid all the extraCandies, 
 they will have the greatest number of candies
   among all the kids, or false otherwise.
'''

from typing import List


def kidsWithCandies(candies : List[int], extraCandies :int )-> List[bool]:
    max_candies = max(candies)
    result =[]
    for i in candies :
        if i+extraCandies >= max_candies :
                result.append(True)
        else :
             result.append(False)
    return result

candies = [2,3,5,1,3]
extracandides = 3
print(kidsWithCandies(candies=candies,extraCandies=extracandides))


