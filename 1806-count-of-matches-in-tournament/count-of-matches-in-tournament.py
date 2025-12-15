class Solution:
    def numberOfMatches(self, n: int) -> int:
        sum =0
        while n!=1:
            if n%2 ==0:
                sum+=n/2
                n=n/2
            else :
                sum+=int(n/2)
                n=((n-1)/2)+1
            print(sum)
        return int(sum)
