import time
# import regex

def isPalindrome(s: str) -> bool:
    m = s.lower().strip()
    l:list = []
    for c in m:
        if c.isalnum():
            l.append(c)

    print(f'l: {l}')   

    if l is None or len(l) == 0 or len(l) == 1:
        return True
    print(f'l: {l}')
    i = 0
    j = len(l)-1
    while i <= j and l[i] == l[j]:
        if j-i <= 1:
            return True
        i += 1
        j -= 1
    return False

def main():
    # s = "A man, a plan, a canal: Panama"
    # print('Yes') if isPalindrome(s) else print('No')

    # s = ""
    # print('Yes') if isPalindrome(s) else print('No')

    # s = "No"
    # print('Yes') if isPalindrome(s) else print('No')

    # s = "NN"
    # print('Yes') if isPalindrome(s) else print('No')

    # s = ".,"
    # print('Yes') if isPalindrome(s) else print('No')

    s = "0P"
    print('Yes') if isPalindrome(s) else print('No')

if __name__ == '__main__':
    b = time.perf_counter()
    main()
    s = time.perf_counter()
    print(f'{s-b} sec')