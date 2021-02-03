def myAtoi(self, s: str) -> int:
    s = s.lstrip()
    if len(s) == 0:
        return 0
    
    if not s[0] in ("+", "-") and not s[0].isdigit():
        return 0
    
    if s[0] in ("+", "-"):
        if len(s) == 1 or not s[1].isdigit():
            return 0
        
        positive = s[0] == "+"
        s = s[1:]
    else:
        positive = True
        
    stop = -1
    for i, char in enumerate(s):
        if not char.isdigit():
            stop = i
            break
            
    maximum = 2 ** 31 + (-1 if positive else 0)
    num = int(s) if stop == -1 else int(s[:stop])
    num = num if num < maximum else maximum
    
    return num * (1 if positive else -1)
    