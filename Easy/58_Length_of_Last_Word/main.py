class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t = s.strip()
        # print(f'({t})')
        f = len(t) - (t.rfind(' ')+1)
        # print(f)
        return f
    
def main():
    t = Solution()

    s = "   fly me   to   the moon  "
    i = t.lengthOfLastWord(s)
    assert i == 4

    s = "luffy is still joyboy"
    i = t.lengthOfLastWord(s)
    assert i == 6




    
if __name__ == '__main__':
    main()
        


