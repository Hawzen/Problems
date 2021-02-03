def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    import heapq
    merged = list(heapq.merge(nums1, nums2))
    
    if len(merged) == 1:
        return merged[0]
    elif len(merged) == 0:
        return 0
    
    middle = len(merged) // 2
    if len(merged) % 2 == 0:
        return (merged[middle-1] + merged[middle]) / 2
    else:
        return merged[middle]
    