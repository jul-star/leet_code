class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs is None or len(strs) == 0:
            return ''
        _sorted = sorted(strs)
        m = min(len(_sorted[0]), len(_sorted[-1]))
        for i in range(1, m+1):
            if _sorted[0][:i] != _sorted[-1][:i]:
                return _sorted[0][:i-1]
        return _sorted[0][:m+1]

    # not very good 
    def longestCommonPrefix1(self, strs: list[str]) -> str:
        l = 0
        m = self.get_min(strs)
        if m == 0:
            return ''
        while l <= m:
            l += 1
            if self.is_prefix(strs, l):
                continue
            else:
                return strs[0][:l-1]
        return strs[0][:l]
    
    def is_prefix(self, strs: list[str], l:int) -> bool:
        pref = strs[0][:l]
        for i in range(1, len(strs)):
            if pref != strs[i][:l]:
                return False
        return True


    def get_min(self, strs: list[str])->int:
        if strs is None or len(strs) == 0:
            return 0
        m = len(strs[0])
        for i in range(1, len(strs)):
            if m > len(strs[i]):
                m = len(strs[i])
        return m
    
def main():
    s = Solution()

    strs = ["flower","flow","flight"]
    prefix = s.longestCommonPrefix(strs)
    assert prefix == 'fl'

    strs = ["ab", "a"]
    prefix = s.longestCommonPrefix(strs)
    assert prefix == 'a'

    strs = ["a","b"]
    prefix = s.longestCommonPrefix(strs)
    assert prefix == ''

if __name__ == '__main__':
    main()
