class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        s = str(n)
        t = int(s, base=3)
        return t % 10 == 0
        # if n <= 0:
        #     return False
        # s = str(n)
        # sum = 0
        # for i in range(len(s)):
        #     try:
        #         sum += int(s[i], base=10)
        #     except Exception as ex:
        #         print(f'{s[i]} : {ex}')
        # if sum % 3 == 0:
        #     return True
        # return False
    
    

def main():
    s = Solution()
    if s.isPowerOfThree(4782969):
        print('True')
    else:
        print('False')




if __name__ == '__main__':
    main()