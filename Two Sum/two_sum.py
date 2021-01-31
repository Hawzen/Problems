def twoSum(self, nums: List[int], target: int) -> List[int]:
        dual_dict = {}
        for i in range(len(nums)):
            if dual_dict.get(nums[i], -1) != -1:
                return [dual_dict.get(nums[i], -1), i]
            dual_dict[target-nums[i]] = i