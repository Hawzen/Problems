def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs: return ""
    i = 0        
    for chars in zip(*strs):
        c = chars[0]
        for char in chars[1:]:
            if c != char:
                return strs[0][:i]
            c = char
        i += 1
    
    return strs[0][:i]