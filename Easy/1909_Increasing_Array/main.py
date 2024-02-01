class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        d = 0
        l = len(nums)
        if l <= 1:
            return True
        d = self.indexes(l)
        for _, indx in d.items():   
            if len(indx) <= 1:
                return True
            for i in range(1, len(indx)):
                if nums[indx[i-1]] >= nums[indx[i]]:
                    break
                if i == len(indx) - 1:
                    return True
            
        return False    
       
    def indexes(self, l:int)->dict:
        d:dict[int] = {}
        lst = []
        for i in range(l):
            lst.append(i)
        d[0] = lst
        for i in range(l):
            lst = []
            for j in range(l):
                if i != j:
                    lst.append(j)
            d[i+1] = lst            
        return d
    

def main():
    s = Solution()
    assert s.canBeIncreasing([1,1]) == True
    assert s.canBeIncreasing([1,2,10,5,7]) == True
    assert s.canBeIncreasing([1,1,1]) == False
    assert s.canBeIncreasing([2,3,1,2]) == False
    assert s.canBeIncreasing([100,21,100]) == True

    


if __name__ == '__main__':
    main()