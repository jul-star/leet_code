def singleNumber(nums: list[int]) -> int:
    d:dict[int] = {}
    for i in nums:
        if i in d.keys():
            del d[i]
        else:
            d[i] = 1
    for k in d.keys():
        return k
    
def singleXor(nums: list[int]) -> int:
    """Better than dictionary"""
    x = 0
    for i in nums:
        x ^= i
    return x

def main():
    nums = [2,2,1]
    i = singleNumber(nums)    
    x = singleXor(nums)
    print(f'1 == {i} == {x}')




if __name__ == '__main__':
    main()
