class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i = 1
        while i <= len(s)/2:
            if len(s)%len(s[:i]) == 0:
                if self.repeat_to_length(s[:i], len(s)) == s:
                    return True
            i += 1
        return False
    

    def repeat_to_length(self, s:str, wanted:int)->str:
        return (s*int(wanted/len(s)+1))[:wanted]
    

def main():
    t = Solution()

    s = "aabaaba"
    res = t.repeatedSubstringPattern(s)
    assert res == False


if __name__ == '__main__':
    main()
