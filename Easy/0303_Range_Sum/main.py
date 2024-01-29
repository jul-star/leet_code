class NumArray:

    # def __init__(self, nums: list[int]):
    #     self.nums = []
    #     for i in nums:
    #         self.nums.append(i)
        

    # def sumRange(self, left: int, right: int) -> int:
    #     sum = 0
    #     for i in range(left, right+1, 1):
    #         sum += self.nums[i]
    #     return sum
    
    def __init__(self, nums:list[int]) -> None:
        self.nums = []
        self.nums.append(nums[0])
        for i in range(1, len(nums)):
            self.nums.append(self.nums[i-1] + nums[i])
    
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.nums[right]
        return self.nums[right] - self.nums[left-1]
    
    
def main():
    nm = NumArray([-2, 0, 3, -5, 2, -1])
    print(f'nm: {nm.nums}')
    
    sum = nm.sumRange(0,2)
    print(f'sum: {sum}')

    sum = nm.sumRange(2,5)
    print(f'sum: {sum}')

    sum = nm.sumRange(0,5)
    print(f'sum: {sum}')



if __name__ == '__main__':
    main()