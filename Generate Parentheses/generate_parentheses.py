#     from itertools import product
#     from functools import lru_cache

#     def generateParenthesis(self, n: int) -> List[str]:    
#         if n == 1: return ["()"]
    
#         res = []
#         for digits in product(range(2), repeat=n-1):
#             parns = ["()"]
#             print(digits)
#             for digit in digits:
#                 if digit == 0:
#                     parns.append("()")
#                 else:
#                     parns.append(self.nest(parns.pop()))
#             res.append("".join(parns))
#         return res
    
#     @lru_cache
#     def nest(self, s):
#         return f"({s})"
#         # for i, j in product(range(len(parns))):
def generateParenthesis(self, n: int) -> List[str]:
    if not n: return []
    if n == 1: return ["()"]
    
    res = self.expand(["("], n-1, 0)
    for i in range(len(res)):
        res[i] = res[i] + ")" * self.getOpen(res[i])
    return res
    

def expand(self, parns, n, crnt):
    if n == crnt:
        return parns
        
    res = []
    for parn in parns:
        for i in range(self.getOpen(parn)+1):
            res.append(f"{parn}{')' * i}(")
    
    return self.expand(res, n, crnt+1)
    
def getOpen(self, parn):
    count = 0
    for char in parn:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
    return count