def reverse(self, x: int) -> int:
    positive = x > 0
    s = str(x if positive else abs(x))

    if len(s) < 10:
        return int(s[::-1]) * (1 if positive else -1)
    elif len(s) > 10:
        return 0

    carry = 0
    for num, max_num in zip(reversed(s), "2147483648"):
        num, max_num = int(num), int(max_num) + carry
        if max_num < num:
            return 0
        carry = (max_num - num) * 10
        
    return int(s[::-1]) * (1 if positive else -1)
