def maxArea(self, height: List[int]) -> int:
    if len(height) < 2:
        return 0
    
    maxWater = 0
    i, j = 0, len(height)-1
    while i < j:
        hi, hj = height[i], height[j]
        water = min(hi, hj) * (j-i)
        if water > maxWater:
            maxWater = water
                
        if min(hi, hj) == hi:
            i+=1
        else:
            j-=1
            
    return maxWater
