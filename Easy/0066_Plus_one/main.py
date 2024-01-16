def main():
    l1 = plusOne(digits = [1,2,3])
    assert l1 == [1,2,4]

    l2 = plusOne(digits = [4,3,2,1])
    assert l2 == [4,3,2,2]

    l3 = plusOne(digits = [9])
    assert l3 == [1, 0]

    l4 = plusOne(digits = [9,9])
    assert l4 == [1, 0, 0]


    
    
def plusOne(digits: list[int]) -> list[int]:    
    _tmp = 0
    for i in digits:
        _tmp = _tmp*10+i
    _tmp += 1
    _res = list(str(_tmp))
    _out:list[int] = []
    for s in _res:
        _out.append(int(s))
    return _out



if __name__ == '__main__':
    main()