def generate(numRows: int) -> list[list[int]]:
    res = [[1]]
    for r in range(1, numRows, 1):
        if r > 0:
            res.append([])
        for c in range(r+1):
            if c == 0 or c == r:
                res[r].append(1)
            else:
                res[r].append(res[r-1][c-1] + res[r-1][c])
    return res


def main():

    _l1 = generate(1)
    print('l1: ', _l1)
    assert [[1]] == _l1

    _l2 = generate(2)
    print('l2: ', _l2)
    assert [[1], [1,1]] == _l2

    _l3 = generate(3)
    print('l3: ', _l3)
    assert [[1], [1,1], [1,2,1]] == _l3

    _l4 = generate(4)
    print('l4: ', _l4)
    assert [[1], [1,1], [1,2,1], [1,3,3, 1]] == _l4

    _l5 = generate(5)
    print('l5: ', _l5)
    assert [[1], [1,1], [1,2,1], [1,3,3, 1], [1,4,6,4, 1]] == _l5

    _l6 = generate(6)
    print('l6: ', _l6)
    assert [[1], [1,1], [1,2,1], [1,3,3, 1], [1,4,6,4, 1], [1,5,10, 10, 5, 1]] == _l6

if __name__ == '__main__':
    main()

