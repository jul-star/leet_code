
def searchInsert(nums: list[int], target: int) -> int:
        if nums[0] == target:
             return 0
        if nums[len(nums) - 1] == target:
             return len(nums)-1
        if nums[0] > target:
            return 0
        if nums[len(nums)-1] < target:
            return len(nums)
        
        l = 0
        r = len(nums)-1
        half = int((l+r)/2)
        while nums[half] != target:   
            if half < len(nums)  and nums[half] <target and target<nums[half+1]:    # Non-existed item
                 return half+1
            
            if nums[half] < target:
                l = half
                half = int((l+r)/2)            
            elif nums[half] > target:
                r = half
                half = int((l+r)/2) 
        return half

def main():     
    k = searchInsert(nums = [1,3,5,6], target = 5)
    print('1: ', k , '~', 2)

    k = searchInsert(nums = [1,3,5,6], target = 2)
    print('2: ', k , '~', 1)

    k = searchInsert(nums = [1,3,5,6], target = 7)
    print('3: ', k , '~', 4)

    k = searchInsert(nums = [1,3,5,6], target = 6)
    print('4: ', k , '~', 3)

    k = searchInsert(nums = [1,3,5,6], target = 1)
    print('5: ', k , '~', 0)

    k = searchInsert(nums = [1,3,5,6], target = 0)
    print('6: ', k , '~', 0)

    k = searchInsert(nums =[1,4,6,7,8,9], target = 6)
    print('7: ', k , '~', 2)






if __name__ == '__main__':
     main()