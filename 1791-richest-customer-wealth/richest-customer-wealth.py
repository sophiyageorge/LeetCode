import numpy as np
class Solution:
    
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        
    #    return max(sum(customer) for customer in accounts)
       return int(np.max(np.sum(np.array(accounts),axis=1)))
        
        