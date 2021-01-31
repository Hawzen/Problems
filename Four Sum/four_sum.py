def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        solutions = set()
        nums.sort()
        for i in range(len(nums) - 3):
            for j in range(i+1, len(nums) - 2):
                lo, hi = j + 1, len(nums) - 1
                while lo < hi:
                    summation = sum((nums[el] for el in [i, j, lo, hi]))
                    if summation == target:
                        solutions.add((nums[i], nums[j], nums[lo], nums[hi]))
                        lo, hi = lo + 1, hi - 1
                    elif summation < target: lo += 1
                    elif summation > target: hi -= 1
        
        return [list(s) for s in  list(solutions)]
        