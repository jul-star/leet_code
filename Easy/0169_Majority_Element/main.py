"""
    Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
 Could you solve the problem in linear time and in O(1) space?
"""

def majorityElement(nums: list[int]) -> int:
        d:dict[int] = {}
        for i in nums:
            if i in d.keys():
                d[i] +=1
            else:
                d[i]=1
        n = int(len(nums)/2)
        for k in d.keys():
            if d[k] > n :
                return k
        return 0


def main():
    nums = [2,2,1,1,1,2,2]
    out = 2
    res = majorityElement(nums=nums)
    print( f'{out}  == {res}')

if __name__ == '__main__':
    main()