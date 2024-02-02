class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        res:list[int] = []
        sl = str(low)
        i = int(sl[0])
        for ln in range(len(str(low)), len(str(high))+1):
            n = Solution.build_number(i, ln)
            while n <= high:      
                if n >= low and n <= high:
                    res.append(n)
                i += 1
                if i > 9:
                    break
                n = Solution.build_number(i, ln)
            i = 1
            
        return res
            

    def build_number(v:int, ln:int)->int:
        s:str = ''
        for i in range(ln):
            if v+i > 9:
                return 0
            s = s + str(v+i)
        return int(s)

    

def main():
    s = Solution()
    low = 1000
    high = 13000
    l = s.sequentialDigits(low, high)    
    assert l == [1234,2345,3456,4567,5678,6789,12345]

    low = 10
    high = 1000000000

    l1 = s.sequentialDigits(low, high)
    assert l1 == [12,23,34,45,56,67,78,89,123,234,345,456,567,678,789,1234,2345,3456,4567,5678,6789,12345,23456,34567,45678,56789,123456,234567,345678,456789,1234567,2345678,3456789,12345678,23456789,123456789]

if __name__ == '__main__':
    main()