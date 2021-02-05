def intToRoman(self, num: int) -> str:
    getMode = {n+1:m for n, m in zip(range(5), "IXCM")}
    res = []
    for i, n in enumerate(reversed(str(num))):
        res.append(self.convert(getMode[i+1], int(n)))
    
    return "".join(res[::-1])

def convert(self, mode, number):
    if number == 0:
        return ""
    
    if mode == "I":
        one, five, ten = "I", "V", "X"
    if mode == "X":
        one, five, ten = "X", "L", "C"
    if mode == "C":
        one, five, ten = "C", "D", "M"
    if mode == "M":
        return "M" * number
        
    converter = {
        1: one,
        2: one * 2,
        3: one * 3,
        4: one + five,
        5: five,
        6: five + one,
        7: five + (one * 2),
        8: five + (one * 3),
        9: one + ten,
    }
    
    return converter[number]