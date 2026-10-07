class Solution:
    import numpy
    def maximumWealth(self, accounts: list[list[int]]) -> int:
       return max(sum(customer) for customer in accounts)
        
        