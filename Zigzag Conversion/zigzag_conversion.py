def convert(self, s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    sepSize = max(0, numRows - 2)
    block_size = numRows + sepSize
    if len(s) % block_size != 0:
        s +=  " " * (block_size - len(s) % block_size)

    res = []
    for letter in range(numRows):
        for block_num in range(int(len(s) / block_size)):
            res.append(s[block_num * block_size + letter])
            if letter not in (0, numRows-1):
                res.append(s[(block_num+1) * block_size - letter])
    return "".join(res).replace(" ", "")
