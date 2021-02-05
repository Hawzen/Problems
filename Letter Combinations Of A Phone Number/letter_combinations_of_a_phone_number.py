def letterCombinations(self, digits: str) -> List[str]:
    if not digits: return digits
    
    from functools import reduce
    
    digits_to_string = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wyxz",
    }
    
    strs = [digits_to_string[d] for d in digits]
    
    return reduce(self.combine, strs)
    
def combine(self, l1, l2):
    res = []
    for char1 in l1:
        for char2 in l2:
            res.append(char1 + char2)
    return res