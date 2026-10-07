import numpy as np
class Solution:
    
    def maximumWealth(self, accounts: list[list[int]]) -> int:
    #    accounts =np.array(accounts)
    #    wealth = np.sum(accounts,axis=1)
    #    w = np.max(wealth)
    #    return int(w)
       return max(sum(customer) for customer in accounts)
        
        