def threeSumClosest(self, nums: List[int], target: int) -> int:
    if len(nums) < 3: return []
    
    nums = sorted(nums)    
    summation = nums[0] + nums[1] + nums[2]
    res, min_close = summation, abs(target - summation)    
    
    for k in range(len(nums)):
        i, j = k+1, len(nums)-1
        while i < j:
            summation = nums[i] + nums[j] + nums[k]
            diff = target - summation
            
            if abs(diff) < min_close:
                min_close = abs(diff)
                res = nums[i] + nums[j] + nums[k]
            if diff > 0:
                i += 1
            elif diff < 0:
                j -= 1
            else:
                return res
            
    return res