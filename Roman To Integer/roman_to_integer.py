def romanToInt(self, s: str) -> int:
    subt_dict = {
        "V": -2,
        "X": -2,
        "L": -20,
        "C": -20,
        "D": -200,
        "M": -200,
    }
    
    vals_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    
    prev = 1001
    total = 0
    for roman in s:
        val = vals_dict[roman]
        if prev < val:
            print(prev)
            total += subt_dict[roman]
        total += val
        prev = val
        
    
    return total