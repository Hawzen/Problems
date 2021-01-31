def lengthOfLongestSubstring(self, s: str) -> int:
    longest, substring = 0, []
    for char in s:
        if char in substring:
            longest = max(longest, len(substring))
            substring = substring[substring.index(char)+1:]
        substring.append(char)
        
    return max(longest, len(substring))