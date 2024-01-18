def get_v(r, c, l: list[list[int]]):
    if r < 0 or c < 0 or r > len(l) or c > len(l[r]):
        return 0
  
    if r == 1 or c == 0 or c == len(l[r])-1 :
        return 1
    
    return l[r][c-1] + l[r][c]


def generate(numRows: int) -> list[list[int]]:
    if numRows == 1:
        return [[1]]
    return generate(numRows-1).append(generate_row(numRows))


def generate_row(numRows):
    r = numRows
    _res = []
    for c in range(numRows): 
        if c == 0 or c == numRows-1:
            _res.append(1)
        else:
            _res.append(get_v(r-1, c-1, generate(r-1)) + get_v(r-1, c, generate(r-1)))
    return _res


def triangle()->list[list[int]]:
    l = [[1], [1,1], [1,2,1]]
    print(l[2][1])
