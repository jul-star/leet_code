def main():
    i = strStr(haystack = "sadbutsad", needle = "sad")
    print(i, ' ~ 0')
    assert i == 0
    i = strStr(haystack = "leetcode", needle = "leeto")
    print(i, ' ~ -1')
    assert i == -1

    i = strStr(haystack = "leetcode", needle = "eet")
    print(i, ' ~ 1')
    assert i == 1

    i = strStr(haystack = "leetcode", needle = "code")
    print(i, ' ~ 4')
    assert i == 4



def strStr(haystack: str, needle: str) -> int:     
        h = len(haystack) 
        n = len(needle)  
        for i in range(h):
            j=0
            k = i
            while j < n and k < h and needle[j] == haystack[k]:
                  j+=1
                  k+=1
                  if j == n:
                    return i
        return -1
                        


            

if __name__ == '__main__':
      main()