class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        cell = n*n
        weight =w
        container =0
        for i in range(cell):
            if maxWeight>=weight:
                weight +=w
                container +=1

        return container
