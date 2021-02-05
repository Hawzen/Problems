def threeSum(self, nums: List[int]) -> List[List[int]]:
    if len(nums) < 3: return []
    
    hashes = {}
    res = []
    nums = sorted(nums)        
    
    for k in range(len(nums)):
        i, j = k+1, len(nums)-1
        while i < j:
            summation = nums[i] + nums[j] + nums[k]
            if summation == 0:
                fs = (nums[i], nums[j], nums[k])
                if not hashes.get(hash(fs), 0):
                    hashes[hash(fs)] = True
                    res.append([nums[i], nums[j], nums[k]])
            if summation < 0:
                i += 1
            elif summation > 0:
                j -= 1
            else:
                i, j = i+1, j-1
            
    return res