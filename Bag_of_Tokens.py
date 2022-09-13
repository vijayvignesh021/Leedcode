class Solution: 
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l,r=0, len(tokens)-1
        max_score,score = 0,0
        while(l<=r):
            if tokens[l] <= power:
                power -= tokens[l]
                score += 1
                max_score = max(max_score,score)
                l+=1
            elif score > 0:
                power += tokens[r]
                score -= 1
                r-=1
            else:
                break
        return max_score
