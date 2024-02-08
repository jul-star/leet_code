class Solution:
    def romanToInt(self, s: str) -> int:              
        if s is None or len(s) == 0:
            return 0
        res = 0
        i = 0 
        tmp = 0 
        while i < len(s):
            if i+1 < len(s):
                tmp = self.get2digits(s[i:i+2])
            if tmp > 0:
                    res += tmp
                    tmp = 0
                    i += 2
            else:
                res += self.get1digits(s[i])
                i += 1
        return res

    def get2digits(self, s:str)->int:
        roman = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400,'CM':900 }
        return roman.get(s, 0)
    
    def get1digits(self, s:str)->int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50,  'C':100, 'D':500, 'M':1000}
        return roman.get(s, 0)

#     def get2digits(self, s:str)->int:
#         if s == 'IV':
#             return 4
#         elif s == 'IX':
#             return 9
#         elif s == 'XL':
#             return 40
#         elif s == 'XC':
#             return 90
#         elif s == 'CD':
#             return 400
#         elif s == 'CM':
#             return 900
#         return 0
    
#     def get1digits(self, s:str)->int:
#         if s == 'I':
#             return 1
#         elif s == 'V':
#             return 5
#         elif s == 'X':
#             return 10
#         elif s == 'L':
#             return 50
#         elif s == 'C':
#             return 100
#         elif s == 'D':
#             return 500
#         elif s == 'M':
#             return 1000
#         return 0


def main():
    s = Solution()
    
    r = 'MCMXCIV'
    n = s.romanToInt(r)
    assert n == 1994

    r = 'MDCXCV'
    n = s.romanToInt(r)
    assert n == 1695


if __name__ == '__main__':
    main()
