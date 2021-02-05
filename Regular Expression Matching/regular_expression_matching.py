def isMatch(self, s: str, p: str) -> bool:
    if len(p) == 0:
        if len(s) == 0:
            return True
        return False
    
    if len(p) == 1 and p == s:
        return True
            
#         # Init Succ
#         star = False
#         succ = {}
#         for i in range(len(p) - 1, 0, -1):
#             if p[i] == "*":
#                 star = True
#                 succ[i] = True
#                 continue
        
#             if star:
#                 star = False
#                 succ[i] = True
#                 continue
    
#             succ[i] = False
    
    # Simplify regex
    simplified = []
    star = False
    for i, char in enumerate(p):
        if star:
            if simplified[-2] == char or char == "*":
                continue
            star = False
        
        if char == "*":
            star = True
            
        simplified.append(char)
    p = "".join(simplified)
    
    simplified = []
    star = False
    for i, char in enumerate(p):
        if char == "*":
            star = True
            try:
                flag = True
                while flag:
                    if simplified[-1] == simplified[-2]:
                        simplified[-2].pop()
                    else:
                        flag = False
            except IndexError:
                pass
            
        simplified.append(char)
        
    p = "".join(simplified)
    
    print(f"p after simplification is {p}")
    
    # Loop over string
    star = False
    p_i = len(p)-1
    for i, s_char in enumerate(reversed(s)):
        print("Iteration")
        break_inner = False
        while not break_inner:
            if p_i == -1:
                print("P CONSUMPTION FAILURE")
                return False
            
            if p[p_i] == "*":
                star = True
                p_i += -1

            if star:
                if p[p_i] in (".", s_char):
                    print(f"[star] {p_i} or {p[p_i]} matched {s_char}")
                    if i == len(s) -1:
                        p_i += -1
                    break_inner = True
                else:
                    star = False
                    p_i += -1
                    continue
            
            else:
                if p[p_i] in (".", s_char):
                    print(f"{p_i} or {p[p_i]} matched {s_char}")
                    p_i += -1
                    break_inner = True
                else:
                    print("MATCH FAILURE")
                    return False 
    
    if p_i != -1:
        size = p_i + 1
        if size % 2 == 1:
            print(p_i, "ODD FAILURE")
            return False
        else:
            stars = 0
            if sum([1 for c in p[:p_i+1] if c == "*"]) != size / 2:
                print("SUM FAILURE")
                return False
    return True
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                