class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        L = moves.count('L')
        R = moves.count('R')
        under_score = moves.count('_')

        return abs(R-L)+under_score